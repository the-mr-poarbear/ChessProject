import copy
from TransitionNode import TransitionNode
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
        self.secondMove = False
        
     def Move (self ,rowCol , doMove = True  ,captured = None) :
         if doMove :
            for validMove in self.validMoves :
                 
                 if validMove == rowCol :
                    
                    fr = copy.deepcopy(self.FileRank([self.row , self.column]))
                    startingPoint = copy.deepcopy([self.row , self.column])
                    self.row = rowCol[0]
                    self.column = rowCol[1] 
                    
                    
                    if self.tag == "pawn" and self.color == "white"  :
                        piece = Board.getPieceOnGivenSquare(validMove[0] +1 , validMove[1])
                        if piece != None and piece.tag == "pawn" and piece.color != self.color and piece.enPassant :
                            Board.log.pop() 
                            Board.saveLog(self , self.FileRank(rowCol) , True , fr)
                            Board.Remove(piece) 
                            Board.undo.Push(TransitionNode(Board.turn , self ,startingPoint, validMove , self.firstMove ,captured = piece )) 
                            Board.Check()

                        else :
                            Board.undo.Push(TransitionNode(Board.turn , self ,startingPoint, validMove , self.firstMove ,captured = captured )) 
                            
                        self.enPassant = False
                        
                    elif self.tag == "pawn" and self.color == "black" :
                        piece = Board.getPieceOnGivenSquare(validMove[0] - 1 , validMove[1])
                        if piece != None and piece.tag == "pawn" and piece.color != self.color and piece.enPassant :
                            Board.Remove(piece)
                            Board.undo.Push(TransitionNode(Board.turn , self ,startingPoint, validMove , self.firstMove ,captured = piece )) 
                            Board.Check()
                        else :
                            Board.undo.Push(TransitionNode(Board.turn , self ,startingPoint, validMove , self.firstMove ,captured = captured )) 
                            
                        self.enPassant = False
                        
                    for piece in Board.pieces :
                        if piece.tag == "pawn" :
                            piece.enPassant = False
                        if piece.tag == "pawn" and piece.color != self.color :
                            piece.canBeEnPa = False
                            
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
                             self.secondMove = True
                    if self.secondMove :
                        secondMove = False 
                    while not Board.redo.IsEmpty() :
                        Board.redo.Pop() 
                        
                    Board.SwitchTurn()
                    self.selected = False
             
                    Board.CheckMate()
                    
         else :
            self.row = rowCol[0]
            self.column = rowCol[1]
                    
     
     
        
     def MovementSelection(self , ignoreCheck = False) :
          self.validMoves = [] 
          
          for pattern in self.patterns:
                
                 if self.firstMove : 
                    self.canBeEnPa = True
                    self.PawnHandling(ignoreCheck)
                    if self.color == "white" :   
                        if Board.getPieceOnGivenSquare(self.row - 1 , self.column) is None :
                            self.validMoves.append([self.row - 1 , self.column])
                            if Board.getPieceOnGivenSquare(self.row - 2 , self.column) is None :
                                self.validMoves.append([self.row - 2 , self.column])
                    else : 
                        if Board.getPieceOnGivenSquare(self.row + 1 , self.column) is None :
                            self.validMoves.append([self.row + 1 , self.column])
                            if Board.getPieceOnGivenSquare(self.row + 2 , self.column) is None :
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
        