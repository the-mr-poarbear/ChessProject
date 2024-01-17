import copy
from TransitionNode import TransitionNode
from Piece import Piece
import pygame
from Board import Board

class Pawn(Piece):
     
     def __init__ (self , tag , color , sprite , rowCol ,smallSprite ) :
        super().__init__(  tag , color , sprite , rowCol  , smallSprite)
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
                    
                    if self.color == "white" and self.row == 1:
                        Board.pawnPro = self 
                    elif self.color == "black" and self.row == 8 :
                        Board.pawnPro = self
                    
                    
                    if  self.color == "white"  :
                        
                        piece = Board.getPieceOnGivenSquare(validMove[0] +1 , validMove[1])
                        
                        node = Board.undo.Pop()
                        Board.undo.Push(node)
                        
                        if piece != None and piece.tag == "pawn" and piece.color != self.color and  node and node.movedPiece == piece and piece.secondMove and piece.row == 4 :
                            
                            Board.saveLog(self , self.FileRank(rowCol) , True , fr)
                            Board.pop = True
                            Board.Remove(piece) 
                            Board.undo.Push(TransitionNode(Board.turn , self ,startingPoint, validMove , self.firstMove ,captured = piece , secondMove= self.secondMove ,  pot =Board.pot , promotion = Board.pawnPro)) 
                            Board.Check()

                        else :
                            Board.undo.Push(TransitionNode(Board.turn , self ,startingPoint, validMove , self.firstMove ,captured = captured ,secondMove= self.secondMove  ,  pot =Board.pot , promotion = Board.pawnPro )) 
                            
                        self.enPassant = False
                        
                    elif  self.color == "black" :
                        piece = Board.getPieceOnGivenSquare(validMove[0] - 1 , validMove[1])
                        
                        node = Board.undo.Pop()
                        Board.undo.Push(node)
                        
                        if piece != None and piece.tag == "pawn" and piece.color != self.color and node and node.movedPiece == piece and piece.secondMove and piece.row == 5 :
                            Board.pop = True
                            Board.saveLog(self , self.FileRank(rowCol) , True , fr)
                            Board.Remove(piece)
                            Board.undo.Push(TransitionNode(Board.turn , self ,startingPoint, validMove , self.firstMove ,captured = piece , secondMove= self.secondMove , pot =Board.pot , promotion = Board.pawnPro )) 
                            Board.Check()
                        else :
                            Board.undo.Push(TransitionNode(Board.turn , self ,startingPoint, validMove , self.firstMove ,captured = captured , secondMove= self.secondMove  , pot =Board.pot , promotion = Board.pawnPro )) 
                            
                        self.enPassant = False
                        
                    for piece in Board.pieces :
                        if piece.tag == "pawn" :
                            piece.enPassant = False
                        if piece.tag == "pawn" and piece.color != self.color :
                            piece.canBeEnPa = False
                            
                    
                        
                    if  self.firstMove :
                             #print("1") 
                             if self.row == 4 or self.row == 5 :
                                # print("2")
                                 left = Board.getPieceOnGivenSquare(self.row , self.column - 1)
                                 right = Board.getPieceOnGivenSquare(self.row , self.column + 1) 
                                 if left != None and left.tag == "pawn" and left.color != self.color :
                                     self.enPassant = True
                                 if right != None and right.tag == "pawn" and right.color != self.color :
                                     self.enPassant = True
                                 
                             #self.firstMove = False
                             #self.secondMove = True
                             self.firstMove = False
                          
                    if  self.secondMove :
                       self.secondMove = False   
                      
                    if not self.firstMove :
                        self.secondMove = True 
                        
                    while not Board.redo.IsEmpty() :
                        Board.redo.Pop() 
                        
                    Board.SwitchTurn()
                    self.selected = False
                    
                         
                    Board.CheckMate()
                    
         else :
            self.row = rowCol[0]
            self.column = rowCol[1]
                    
     
     
        
     def MovementSelection(self , ignoreCheck = False) :
          if not ignoreCheck : 
                self.validMoves = [] 
          tempResult = []
          
          for pattern in self.patterns:
                
                 if self.firstMove : 
                    self.canBeEnPa = True
                    
                    temp = self.PawnHandling(ignoreCheck)
                    print("pawnhandl" , temp)
                    tempResult += temp
                    if self.color == "white" :   
                        if Board.getPieceOnGivenSquare(self.row - 1 , self.column) is None :
                            tempResult.append([self.row - 1 , self.column])
                            if Board.getPieceOnGivenSquare(self.row - 2 , self.column) is None :
                                tempResult.append([self.row - 2 , self.column])
                    else : 
                        if Board.getPieceOnGivenSquare(self.row + 1 , self.column) is None :
                            tempResult.append([self.row + 1 , self.column])
                            if Board.getPieceOnGivenSquare(self.row + 2 , self.column) is None :
                                tempResult.append([self.row + 2 , self.column]) 
                         
                        
                 else :
                     self.canBeEnPa = False
                     tempRow = self.row
                     tempCol =  self.column
                     tempRow += pattern[0]  
                     tempCol += pattern[1]  
                 
                     tempResult += self.PawnHandling(ignoreCheck)
      
                     if tempRow <= 0 or tempCol <=0 or tempRow > 8 or tempCol >8 :
                        pass 
                     
                     elif Board.getPieceOnGivenSquare(tempRow , tempCol) is None :  
                         tempResult.append([tempRow,tempCol])
                     else :
                         pass
                     
                 if not ignoreCheck :       
                           self.CheckValidMoves(tempResult) 
                           return self.validMoves
                 else :
                    return tempResult  
                 

     def PawnHandling(self , ignoreCheck) :
        result = []
        
        if self.color == "white" :
              
              print("1")    
              left = Board.getPieceOnGivenSquare(self.row , self.column - 1)
              right = Board.getPieceOnGivenSquare(self.row , self.column + 1) 
              
              node = Board.undo.Pop()
              Board.undo.Push(node)
              
              if left != None and left.tag == "pawn" and node and node.movedPiece == left and left.secondMove and left.row == 4 :
                        
                    result.append([self.row -1 , self.column -1])
              if right != None and right.tag == "pawn" and node and node.movedPiece == right and right.secondMove and right.row == 4  :
                        
                    result.append([self.row -1 , self.column +1]) 
                        
                    
                    
              if Board.getPieceOnGivenSquare(self.row-1 , self.column-1) is not None :
                         
                    if Board.getPieceOnGivenSquare(self.row-1 , self.column-1).color == "black" :       
                        result.append([self.row-1,self.column-1])
                        print("2", result)     
              if Board.getPieceOnGivenSquare(self.row-1 , self.column+1) is not None :
                         
                    if Board.getPieceOnGivenSquare(self.row-1 , self.column+1).color == "black" :               
                        result.append([self.row-1,self.column+1])
                        print("3")     
        elif  self.color == "black" :
            
             
                    
             left = Board.getPieceOnGivenSquare(self.row , self.column - 1)
             right = Board.getPieceOnGivenSquare(self.row , self.column + 1)  
             
             node = Board.undo.Pop()
             Board.undo.Push(node)
             
             if left != None and left.tag == "pawn" and node and node.movedPiece == left and left.secondMove and left.row == 5 :
                        
                    result.append([self.row +1 , self.column -1])
                    
             if right != None and right.tag == "pawn" and node and node.movedPiece == right and right.secondMove and right.row == 5  :
                        
                    result.append([self.row +1 , self.column +1]) 
                        
                        
                   
                     
             if Board.getPieceOnGivenSquare(self.row+1 , self.column-1) is not None :
                         
                    if Board.getPieceOnGivenSquare(self.row+1 , self.column-1).color == "white" :                    
                        result.append([self.row+1,self.column-1])
                        
             if Board.getPieceOnGivenSquare(self.row+1 , self.column+1) is not None :
                        
                    if Board.getPieceOnGivenSquare(self.row+1 , self.column+1).color == "white" :                     
                        result.append([self.row+1,self.column+1])
                        
        return result