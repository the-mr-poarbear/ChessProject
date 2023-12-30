
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
                self.MovementSelection(True)
            position = Board.getPoistionOnGivenSquare(self.row , self.column)
            Board.screen.blit(self.sprite ,( position[0] , position[1]) )

    def MovementSelection(self , draw) :
          self.validMoves = [] 
          
          for pattern in self.patterns:
                 tempRow = self.row
                 tempCol =  self.column
                 tempRow += pattern[0]  
                 tempCol += pattern[1]  
                 
                  
                             
                         
                 if tempRow <= 0 or tempCol <=0 or tempRow > 8 or tempCol >8 :
                    pass   
                     
                 elif Board.getPieceOnGivenSquare(tempRow , tempCol) is None :  
                     
                     if draw :
                         pygame.draw.circle(Board.screen , "blue" , Board.getPoistionOnGivenSquare(tempRow +.5 , tempCol + .5) ,10 )
                     self.validMoves.append([tempRow,tempCol])
                 elif Board.getPieceOnGivenSquare(tempRow , tempCol).color != self.color and Board.getPieceOnGivenSquare(tempRow , tempCol).tag != "king":
                     
                     if draw :
                         pygame.draw.circle(Board.screen , "red" , Board.getPoistionOnGivenSquare(tempRow +.5 , tempCol + .5) ,10 )
                     self.validMoves.append([tempRow,tempCol])
                 elif  Board.getPieceOnGivenSquare(tempRow , tempCol).color != self.color and  Board.getPieceOnGivenSquare(tempRow , tempCol).tag =="king" :
                      if draw : 
                          pygame.draw.circle(Board.screen , "purple" , Board.getPoistionOnGivenSquare(tempRow +.5 , tempCol + .5) ,10 ) 
                      self.validMoves.append([tempRow,tempCol])
                 else :
                     pass


    def Check():
        
        if Board.king[0].color == "white" :
                kingW =  Board.king[0]
                kingB = Board.king[1]
        else :
                kingB =  Board.king[0]
                kingW = Board.king[1] 
                
        for piece in Board.pieces : 
            
            if piece.color != "white" :
                piece.MovementSelection(False) 
                for validMove in piece.validMoves :
                    if validMove == [kingW.row , kingW.column] :
                        print("white check")
                        kingW.check = True
                        return "white"
                kingW.check = False
                    
            else :
                piece.MovementSelection(False) 
                for validMove in piece.validMoves :
                    if validMove == [kingB.row , kingB.column] :
                        print("black check")
                        kingB.check = True
                        return "black" 
                    
                kingB.check = False
                 
    def Checkmate(self):
        if self.check and Board.turn != self.color :
            font = pygame.font.Font("freesansbold.ttf" , 80)
            Board.SwitchTurn
            Board.screen.blit(font.render((Board.turn + ' Won'), True, Board.turn), Board.startingPoint)
            pygame.display.flip()
            Board.run = False   
            time.sleep(3)
            Board.won = Board.turn

