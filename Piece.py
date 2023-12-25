


from turtle import position

from pygame import draw
import pygame
from Board import Board


screen = Board.screen 


class Piece:
    
    def __init__(self , tag , color , sprite , rowCol , constant = False) :
        self.tag = tag
        self.color = color 
        self.sprite = sprite
        self.row = rowCol[0]
        self.column = rowCol[1]
        self.isDead = False
        self.Patterns()
        self.constant = constant
        self.selected = False
    
       
        
    def Draw(self) :
        if not self.isDead :
            if self.selected :
                self.MovementSelection()
            position = Board.getPoistionOnGivenSquare(self.row , self.column)
            screen.blit(self.sprite ,( position[0] , position[1]) )
        
        
    def MovementSelection(self) :
         self.validMoves = [] 
         # if constant movement then you can do the pattern as many times as you want until you hit an obsticle 
         if not self.constant :
            for pattern in self.patterns:
                 tempRow = self.row
                 tempCol =  self.column
                 tempRow += pattern[0]  
                 tempCol += pattern[1]
                 
                 if tempRow <= 0 or tempCol <=0 or tempRow > 8 or tempCol >8 :
                     print("gi")
                     
                 elif Board.getPieceOnGivenSquare(tempRow , tempCol) is None :  
                     
                     pygame.draw.circle(Board.screen , "blue" , Board.getPoistionOnGivenSquare(tempRow +.5 , tempCol + .5) ,10 )
                     self.validMoves.append([tempRow,tempCol])
                 elif Board.getPieceOnGivenSquare(tempRow , tempCol).color != self.color :
                     pygame.draw.circle(Board.screen , "red" , Board.getPoistionOnGivenSquare(tempRow +.5 , tempCol + .5) ,10 )
                     self.validMoves.append([tempRow,tempCol])
                     
                 else :
                     pass
         else :
             
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
             
     
    def Move(self , rowCol) :
        self.row = rowCol[0]
        self.column = rowCol[1]    
    
    def Delete(self) :
        isDead = True
        print("deleted")
        Board.pieces.remove(self)
        
        
   
    def Patterns(self) :
        if self.tag == "pawn" :  
            if self.color == "black" :
                 self.patterns = [[1,0] ,]
            else :
                self.patterns =  [[-1,0] ,]
        if self.tag == "rook" :
            self.patterns = [[0,1] , [1,0] , [-1,0] , [0,-1]]
        if self.tag == "bishop" :
            self.patterns = [ [1,1] , [-1,-1] , [1,-1] , [-1,1] ]
        if self.tag == "king" :
            self.patterns = [[0,1] , [1,0] , [-1,0] , [0,-1] , [1,1] , [-1,-1] , [1,-1] , [-1,1] ]
        if self.tag == "queen" :
            self.patterns = [[0,1] , [1,0] , [-1,0] , [0,-1] , [1,1] , [-1,-1] , [1,-1] , [-1,1] ]
        if self.tag == "knight" :
            self.patterns = [[-2,-1] , [-2,1] , [1,-2] , [-1,-2] , [2,-1] , [2,1] , [1,2] , [-1,2] ]
            