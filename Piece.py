


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
        self.isDead = True
        self.Patterns()
        self.constant = constant
        
    def Draw(self) :
        position = Board.getPoistionOnGivenSquare(self.row , self.column)
        screen.blit(self.sprite ,( position[0] , position[1]) )
        
    def MovementSelection(self) :
         # if constant movement then you can do the pattern as many times as you want until you hit an obsticle 
         if not self.constant :
            for pattern in self.patterns:
                 self.row += pattern[0]  
                 self.column += pattern[1]
                 pygame.draw.circle(Board.screen , "blue" , Board.getPoistionOnGivenSquare(self.row +.5 , self.column + .5) ,10 )
                 self.row -= pattern[0]  
                 self.column -= pattern[1]
     
    def Move(self , rowCol) :
        self.row = rowCol[0]
        self.column = rowCol[1]    
    
    def DeletePiece(self) :
        pass
   
    def Patterns(self) :
        if self.tag == "pawn" :  
            self.patterns = [[1,0] ,]
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
            