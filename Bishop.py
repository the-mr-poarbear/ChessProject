from Piece import Piece
import pygame
from Board import Board

class Bishop(Piece):
    
    def __init__ (self , tag , color , sprite , rowCol ,smallSprite ) :
        super().__init__( tag , color , sprite , rowCol , smallSprite)
        self.patterns = [ [1,1] , [-1,-1] , [1,-1] , [-1,1] ]
        self.shorten = "B"
        
    def MovementSelection(self  , ignoreCheck = False) :
         if not ignoreCheck : 
            self.validMoves = [] 
         tempResult = []
         
         for pattern in self.patterns:
                 tempRow = self.row
                 tempCol =  self.column
                 
                 while not (tempRow <= 0 or tempCol <=0 or tempRow > 8 or tempCol >8) :    
                     tempRow += pattern[0]  
                     tempCol += pattern[1]
                     
                     if tempRow <= 0 or tempCol <=0 or tempRow > 8 or tempCol >8 :
                         break
                     elif Board.getPieceOnGivenSquare(tempRow , tempCol) is None :  
                         
                         tempResult.append([tempRow,tempCol])
                     elif Board.getPieceOnGivenSquare(tempRow , tempCol).color != self.color and Board.getPieceOnGivenSquare(tempRow , tempCol).tag !="king":

                         tempResult.append([tempRow,tempCol])
                         break
                     elif  Board.getPieceOnGivenSquare(tempRow , tempCol).color != self.color and  Board.getPieceOnGivenSquare(tempRow , tempCol).tag =="king" :
                        
                        tempResult.append([tempRow,tempCol])
                     else :
                         break
                     
         if not ignoreCheck :       
              self.CheckValidMoves(tempResult)           
              return self.validMoves  
         else :
             return tempResult
    




