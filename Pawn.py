from Piece import Piece
import pygame
from Board import Board

class Pawn(Piece):
     
     def __init__ (self , tag , color , sprite , rowCol ) :
        super().__init__(  tag , color , sprite , rowCol )
        self.shorten = ""
        if self.color == "black" :
            self.patterns = [[1,0]]
        else :
            self.patterns =  [[-1,0]]
        self.firstMove = True
        self.enPassant = False
        self.canBeEnPa = True
        
     def MovementSelection(self , ignoreCheck = False) :
          self.validMoves = [] 
          
          for pattern in self.patterns:
                
                 if self.firstMove : 
                    self.canBeEnPa = True
                    self.PawnHandling(ignoreCheck)
                    if self.color == "white" :       
                        self.validMoves.append([self.row - 1 , self.column])
                        self.validMoves.append([self.row - 2 , self.column])
                    else : 
                        self.validMoves.append([self.row + 1 , self.column])
                        self.validMoves.append([self.row + 2 , self.column]) 
                         
                        
                 else :
                     self.canBeEnPa = False
                     tempRow = self.row
                     tempCol =  self.column
                     tempRow += pattern[0]  
                     tempCol += pattern[1]  
                 
                     self.PawnHandling(ignoreCheck)
      
                     if tempRow <= 0 or tempCol <=0 or tempRow > 8 or tempCol >8 :
                        pass 
                     
                     elif Board.getPieceOnGivenSquare(tempRow , tempCol) is None :  
                         self.validMoves.append([tempRow,tempCol])
                     else :
                         pass
                     
                 if not ignoreCheck :       
                           self.CheckValidMoves(self.validMoves) 
                           
                 
                 return self.validMoves  
                 

     def PawnHandling(self , ignoreCheck) :
         
        
        if self.color == "white" :
              
                   
              left = Board.getPieceOnGivenSquare(self.row , self.column - 1)
              right = Board.getPieceOnGivenSquare(self.row , self.column + 1)  
              if left != None and left.tag == "pawn" and left.enPassant :
                        
                    self.validMoves.append([self.row -1 , self.column -1])
              if right != None and right.tag == "pawn" and right.enPassant :
                        
                    self.validMoves.append([self.row -1 , self.column +1]) 
                        
                    
                    
              if Board.getPieceOnGivenSquare(self.row-1 , self.column-1) is not None :
                         
                    if Board.getPieceOnGivenSquare(self.row-1 , self.column-1).color == "black" :       
                        self.validMoves.append([self.row-1,self.column-1])
                            
              if Board.getPieceOnGivenSquare(self.row-1 , self.column+1) is not None :
                         
                    if Board.getPieceOnGivenSquare(self.row-1 , self.column+1).color == "black" :               
                        self.validMoves.append([self.row-1,self.column+1])
                            
        elif  self.color == "black" :
            
             
                    
              left = Board.getPieceOnGivenSquare(self.row , self.column - 1)
              right = Board.getPieceOnGivenSquare(self.row , self.column + 1)  
              if left != None and left.tag == "pawn" and left.enPassant :
                    self.validMoves.append([self.row +1 , self.column -1])
              if right != None and right.tag == "pawn" and right.enPassant :
                    self.validMoves.append([self.row +1 , self.column +1])
                        
                   
                     
              if Board.getPieceOnGivenSquare(self.row+1 , self.column-1) is not None :
                         
                    if Board.getPieceOnGivenSquare(self.row+1 , self.column-1).color == "white" :                    
                        self.validMoves.append([self.row+1,self.column-1])
                        
              if Board.getPieceOnGivenSquare(self.row+1 , self.column+1) is not None :
                         
                    if Board.getPieceOnGivenSquare(self.row+1 , self.column+1).color == "white" :                     
                        self.validMoves.append([self.row+1,self.column+1])
        