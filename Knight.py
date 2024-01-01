from Piece import Piece
import pygame
from Board import Board

class Knight(Piece):
    
     def __init__ (self , tag , color , sprite , rowCol ) :
        super().__init__( tag , color , sprite , rowCol)
        self.patterns = [[-2,-1] , [-2,1] , [1,-2] , [-1,-2] , [2,-1] , [2,1] , [1,2] , [-1,2] ]
        self.shorten = "N"

     def MovementSelection(self , draw , ignoreCheck = False) :
          self.validMoves = [] 
          
          if Piece.Check() == self.color and not ignoreCheck :
                  startingRow = self.row 
                  startingCol = self.col
                  resultMoves = []
                  self.MovementSelection(False , True) 
                  
                  validMoves = self.validMoves
                  
                  for validMove in validMoves :
                      self.Move(validMove) 
                      if Piece.Check() != self.color :
                         pygame.draw.circle(Board.screen , "blue" , Board.getPoistionOnGivenSquare(tempRow +.5 , tempCol + .5) ,10 )
                         resultMoves.append([self.row , self.column])    
                      self.Move([startingRow , startingCol])
                      
                  self.validMoves =  resultMoves  
              
          else :
              for pattern in self.patterns:
                     tempRow = self.row
                     tempCol =  self.column
                     tempRow += pattern[0]  
                     tempCol += pattern[1]  
               
                  
                             
                         
                     if tempRow <= 0 or tempCol <=0 or tempRow > 8 or tempCol >8 :
                         pass
                     
                     elif Board.getPieceOnGivenSquare(tempRow , tempCol) is None :  
                     
                         if draw :
                             pygame.draw.circle(Board.screen , "blue" , Board.getPoistionOnGivenSquare(tempRow +.5 , tempCol + .5) ,10 )
                         self.validMoves.append([tempRow,tempCol])
                     elif Board.getPieceOnGivenSquare(tempRow , tempCol).color != self.color and Board.getPieceOnGivenSquare(tempRow , tempCol).tag != "king":
                     
                         if draw :
                             pygame.draw.circle(Board.screen , "red" , Board.getPoistionOnGivenSquare(tempRow +.5 , tempCol + .5) ,10 )
                         self.validMoves.append([tempRow,tempCol])
                     elif  Board.getPieceOnGivenSquare(tempRow , tempCol).color != self.color and  Board.getPieceOnGivenSquare(tempRow , tempCol).tag =="king" :
                          if draw : 
                              pygame.draw.circle(Board.screen , "purple" , Board.getPoistionOnGivenSquare(tempRow +.5 , tempCol + .5) ,10 )  
                          self.validMoves.append([tempRow,tempCol])
                     else :
                         pass


