from Piece import Piece
import pygame
from Board import Board

class Pawn(Piece):
     
     def __init__ (self , tag , color , sprite , rowCol ) :
        super().__init__(  tag , color , sprite , rowCol )
     
        if self.color == "black" :
            self.patterns = [[1,0] ,]
        else :
            self.patterns =  [[-1,0] ,]
        self.firstMove = True

     def MovementSelection(self ,draw) :
          self.validMoves = [] 
          
          for pattern in self.patterns:
                 tempRow = self.row
                 tempCol =  self.column
                 if self.firstMove : 
                     for i in range(2) :
                          if not (tempRow <= 0 or tempCol <=0 or tempRow > 8 or tempCol >8) :
                             tempRow += pattern[0]  
                             tempCol += pattern[1]   
                             self.PawnHandling(draw)
                             print("1")
                            
                             if tempRow <= 0 or tempCol <=0 or tempRow > 8 or tempCol >8 :
                                 print("gi")
                     
                             elif Board.getPieceOnGivenSquare(tempRow , tempCol) is None :  
                                 print("2")
                                 if draw :
                                    pygame.draw.circle(Board.screen , "blue" , Board.getPoistionOnGivenSquare(tempRow +.5 , tempCol + .5) ,10 )
                                 self.validMoves.append([tempRow,tempCol])
                             else :
                                 pass
                 else :            
                               
                     tempRow += pattern[0]  
                     tempCol += pattern[1]  
                 
                     self.PawnHandling(draw)
                     print("1")
                            
                     if tempRow <= 0 or tempCol <=0 or tempRow > 8 or tempCol >8 :
                         print("gi")
                     
                     elif Board.getPieceOnGivenSquare(tempRow , tempCol) is None :  
                         print("2")
                         if draw :
                            pygame.draw.circle(Board.screen , "blue" , Board.getPoistionOnGivenSquare(tempRow +.5 , tempCol + .5) ,10 )
                         self.validMoves.append([tempRow,tempCol])
                     else :
                         pass

     def PawnHandling(self , draw) :
         
        
        if self.tag == "pawn" and self.color == "white" :
                     
              if Board.getPieceOnGivenSquare(self.row-1 , self.column-1) is not None :
                         
                    if Board.getPieceOnGivenSquare(self.row-1 , self.column-1).color == "black" :
                        if draw :    
                          pygame.draw.circle(Board.screen , "red" , Board.getPoistionOnGivenSquare(self.row-1 +.5 ,  self.column-1 + .5) ,10 )  
                        self.validMoves.append([self.row-1,self.column-1])
                            
              if Board.getPieceOnGivenSquare(self.row-1 , self.column+1) is not None :
                         
                    if Board.getPieceOnGivenSquare(self.row-1 , self.column+1).color == "black" :
                        if draw :   
                           pygame.draw.circle(Board.screen , "red" , Board.getPoistionOnGivenSquare(self.row-1 +.5 ,  self.column+1 + .5) ,10 )  
                        self.validMoves.append([self.row-1,self.column+1])
                            
        elif self.tag == "pawn" and self.color == "black" :
                     
              if Board.getPieceOnGivenSquare(self.row+1 , self.column-1) is not None :
                         
                    if Board.getPieceOnGivenSquare(self.row+1 , self.column-1).color == "white" :
                        if draw :
                             pygame.draw.circle(Board.screen , "red" , Board.getPoistionOnGivenSquare(self.row+1 +.5 ,  self.column-1 + .5) ,10 )  
                        self.validMoves.append([self.row+1,self.column-1])
                        
              if Board.getPieceOnGivenSquare(self.row+1 , self.column+1) is not None :
                         
                    if Board.getPieceOnGivenSquare(self.row+1 , self.column+1).color == "white" :
                        if draw :
                            pygame.draw.circle(Board.screen , "red" , Board.getPoistionOnGivenSquare(self.row+1 +.5 ,  self.column+1 + .5) ,10 )  
                        self.validMoves.append([self.row+1,self.column+1])