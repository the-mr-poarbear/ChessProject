import copy
from unittest import result
from Piece import Piece
import pygame
from Board import Board

class Knight(Piece):
    
     def __init__ (self , tag , color , sprite , rowCol , smallSprite ) :
        super().__init__( tag , color , sprite , rowCol , smallSprite)
        self.patterns = [[-2,-1] , [-2,1] , [1,-2] , [-1,-2] , [2,-1] , [2,1] , [1,2] , [-1,2] ]
        self.shorten = "N"
        

     def MovementSelection(self , ignoreCheck = False) :
            if not ignoreCheck : 
                self.validMoves = [] 
            tempResult = []
     
            for pattern in self.patterns:
                    tempRow = self.row
                    tempCol =  self.column
                    tempRow += pattern[0]  
                    tempCol += pattern[1]     
                         
                    if tempRow <= 0 or tempCol <=0 or tempRow > 8 or tempCol >8 :
                        pass 
                    elif Board.getPieceOnGivenSquare(tempRow , tempCol) is None :  
                        tempResult.append([tempRow,tempCol])
                            
                    elif Board.getPieceOnGivenSquare(tempRow , tempCol).color != self.color :
                            
                        tempResult.append([tempRow,tempCol])  
                    else :
                        pass
                    
            if not ignoreCheck :       
                self.CheckValidMoves(tempResult) 
                return self.validMoves
            else :
                return tempResult       
    