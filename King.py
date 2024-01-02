
import time
from Piece import Piece
import pygame
from Board import Board

class King(Piece):
    
    def __init__ (self , tag , color , sprite , rowCol ) :
        super().__init__( tag , color , sprite , rowCol)
        self.patterns = [[0,1] , [1,0] , [-1,0] , [0,-1] , [1,1] , [-1,-1] , [1,-1] , [-1,1] ]
        self.cult = False
        Board.king.append(self)
        self.check = False
        self.checkmate = False
        self.shorten = "K"
        
    def Draw(self) :
        if not self.isDead :
            if self.check :
                position = Board.getPoistionOnGivenSquare(self.row , self.column)      
                pygame.draw.rect(Board.screen , "red", pygame.Rect(position[0] , position[1] , Board.sideOfTheSquare , Board.sideOfTheSquare))
            if self.selected :
                self.MovementSelection()
                self.ShowValidMoves()
            position = Board.getPoistionOnGivenSquare(self.row , self.column)
            Board.screen.blit(self.sprite ,( position[0] , position[1]) )

    def MovementSelection(self  , ignoreCheck = False) :
            
            self.validMoves = [] 
            for pattern in self.patterns:
                    tempRow = self.row
                    tempCol =  self.column
                    tempRow += pattern[0]  
                    tempCol += pattern[1]     
                         
                    if tempRow <= 0 or tempCol <=0 or tempRow > 8 or tempCol >8 :
                        pass 
                    elif Board.getPieceOnGivenSquare(tempRow , tempCol) is None :  
                        self.validMoves.append([tempRow,tempCol])
                            
                    elif Board.getPieceOnGivenSquare(tempRow , tempCol).color != self.color :
                            
                        self.validMoves.append([tempRow,tempCol])  
                    else :
                        pass
                    
            if not ignoreCheck :       
                    self.CheckValidMoves(self.validMoves) 
         
            return self.validMoves 
    
   
    def Checkmate(self):
        if self.check and Board.turn != self.color :
            font = pygame.font.Font("freesansbold.ttf" , 80)
            Board.SwitchTurn
            Board.screen.blit(font.render((Board.turn + ' Won'), True, Board.turn), Board.startingPoint)
            pygame.display.flip()
            Board.run = False   
            time.sleep(3)
            Board.won = Board.turn

