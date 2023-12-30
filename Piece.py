

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
                self.MovementSelection(True)
            position = Board.getPoistionOnGivenSquare(self.row , self.column)
            screen.blit(self.sprite ,( position[0] , position[1]) )
        
        
    def MovementSelection(self , draw) :
         pass
             
            
             
   
       
                        
    def Move(self , rowCol) :
        for validMove in self.validMoves :
             if validMove == rowCol :
                self.row = rowCol[0]
                self.column = rowCol[1]  
                Board.SwitchTurn()
                self.selected = False
                #Board.saveLog(self.tag , self.FileRank(rowCol))
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

    def FileRank(self , rowCol) :
        row = rowCol[0]
        col = rowCol[1]
        
        if row == 1 :
            rank = 8
        elif row ==2 :
            rank = 7
        elif row ==3 :
            rank = 6
        elif row ==4 :
            rank = 5
        elif row ==5 :
            rank = 4
        elif row ==6 :
            rank = 3
        elif row ==7 :
            rank = 2
        elif row ==8 :
            rank = 1
            

        if col == 1 :
            file = "a"
        elif col ==2 :
            file = "b"
        elif col ==3 :
            file = "c"
        elif col ==4 :
            file = "d"
        elif col ==5 :
            file = "e"
        elif col ==6 :
            file = "f"
        elif col ==7 :
            file = "g"
        elif col ==8 :
            file = "h"
        
        return file + str(rank)