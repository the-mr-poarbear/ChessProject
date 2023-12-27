from Piece import Piece
import pygame
from Board import Board

class Rook(Piece):
    def __init__ (self , tag , color , sprite , rowCol ) :
        super().__init__( tag , color , sprite , rowCol )
        self.patterns = [[0,1] , [1,0] , [-1,0] , [0,-1]]
        
    def MovementSelection(self) :
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
                     
                         pygame.draw.circle(Board.screen , "blue" , Board.getPoistionOnGivenSquare(tempRow +.5 , tempCol + .5) ,10 )
                         self.validMoves.append([tempRow,tempCol])
                     elif Board.getPieceOnGivenSquare(tempRow , tempCol).color != self.color :
                         pygame.draw.circle(Board.screen , "red" , Board.getPoistionOnGivenSquare(tempRow +.5 , tempCol + .5) ,10 )  
                         self.validMoves.append([tempRow,tempCol])
                         break
                     else :
                         break
    




