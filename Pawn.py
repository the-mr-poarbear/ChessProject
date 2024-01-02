from Piece import Piece
import pygame
from Board import Board

class Pawn(Piece):
     
     def __init__ (self , tag , color , sprite , rowCol ) :
        super().__init__(  tag , color , sprite , rowCol )
        self.shorten = ""
        if self.color == "black" :
            self.patterns = [[1,0] ,]
        else :
            self.patterns =  [[-1,0] ,]
        self.firstMove = True

     def MovementSelection(self , ignoreCheck = False) :
          self.validMoves = [] 
          
          for pattern in self.patterns:
                
                 if self.firstMove : 
                     tempRow = self.row
                     tempCol =  self.column
                     for i in range(2) :
                          
                             tempRow += pattern[0]  
                             tempCol += pattern[1]   
                             self.PawnHandling()
                           
                            
                             if tempRow <= 0 or tempCol <=0 or tempRow > 8 or tempCol >8 :
                                pass
                     
                             elif Board.getPieceOnGivenSquare(tempRow , tempCol) is None :  
                                 
                                 self.validMoves.append([tempRow,tempCol])
                             else :
                                 pass
                 else :
                     tempRow = self.row
                     tempCol =  self.column
                     tempRow += pattern[0]  
                     tempCol += pattern[1]  
                 
                     self.PawnHandling()
      
                     if tempRow <= 0 or tempCol <=0 or tempRow > 8 or tempCol >8 :
                        pass 
                     
                     elif Board.getPieceOnGivenSquare(tempRow , tempCol) is None :  
                         self.validMoves.append([tempRow,tempCol])
                     else :
                         pass
                     
          if not ignoreCheck :       
                   self.CheckValidMoves(self.validMoves)           
          return self.validMoves  

     def PawnHandling(self) :
         
        
        if self.tag == "pawn" and self.color == "white" :
                    
              if Board.getPieceOnGivenSquare(self.row-1 , self.column-1) is not None :
                         
                    if Board.getPieceOnGivenSquare(self.row-1 , self.column-1).color == "black" :       
                        self.validMoves.append([self.row-1,self.column-1])
                            
              if Board.getPieceOnGivenSquare(self.row-1 , self.column+1) is not None :
                         
                    if Board.getPieceOnGivenSquare(self.row-1 , self.column+1).color == "black" :               
                        self.validMoves.append([self.row-1,self.column+1])
                            
        elif self.tag == "pawn" and self.color == "black" :
                     
              if Board.getPieceOnGivenSquare(self.row+1 , self.column-1) is not None :
                         
                    if Board.getPieceOnGivenSquare(self.row+1 , self.column-1).color == "white" :                    
                        self.validMoves.append([self.row+1,self.column-1])
                        
              if Board.getPieceOnGivenSquare(self.row+1 , self.column+1) is not None :
                         
                    if Board.getPieceOnGivenSquare(self.row+1 , self.column+1).color == "white" :                     
                        self.validMoves.append([self.row+1,self.column+1])
        