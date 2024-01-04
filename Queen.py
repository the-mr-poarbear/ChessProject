from Piece import Piece

import pygame
from Board import Board

class Queen(Piece):
    
    def __init__ (self , tag , color , sprite , rowCol  , smallSprite) :
        super().__init__( tag , color , sprite , rowCol , smallSprite)
        self.patterns = [[0,1] , [1,0] , [-1,0] , [0,-1] , [1,1] , [-1,-1] , [1,-1] , [-1,1] ]
        self.shorten = "Q"
        
    def MovementSelection(self ,  ignoreCheck = False) :
         self.validMoves = [] 
         
         for pattern in self.patterns:
                 tempRow = self.row
                 tempCol =  self.column
                 
                 while not (tempRow <= 0 or tempCol <=0 or tempRow > 8 or tempCol >8) :    
                     tempRow += pattern[0]  
                     tempCol += pattern[1]
                 
                     if tempRow <= 0 or tempCol <=0 or tempRow > 8 or tempCol >8 :
                         break
                     elif Board.getPieceOnGivenSquare(tempRow , tempCol) is None :  
                         
                         self.validMoves.append([tempRow,tempCol])
                     elif Board.getPieceOnGivenSquare(tempRow , tempCol).color != self.color and Board.getPieceOnGivenSquare(tempRow , tempCol).tag !="king":

                         self.validMoves.append([tempRow,tempCol])
                         break
                     elif  Board.getPieceOnGivenSquare(tempRow , tempCol).color != self.color and  Board.getPieceOnGivenSquare(tempRow , tempCol).tag =="king" :
                        
                        self.validMoves.append([tempRow,tempCol])
                     else :
                         break
         if not ignoreCheck :       
                 self.CheckValidMoves(self.validMoves)           
         return self.validMoves  



