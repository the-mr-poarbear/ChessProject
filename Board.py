from ast import List
import pygame

class Board:
    
    startingPoint = [550,130]
    sideOfTheSquare = 103
    board = pygame.image.load("ChessProject\Board\APossant.png")
    scaleRate = 0.6
    board = pygame.transform.scale(board , (board.get_width()*scaleRate , board.get_height()*scaleRate)) 
    startingPoint[0] =  startingPoint[0]*scaleRate
    startingPoint[1] =  startingPoint[1]*scaleRate
    sideOfTheSquare = sideOfTheSquare*scaleRate
    
    screen = pygame.display.set_mode([board.get_width() , board.get_height()])
    pieces = []
    def __init__(self) :
        
        pass
    
    def getPieceOnGivenSquare( row , column) :     
        #file is a to h and rank is 1 to 8
        for piece in Board.pieces :
            
            if type(piece) != type([]) :
                print(piece.row , row)
                print(piece.column , column)
                if piece.row == row and piece.column == column :
                    return piece
           
    def getPoistionOnGivenSquare(row , column ) :
        positionX = Board.startingPoint[0] + column * Board.sideOfTheSquare - Board.sideOfTheSquare
        positionY = Board.startingPoint[1] + row * Board.sideOfTheSquare - 16*Board.sideOfTheSquare/16
        return [positionX , positionY]
        

    def getRowColOnGivenPosition(positionX , positionY) :
        row = (positionY - Board.startingPoint[1]) //  Board.sideOfTheSquare + 1
        col = (positionX - Board.startingPoint[0]) //  Board.sideOfTheSquare + 1
        
        return [int(row),int(col)]

