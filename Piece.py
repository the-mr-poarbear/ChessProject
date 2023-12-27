
import pygame
from Board import Board


screen = Board.screen 


class Piece:
    
    def __init__(self , tag , color , sprite , rowCol ) :
        self.tag = tag
        self.color = color 
        self.sprite = sprite
        self.row = rowCol[0]
        self.column = rowCol[1]
        self.isDead = False
        self.selected = False
        self.patterns = []
       
        
    def Draw(self) :
        if not self.isDead :
            if self.selected :
                self.MovementSelection()
            position = Board.getPoistionOnGivenSquare(self.row , self.column)
            screen.blit(self.sprite ,( position[0] , position[1]) )
        
        
    def MovementSelection(self) :
         pass
             
            
             
   
       
                        
    def Move(self , rowCol) :
        for validMove in self.validMoves :
             if validMove == rowCol :
                self.row = rowCol[0]
                self.column = rowCol[1]  
                Board.SwitchTurn()
                self.selected = False
                
                if self.tag == "pawn" and  self.firstMove :
                    self.firstMove = False
                
    
    def Delete(self) :
        self.isDead = True
        print("deleted")
        Board.pieces.remove(self)
        
  
  
     
    def KillOpponent(self, opPiece) :
        for validMove in self.validMoves :
                if validMove == [opPiece.row , opPiece.column] :
                    print("bye") 
                    self.Move([opPiece.row , opPiece.column])
                    opPiece.Delete()                           
                    self.selected = False 
                    
                    #Board.SwitchTurn()

   