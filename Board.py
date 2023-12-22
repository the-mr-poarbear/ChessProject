import pygame

class Board:
    
    startingPoint = [550,130]
    sideOfTheSquare = 100
    board = pygame.image.load("ChessProject\Board\APossant.png")
    scaleRate = 0.6
    board = pygame.transform.scale(board , (board.get_width()*scaleRate , board.get_height()*scaleRate)) 
    startingPoint[0] =  startingPoint[0]*scaleRate
    startingPoint[1] =  startingPoint[1]*scaleRate
    sideOfTheSquare = sideOfTheSquare*scaleRate
    
    screen = pygame.display.set_mode([board.get_width() , board.get_height()])
    
    def __init__(self) :
        pass
    
    def getPieceOnGivenSquare(self , row , column) :
        #file is a to h and rank is 1 to 8
        pass 

   
        
     

