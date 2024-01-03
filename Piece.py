

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
                    fr = copy.deepcopy(self.FileRank([self.row , self.column]))
                    
                    self.row = rowCol[0]
                    self.column = rowCol[1] 
                    
                    if self.tag == "pawn" and self.color == "white"  :
                        piece = Board.getPieceOnGivenSquare(validMove[0] +1 , validMove[1])
                        if piece != None and piece.tag == "pawn" and piece.color != self.color and piece.enPassant :
                            Board.log.pop() 
                            Board.saveLog(self , self.FileRank(rowCol) , Piece.Check() , Piece.CheckMate() , True , fr)
                            Board.Remove(piece) 
                            Piece.Check()
                            
                        self.enPassant = False
                        
                    elif self.tag == "pawn" and self.color == "black" :
                        piece = Board.getPieceOnGivenSquare(validMove[0] - 1 , validMove[1])
                        if piece != None and piece.tag == "pawn" and piece.color != self.color and piece.enPassant :
                            Board.Remove(piece) 
                            Piece.Check()
                            
                        self.enPassant = False
                        
                    for piece in Board.pieces :
                        if piece.tag == "pawn" :
                            piece.enPassant = False
                        if piece.tag == "pawn" and piece.color != self.color :
                            piece.canBeEnPa = False
                    
                    if self.tag == "king" and validMove == self.castleHousesQ[1] and self.canQcastle :
                        #print("goox")
                        if self.color == "white" :
                            targetRook = Board.rookWL
                        else :
                            targetRook = Board.rookBL
                        
                        targetRook.column += 3
                    elif self.tag == "king" and validMove == self.castleHousesK[1] and self.canKcastle  :
                        
                        if self.color == "white" :
                            targetRook = Board.rookWR
                        else :
                            targetRook = Board.rookBR
                        
                        targetRook.column -= 2
                        
                    
                    if self.tag == "king" or self.tag == "rook":
                        if self.color == "white" and ( Board.whiteKingsideCastle or Board.whiteQueensideCastle) :
                            Board.whiteKingsideCastle = False   
                            Board.whiteQueensideCastle = False
                            for king in Board.king :
                                if king.color == "white" :
                                    king.castle = False
                                    
                        elif self.color == "black" and ( Board.blackKingsideCastle or Board.blackQueensideCastle) :
                            Board.blackKingsideCastle = False   
                            Board.blackQueensideCastle = False  
                            for king in Board.king :
                                if king.color == "black" :
                                    king.castle = False
                    
                    Board.SwitchTurn()
                    self.selected = False
                    #Board.saveLog(self.tag , self.FileRank(rowCol))
                    if self.tag == "pawn" and  self.firstMove :
                         #print("1") 
                         if self.row == 4 or self.row == 5 :
                            # print("2")
                             left = Board.getPieceOnGivenSquare(self.row , self.column - 1)
                             right = Board.getPieceOnGivenSquare(self.row , self.column + 1) 
                             if left != None and left.tag == "pawn" and left.color != self.color :
                                 self.enPassant = True
                             if right != None and right.tag == "pawn" and right.color != self.color :
                                 self.enPassant = True
                                 
                         self.firstMove = False
                         
                    
                            
                    Piece.CheckMate()
                    
                    
            
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
                  

                    fr = copy.deepcopy(self.FileRank([self.row , self.column]))
                    #print(fr)
                    self.Move([opPiece.row , opPiece.column]) 
                    Board.saveLog (self  , self.FileRank(validMove) ,Piece.Check() , Piece.CheckMate(), captured=  True  , lastFR = fr )
                    
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
                    #print(enemyPiece.tag)
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
                    tempMoves = copy.deepcopy(piece.MovementSelection(ignoreCheck = True) )
          
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
        
        if Piece.Check() == "white" and Board.turn == "white" :
            
            moves = []
            for piece in Board.pieces :
                if piece.color == "white" :
                   moves += piece.MovementSelection()
            
            if moves == [] :
                print("Black Won")
                #Board.run = False
                return "white"
        elif Piece.Check() == "black" and Board.turn == "black" :
            moves = []
            for piece in Board.pieces :
                if piece.color == "black" :
                   moves += piece.MovementSelection()
            if moves == []:
                print("White Won")
                #Board.run = False
                return "black"