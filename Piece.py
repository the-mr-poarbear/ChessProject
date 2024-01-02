

import copy
from ctypes.wintypes import RGB
import pygame
from Board import Board



screen = Board.screen 


class Piece:
    
    def __init__(self , tag , color , sprite , rowCol ) :
        self.tag = tag
        self.color = color 
        self.sprite = sprite
        self.row = rowCol[0]
        self.column = rowCol[1]
        self.isDead = False
        self.selected = False
        self.patterns = []
       
        
    def Draw(self) :
        if not self.isDead :
            if self.selected :
                self.MovementSelection()
                self.ShowValidMoves()
            position = Board.getPoistionOnGivenSquare(self.row , self.column)
            screen.blit(self.sprite ,( position[0] , position[1]) )
        
        
    def MovementSelection(self , ignoreCheck = False) :
         pass
             
            
    def ShowValidMoves(self) :
        if self.color == "white" :
             for i , validMove in enumerate(self.validMoves) :
            
                pygame.draw.circle(Board.screen , RGB(255-5 * i , 111 , 180 - 5 * i) , Board.getPoistionOnGivenSquare(validMove[0] +.5 , validMove[1] + .5) ,10 ) 
        else :
            for i , validMove in enumerate(self.validMoves) :
            
                pygame.draw.circle(Board.screen , RGB(255-5 * i , 80 , 60 + 5 * i) , Board.getPoistionOnGivenSquare(validMove[0] +.5 , validMove[1] + .5) ,10 ) 
        
   
       
                        
    def Move(self , rowCol , doMove = True) :
        
        if doMove :
            for validMove in self.validMoves :
                 if validMove == rowCol :
                    self.row = rowCol[0]
                    self.column = rowCol[1] 
             
                
                    
                    Board.SwitchTurn()
                    self.selected = False
                    #Board.saveLog(self.tag , self.FileRank(rowCol))
                    if self.tag == "pawn" and  self.firstMove :
                         self.firstMove = False
        else :
            self.row = rowCol[0]
            self.column = rowCol[1] 
            
    
    def Delete(self) :
        self.isDead = True
        #print("deleted")
        Board.pieces.remove(self)
        
  
  
     
    def KillOpponent(self, opPiece) :
        for validMove in self.validMoves :
                if validMove == [opPiece.row , opPiece.column] :
                  

                    fr = copy.deepcopy(self.FileRank([self.row , self.column]))
                    print(fr)
                    self.Move([opPiece.row , opPiece.column]) 
                    Board.saveLog (self  , self.FileRank(validMove) ,Piece.Check() , captured=  True  , lastFR = fr )
                
                    self.selected = False 
                    Board.Remove(opPiece) 
                    Piece.Check()
                    #Board.SwitchTurn()

    def CheckValidMoves(self , tempValidMoves) :
        startingLoc = [self.row  , self.column]
        result = []
        
       
        for validMove in tempValidMoves :
           
            
            
            if Board.getPieceOnGivenSquare(validMove[0] , validMove[1]) != None :
                    enemyPiece = Board.getPieceOnGivenSquare(validMove[0] , validMove[1])
                    print(enemyPiece.tag)
                    enemyPiece.isDead = True
                    if Piece.Check() != self.color :
                        result.append(validMove) 
                    enemyPiece.isDead = False
            #print(validMove)   
            else :
                self.Move(validMove , doMove= False)
                if Piece.Check() != self.color :
                    result.append(validMove) 
                self.Move(startingLoc , doMove= False) 
           
            
            Piece.Check()
        self.validMoves = copy.deepcopy(result)
        

    def FileRank(self , rowCol) :
        row = rowCol[0]
        col = rowCol[1]
        
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
    
    def Check():
        
        if Board.king[0].color == "white" :
                kingW =  Board.king[0]
                kingB = Board.king[1]
        else :
                kingB =  Board.king[0]
                kingW = Board.king[1] 
                
        for piece in Board.pieces : 
            if not piece.isDead :
                if piece.color == "black" :
                    tempMoves = copy.deepcopy(piece.MovementSelection( ignoreCheck = True) )
          
                    for tempMove2 in tempMoves :
                        if tempMove2 == [kingW.row , kingW.column] :
                            #print("white check")
                            kingW.check = True
                            return "white"
                    kingW.check = False
                   
                elif piece.color == "white" : 
                
                    tempMoves2 = copy.deepcopy(piece.MovementSelection(ignoreCheck = True) )
                    for tempMove in tempMoves2 :
                        if tempMove == [kingB.row , kingB.column] :
                            #print("black check")
                            kingB.check = True
                            return "black" 
                    
                    kingB.check = False
    
    def CheckMate() :
        pass