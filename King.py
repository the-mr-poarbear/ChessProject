
import copy
import time
from TransitionNode import TransitionNode
from Piece import Piece
import pygame
from Board import Board

class King(Piece):
    
    def __init__ (self , tag , color , sprite , rowCol ,smallSprite ) :
        super().__init__( tag , color , sprite , rowCol , smallSprite)
        self.patterns = [[0,1] , [1,0] , [-1,0] , [0,-1] , [1,1] , [-1,-1] , [1,-1] , [-1,1] ]
       
        Board.king.append(self)
        self.check = False
        self.checkmate = False
        self.shorten = "K"
        self.castle = True
        self.canQcastle = False
        self.canKcastle = False
        self.firstMove = True
        
        if self.color == "white" :
            self.castleHousesQ = [[8,4] , [8,3] ,[8,2]]
        else :
            self.castleHousesQ = [[1,4] , [1,3] ,[1,2]]
            
        if self.color == "white" :
            self.castleHousesK = [[8,6] , [8,7]]
        else :
            self.castleHousesK = [[1,6] , [1,7]]
        
     
    def Move(self , rowCol , doMove = True ,captured = None) :
        if doMove :
            
            for validMove in self.validMoves :

                 if validMove == rowCol :
                    self.firstMove = False 
                    startingPoint = copy.deepcopy([self.row , self.column])
                    self.row = rowCol[0]
                    self.column = rowCol[1] 
                    
                    
                    if self.tag == "king" and validMove == self.castleHousesQ[1] and self.canQcastle :
                        
                        if self.color == "white" :
                            targetRook = Board.rookWL
                            
                        else :
                            targetRook = Board.rookBL
                            
                        Board.undo.Push(TransitionNode(Board.turn , self ,startingPoint, validMove  ,captured = captured , castleQ = targetRook , firstMove= self.firstMove ,  pot =Board.pot))   
                        targetRook.column += 3
                        
                    elif self.tag == "king" and validMove == self.castleHousesK[1] and self.canKcastle  :
                        
                        if self.color == "white" :
                            targetRook = Board.rookWR
                        else :
                            targetRook = Board.rookBR
                        Board.undo.Push(TransitionNode(Board.turn , self ,startingPoint, validMove  ,captured = captured , castleK = targetRook , firstMove= self.castle,  pot =Board.pot))
                        targetRook.column -= 2
                    else :
                        Board.undo.Push(TransitionNode(Board.turn , self ,startingPoint, validMove  ,captured = captured ,firstMove= self.castle ,  pot =Board.pot) )
                        
                    for piece in Board.pieces :
                        if piece.tag == "pawn" :
                            piece.enPassant = False
                        if piece.tag == "pawn" and piece.color != self.color :
                            piece.canBeEnPa = False   
                    
                    if self.tag == "king" :
                        if self.color == "white" and ( Board.whiteKingsideCastle or Board.whiteQueensideCastle) :
                            Board.whiteKingsideCastle = False   
                            Board.whiteQueensideCastle = False
                            for king in Board.king :
                                if king.color == "white" :
                                    king.castle = False
                                    
                        elif self.color == "black" and ( Board.blackKingsideCastle or Board.blackQueensideCastle) :
                            Board.blackKingsideCastle = False   
                            Board.blackQueensideCastle = False  
                            for king in Board.king :
                                if king.color == "black" :
                                    king.castle = False
                                    
                    while not Board.redo.IsEmpty() :
                        Board.redo.Pop()
                        
                    Board.SwitchTurn()
                    self.selected = False
             
                    Board.CheckMate()
        else :
            self.row = rowCol[0]
            self.column = rowCol[1]
                    
    def Draw(self) :
        if not self.isDead :
            print(self.check)
            if self.check :
                position = Board.getPoistionOnGivenSquare(self.row , self.column)      
                pygame.draw.rect(Board.screen , "red", pygame.Rect(position[0] , position[1] , Board.sideOfTheSquare , Board.sideOfTheSquare))
            if self.selected :
                self.MovementSelection()
                self.ShowValidMoves()
            position = Board.getPoistionOnGivenSquare(self.row , self.column)
            Board.screen.blit(self.sprite ,( position[0] , position[1]) )

    def MovementSelection(self  , ignoreCheck = False) :
            
            if not ignoreCheck : 
                self.validMoves = [] 
            tempResult = []
            
            for pattern in self.patterns:
                    tempRow = self.row
                    tempCol =  self.column
                    tempRow += pattern[0]  
                    tempCol += pattern[1]     
                         
                    if tempRow <= 0 or tempCol <=0 or tempRow > 8 or tempCol >8 :
                        pass 
                    elif Board.getPieceOnGivenSquare(tempRow , tempCol) is None :  
                        tempResult.append([tempRow,tempCol])
                            
                    elif Board.getPieceOnGivenSquare(tempRow , tempCol).color != self.color :     
                        tempResult.append([tempRow,tempCol])  
                    else :
                        pass
                    
            if not ignoreCheck :       
  
                    castleValMove = self.CastleCheck()   
                    
                    if castleValMove != None :
                        for validCastle in castleValMove :
                            tempResult.append(validCastle)
                            
                    self.CheckValidMoves(tempResult)  
                    return self.validMoves
            else :       
                return tempResult 
    
    def CastleCheck(self) :
        
        if self.castle :
           
            if self.color not in  Board.Check() :
                result = [] 
                startingPoint = copy.deepcopy( [self.row , self.column])
                
                if (Board.blackQueensideCastle and self.color == "black") or (Board.whiteQueensideCastle and self.color == "white") :
                  
                     if Board.getPieceOnGivenSquare(self.castleHousesQ[0][0] , self.castleHousesQ[0][1]) == None and  Board.getPieceOnGivenSquare(self.castleHousesQ[1][0] , self.castleHousesQ[1][1]) == None and Board.getPieceOnGivenSquare(self.castleHousesQ[2][0] , self.castleHousesQ[2][1]) == None :
                        canCastle = True
                        for i in range(2) :
                             self.Move(self.castleHousesQ[i] , False)
                             if self.color in  Board.Check() :
                                canCastle = False       
                             self.Move(startingPoint , False)
                         
                        Board.Check()
                    
                        if canCastle :
                            result.append(self.castleHousesQ[1])
                            self.canQcastle = True
                        
                if (Board.blackKingsideCastle and self.color == "black") or (Board.whiteKingsideCastle and self.color == "white") : 
                    
                     if Board.getPieceOnGivenSquare(self.castleHousesK[0][0] , self.castleHousesK[0][1]) == None and  Board.getPieceOnGivenSquare(self.castleHousesK[1][0] , self.castleHousesK[1][1]) == None  :
                      
                        canCastle = True
                        for house in self.castleHousesK :
                             self.Move(house , False)
                             if self.color in Board.Check() :
                               
                                canCastle = False       
                             self.Move(startingPoint , False)
                         
                        Board.Check()
                    
                        if canCastle :
                           
                            result.append(self.castleHousesK[1])
                            self.canKcastle = True
                        
               
                return result           
                    
            
   
