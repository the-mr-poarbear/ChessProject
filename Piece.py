

import copy
from ctypes.wintypes import RGB
import pygame
from Board import Board
from TransitionNode import TransitionNode



screen = Board.screen 


class Piece:
    
    def __init__(self , tag , color , sprite , rowCol ,smallSprite ) :
        self.tag = tag
        self.color = color 
        self.sprite = sprite
        self.row = rowCol[0]
        self.column = rowCol[1]
        self.isDead = False
        self.selected = False
        self.patterns = []
        self.smallSprite = smallSprite
       
        
    def Draw(self) :
        if not self.isDead :
            if self.selected :
                #self.CheckValidMoves(self.validMoves)
               
                self.ShowValidMoves()
            position = Board.getPoistionOnGivenSquare(self.row , self.column)
            screen.blit(self.sprite ,( position[0] , position[1]) )
        
        
    def MovementSelection(self , ignoreCheck = False) :
         pass
             
            
    def ShowValidMoves(self) :
        if self.color == "white" :
             
             for i , validMove in enumerate(self.validMoves) :
                enemy = Board.getPieceOnGivenSquare(validMove[0] , validMove[1])
                if enemy and enemy.color != Board.turn :
                    pygame.draw.circle(Board.screen , "red" , Board.getPoistionOnGivenSquare(validMove[0] +.5 , validMove[1] + .5) ,10 )    
                else :
                    pygame.draw.circle(Board.screen , RGB(255-7 * i , 111 , 180 - 7 * i) , Board.getPoistionOnGivenSquare(validMove[0] +.5 , validMove[1] + .5) ,10 ) 
        else :
            for i , validMove in enumerate(self.validMoves) :
                
                enemy = Board.getPieceOnGivenSquare(validMove[0] , validMove[1])
                if enemy and enemy.color != Board.turn :
                    pygame.draw.circle(Board.screen , "red" , Board.getPoistionOnGivenSquare(validMove[0] +.5 , validMove[1] + .5) ,10 ) 
                else :
                    pygame.draw.circle(Board.screen , RGB(255-7 * i , 80 , 60 + 7 * i) , Board.getPoistionOnGivenSquare(validMove[0] +.5 , validMove[1] + .5) ,10 ) 
        
   
       
                        
    def Move(self , rowCol , doMove = True , captured = None) :
        
        if doMove :
            for validMove in self.validMoves :
                 
                 if validMove == rowCol :
                    startingPoint = copy.deepcopy([self.row , self.column])
                    
                    fr = copy.deepcopy(self.FileRank([self.row , self.column]))
                    
                    self.row = rowCol[0]
                    self.column = rowCol[1] 
                    if self.tag == "rook" :
                        Board.undo.Push(TransitionNode(Board.turn , self ,startingPoint, validMove ,captured = captured ,firstMove= self.firstMove , pot =Board.pot))   
                    else :
                        Board.undo.Push(TransitionNode(Board.turn , self ,startingPoint, validMove ,captured = captured ,  pot =Board.pot))
                        
                    while not Board.redo.IsEmpty() :
                        Board.redo.Pop()
                    
                        
                    for piece in Board.pieces :
                        if piece.tag == "pawn" :
                            piece.enPassant = False
                        if piece.tag == "pawn" and piece.color != self.color :
                            piece.canBeEnPa = False   
                    
                    if self.tag == "rook":
                        self.firstMove = False
                        if self.color == "white" and Board.whiteKingsideCastle and self == Board.rookWR  :
                            Board.whiteKingsideCastle = False 
                            
                        elif self.color == "white" and Board.whiteQueensideCastle and self == Board.rookWL :
                            Board.whiteQueensideCastle = False
                            
                        elif self.color == "black" and Board.blackKingsideCastle and self == Board.rookBR :
                            Board.blackKingsideCastle = False 
                            
                        elif self.color == "black" and Board.blackQueensideCastle and self == Board.rookBL :
                            Board.blackQueensideCastle = False
   
                            
                    
                    Board.SwitchTurn()
                    self.selected = False   
                    Board.CheckMate()
    
        else :
            
            self.row = rowCol[0]
            self.column = rowCol[1] 
            
    
    def Delete(self) :
        self.isDead = True
        print("deleted")
        Board.pieces.remove(self)
        
  
  
     
    def KillOpponent(self, opPiece) :
        for validMove in self.validMoves :
                if validMove == [opPiece.row , opPiece.column] :
                  
                    Board.Remove(opPiece) 
                    fr = copy.deepcopy(self.FileRank([self.row , self.column]))
                    #print(fr)
                    self.Move([opPiece.row , opPiece.column] , captured = opPiece ) 
                    Board.saveLog (self  , self.FileRank(validMove) , captured=  True  , lastFR = fr )
                    
                    self.selected = False 
                    
                    Board.Check()
                    #Board.SwitchTurn()

    def CheckValidMoves(self , tempValidMoves) :
        #tempValidMoves.append([1,4])
      
        startingLoc =copy.deepcopy([self.row  , self.column])
        result = []

        for validMove in tempValidMoves :
            
            if Board.getPieceOnGivenSquare(validMove[0] , validMove[1]) != None :
                    enemyPiece = Board.getPieceOnGivenSquare(validMove[0] , validMove[1])
                    
                    enemyPiece.isDead = True
                   # Board.Remove(enemyPiece)
                    self.Move(validMove , doMove= False)
                    
                    if self.color not in  Board.Check() :
                        result.append(validMove) 
                    self.Move(startingLoc , doMove= False) 
                    enemyPiece.isDead = False
            #print(validMove)   
            else :
                self.Move(validMove , doMove= False)
                if self.color not in  Board.Check() :
                    result.append(validMove) 
                self.Move(startingLoc , doMove= False)         
            
            Board.Check()
        print(self.tag , result)
        self.validMoves = copy.deepcopy(result)
        

    def FileRank(self , rowCol) :
        row = rowCol[0]
        col = rowCol[1]
        if row<9 and row>0 and col < 9 and col >0:
            if row == 1 :
                rank = 8
            elif row ==2 :
                rank = 7
            elif row ==3 :
                rank = 6
            elif row ==4 :
                rank = 5
            elif row ==5 :
                rank = 4
            elif row ==6 :
                rank = 3
            elif row ==7 :
                rank = 2
            elif row ==8 :
                rank = 1
            

            if col == 1 :
                file = "a"
            elif col ==2 :
                file = "b"
            elif col ==3 :
                file = "c"
            elif col ==4 :
                file = "d"
            elif col ==5 :
                file = "e"
            elif col ==6 :
                file = "f"
            elif col ==7 :
                file = "g"
            elif col ==8 :
                file = "h"
        
            return file + str(rank)
    
    