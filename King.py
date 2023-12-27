from Piece import Piece
import pygame
from Board import Board

class King(Piece):
    
    def __init__ (self , tag , color , sprite , rowCol ) :
        super().__init__( tag , color , sprite , rowCol)
        self.patterns = [[0,1] , [1,0] , [-1,0] , [0,-1] , [1,1] , [-1,-1] , [1,-1] , [-1,1] ]
    

    def MovementSelection(self) :
          self.validMoves = [] 
          
          for pattern in self.patterns:
                 tempRow = self.row
                 tempCol =  self.column
                 tempRow += pattern[0]  
                 tempCol += pattern[1]  
                 print("1")
                  
                             
                         
                 if tempRow <= 0 or tempCol <=0 or tempRow > 8 or tempCol >8 :
                     print("gi")
                     
                 elif Board.getPieceOnGivenSquare(tempRow , tempCol) is None :  
                     print("2")
                     pygame.draw.circle(Board.screen , "blue" , Board.getPoistionOnGivenSquare(tempRow +.5 , tempCol + .5) ,10 )
                     self.validMoves.append([tempRow,tempCol])
                 elif Board.getPieceOnGivenSquare(tempRow , tempCol).color != self.color and Board.getPieceOnGivenSquare(tempRow , tempCol).tag != "king":
                     print("3")         
                     pygame.draw.circle(Board.screen , "red" , Board.getPoistionOnGivenSquare(tempRow +.5 , tempCol + .5) ,10 )
                     self.validMoves.append([tempRow,tempCol])
                 elif  Board.getPieceOnGivenSquare(tempRow , tempCol).color != self.color and  Board.getPieceOnGivenSquare(tempRow , tempCol).tag =="king" and self.tag != "pawn" :
                      pygame.draw.circle(Board.screen , "purple" , Board.getPoistionOnGivenSquare(tempRow +.5 , tempCol + .5) ,10 )   
                 else :
                     pass






