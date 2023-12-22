


from turtle import position

from pygame import draw
from Board import Board


screen = Board.screen 


class Piece:
    
    def __init__(self , tag , color , sprite , rowCol) :
        self.tag = tag
        self.color = color 
        self.sprite = sprite
        self.row = rowCol[0]
        self.column = rowCol[1]
        self.isDead = True
        
    def Draw(self) :
        position = self.getPoistionOnGivenSquare(self.row , self.column)
        screen.blit(self.sprite ,( position[0] , position[1]) )
        
    def Move(self , rowCol ) :
         self.row = rowCol[0]
         self.column = rowCol[1]
         self.Draw()
         
    
    def DeletePiece(self) :
        pass

    def getPoistionOnGivenSquare(self ,row , column ) :
        positionX = Board.startingPoint[0] + column * Board.sideOfTheSquare - Board.sideOfTheSquare
        positionY = Board.startingPoint[1] + row * Board.sideOfTheSquare - 13*Board.sideOfTheSquare/16
        return [positionX , positionY]