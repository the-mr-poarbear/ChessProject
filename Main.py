from ast import List
import copy

import random 
from tabnanny import check
import time
from tkinter import W
from turtle import pos
import pygame

from Board import Board
from Bishop import Bishop
from King import King
from Knight import Knight
from Pawn import Pawn
from Queen import Queen
from Rook import Rook 
from Piece import Piece 
import mouse
from TransitionNode import TransitionNode
from Stack import Stack
    
#initialize 

pygame.init()
width = 1000 
height = 700 
    

    
    

    
capturedBlackPieces = []
capturedWhitePieces = []
    
# state = 0 => white s turn no selection . 1 => white s turn , selection made .
# 2 => black s turn no selection . 3 => black s turn selection made 
state = 0 
    
   
    

#Board 
board_img = pygame.image.load("ChessProject\Board\APossant.png")
    
size = 50
# White Pieces Sprite    
queen_W_img = pygame.image.load("ChessProject\Pieces\WhitePieces\QueenW.png")
queen_W_img = pygame.transform.scale(queen_W_img , (60,60) )
queen_Ws_img = pygame.transform.scale(queen_W_img , (size,size) )
    
bishop_W_img = pygame.image.load("ChessProject\Pieces\WhitePieces\BishopW.png")
bishop_W_img = pygame.transform.scale(bishop_W_img ,(60,60) )
bishop_Ws_img = pygame.transform.scale(bishop_W_img ,(size,size) )  

king_W_img = pygame.image.load("ChessProject\Pieces\WhitePieces\KingW.png")
king_W_img = pygame.transform.scale(king_W_img , (60,60) )
king_Ws_img = pygame.transform.scale(king_W_img , (size,size) )

knight_W_img = pygame.image.load("ChessProject\Pieces\WhitePieces\KnightW.png")
knight_W_img = pygame.transform.scale(knight_W_img , (60,60))
knight_Ws_img = pygame.transform.scale(knight_W_img ,(size,size))
    
pawn_W_img = pygame.image.load("ChessProject\Pieces\WhitePieces\PawnW.png")
pawn_W_img = pygame.transform.scale(pawn_W_img ,(60,60) )
pawn_Ws_img = pygame.transform.scale(pawn_W_img ,(size,size) )

    
rook_W_img = pygame.image.load("ChessProject\Pieces\WhitePieces\RookW.png")
rook_W_img = pygame.transform.scale(rook_W_img , (60,60))
rook_Ws_img = pygame.transform.scale(rook_W_img , (size,size))
    
   
# Black Pieces Sprite
queen_B_img = pygame.image.load("ChessProject\Pieces\BlackPieces\QueenB.png")
queen_B_img = pygame.transform.scale(queen_B_img , (60,60) )
queen_Bs_img = pygame.transform.scale(queen_B_img , (size,size) )

bishop_B_img = pygame.image.load("ChessProject\Pieces\BlackPieces\BishopB.png")
bishop_B_img = pygame.transform.scale(bishop_B_img , (60,60) )
bishop_Bs_img = pygame.transform.scale(bishop_B_img ,(size,size) )  
    
king_B_img = pygame.image.load("ChessProject\Pieces\BlackPieces\Kingb.png")
king_B_img = pygame.transform.scale(king_B_img , (60,60) )
king_Bs_img = pygame.transform.scale(king_B_img , (size,size) )
    
knight_B_img = pygame.image.load("ChessProject\Pieces\BlackPieces\KnightB.png")
knight_B_img = pygame.transform.scale(knight_B_img , (60,60) )
knight_Bs_img = pygame.transform.scale(knight_B_img , (size,size))
    
pawn_B_img = pygame.image.load("ChessProject\Pieces\BlackPieces\PawnB.png")
pawn_B_img = pygame.transform.scale(pawn_B_img , (60,60) )
pawn_Bs_img = pygame.transform.scale(pawn_B_img ,(size,size) )


    
rook_B_img = pygame.image.load("ChessProject\Pieces\BlackPieces\RookB.png")
rook_B_img = pygame.transform.scale(rook_B_img , (60,60) )
rook_Bs_img = pygame.transform.scale(rook_B_img , (size,size))
    
    
#white pieces initializeation   
queen_W = Queen("queen" , "white" , queen_W_img ,[8 , 4]  ,queen_Ws_img)
    
king_W = King("king" , "white" , king_W_img ,[8 , 5] , king_Ws_img) 
    
bishop_WL = Bishop("bishop" , "white" , bishop_W_img ,[8 , 3]  , bishop_Ws_img)
bishop_WR = Bishop("bishop" , "white" , bishop_W_img ,[8 , 6] , bishop_Ws_img)
    
knight_WL = Knight("knight" , "white" , knight_W_img ,[8 , 2], knight_Ws_img)
knight_WR = Knight("knight" , "white" , knight_W_img ,[8 , 7] , knight_Ws_img)
    
rook_WL = Rook("rook" , "white" , rook_W_img ,[8 , 1] , rook_Ws_img )
rook_WR = Rook("rook" , "white" , rook_W_img ,[8 , 8] , rook_Ws_img )
Board.rookWL =  rook_WL
Board.rookWR = rook_WR

pawn_W1 =  Pawn("pawn" , "white" , pawn_W_img ,[7 , 1] , pawn_Ws_img)
pawn_W2 =  Pawn("pawn" , "white" , pawn_W_img ,[7 , 2] , pawn_Ws_img)
pawn_W3 =  Pawn("pawn" , "white" , pawn_W_img ,[7 , 3] , pawn_Ws_img)
pawn_W4 =  Pawn("pawn" , "white" , pawn_W_img ,[7 , 4] , pawn_Ws_img)
pawn_W5 =  Pawn("pawn" , "white" , pawn_W_img ,[7 , 5] , pawn_Ws_img)
pawn_W6 =  Pawn("pawn" , "white" , pawn_W_img ,[7 , 6] , pawn_Ws_img)
pawn_W7 =  Pawn("pawn" , "white" , pawn_W_img ,[7 , 7] , pawn_Ws_img)
pawn_W8 =  Pawn("pawn" , "white" , pawn_W_img ,[7 , 8] , pawn_Ws_img)


    

whitePieces = [queen_W , bishop_WL , bishop_WR , king_W , knight_WR , knight_WL , pawn_W1 ,pawn_W2,pawn_W3,pawn_W4,pawn_W5,pawn_W6,pawn_W7,pawn_W8 , rook_WL , rook_WR ]
  
#black pieces initializeation 
#  
queen_B = Queen("queen" , "black" , queen_B_img ,[1 , 4] , queen_Bs_img )
    
king_B = King("king" , "black" , king_B_img ,[1 , 5] , king_Bs_img) 
    
bishop_BL = Bishop("bishop" , "black" , bishop_B_img ,[1 , 3] , bishop_Bs_img)
bishop_BR = Bishop("bishop" , "black" , bishop_B_img ,[1 , 6] , bishop_Bs_img)
    
knight_BL = Knight("knight" , "black" , knight_B_img ,[1 , 2] , knight_Bs_img)
knight_BR = Knight("knight" , "black" , knight_B_img ,[1 , 7] , knight_Bs_img)
    
rook_BL = Rook("rook" , "black" , rook_B_img ,[1 , 1] ,rook_Bs_img)
rook_BR = Rook("rook" , "black" , rook_B_img ,[1 , 8] , rook_Bs_img)
Board.rookBL =  rook_BL
Board.rookBR = rook_BR
pawn_B1 =  Pawn("pawn" , "black" , pawn_B_img ,[2 , 1] , pawn_Bs_img)
pawn_B2 =  Pawn("pawn" , "black" , pawn_B_img ,[2 , 2] , pawn_Bs_img)
pawn_B3 =  Pawn("pawn" , "black" , pawn_B_img ,[2 , 3] , pawn_Bs_img)
pawn_B4 =  Pawn("pawn" , "black" , pawn_B_img ,[2 , 4] , pawn_Bs_img)
pawn_B5 =  Pawn("pawn" , "black" , pawn_B_img ,[2 , 5] , pawn_Bs_img)
pawn_B6 =  Pawn("pawn" , "black" , pawn_B_img ,[2 , 6] , pawn_Bs_img)
pawn_B7 =  Pawn("pawn" , "black" , pawn_B_img ,[2 , 7] , pawn_Bs_img)
pawn_B8 =  Pawn("pawn" , "black" , pawn_B_img ,[2 , 8] , pawn_Bs_img)

blackPieces = [queen_B , bishop_BL , bishop_BR , king_B , knight_BR , knight_BL , pawn_B1,pawn_B2,pawn_B3,pawn_B4,pawn_B5,pawn_B6,pawn_B7,pawn_B8 , rook_BL , rook_BR ]
  
    

screen = Board.screen
pygame.display.set_caption("Data Structure Project Chess Game")
smallfont = pygame.font.Font("freesansbold.ttf" , 20)
font = pygame.font.Font("freesansbold.ttf" , 30)
bigFont = pygame.font.Font("freesansbold.ttf" , 50)
veryBigFont = pygame.font.Font("freesansbold.ttf" , 120)
timer = pygame.time.Clock()
fps = 60  
    
    


Board.pieces = [queen_B , bishop_BL , bishop_BR , king_B , knight_BR , knight_BL , pawn_B1,pawn_B2,pawn_B3,pawn_B4,pawn_B5,pawn_B6,pawn_B7,pawn_B8 , rook_BL , rook_BR  ,
                queen_W , bishop_WL , bishop_WR , king_W , knight_WR , knight_WL , pawn_W1 ,pawn_W2,pawn_W3,pawn_W4,pawn_W5,pawn_W6,pawn_W7,pawn_W8 , rook_WL , rook_WR  ]

def Reset():
    
    queen_W = Queen("queen" , "white" , queen_W_img ,[8 , 4]  ,queen_Ws_img)
    
    king_W = King("king" , "white" , king_W_img ,[8 , 5] , king_Ws_img) 
    
    bishop_WL = Bishop("bishop" , "white" , bishop_W_img ,[8 , 3]  , bishop_Ws_img)
    bishop_WR = Bishop("bishop" , "white" , bishop_W_img ,[8 , 6] , bishop_Ws_img)
    
    knight_WL = Knight("knight" , "white" , knight_W_img ,[8 , 2], knight_Ws_img)
    knight_WR = Knight("knight" , "white" , knight_W_img ,[8 , 7] , knight_Ws_img)
    
    rook_WL = Rook("rook" , "white" , rook_W_img ,[8 , 1] , rook_Ws_img )
    rook_WR = Rook("rook" , "white" , rook_W_img ,[8 , 8] , rook_Ws_img )
    Board.rookWL =  rook_WL
    Board.rookWR = rook_WR

    pawn_W1 =  Pawn("pawn" , "white" , pawn_W_img ,[7 , 1] , pawn_Ws_img)
    pawn_W2 =  Pawn("pawn" , "white" , pawn_W_img ,[7 , 2] , pawn_Ws_img)
    pawn_W3 =  Pawn("pawn" , "white" , pawn_W_img ,[7 , 3] , pawn_Ws_img)
    pawn_W4 =  Pawn("pawn" , "white" , pawn_W_img ,[7 , 4] , pawn_Ws_img)
    pawn_W5 =  Pawn("pawn" , "white" , pawn_W_img ,[7 , 5] , pawn_Ws_img)
    pawn_W6 =  Pawn("pawn" , "white" , pawn_W_img ,[7 , 6] , pawn_Ws_img)
    pawn_W7 =  Pawn("pawn" , "white" , pawn_W_img ,[7 , 7] , pawn_Ws_img)
    pawn_W8 =  Pawn("pawn" , "white" , pawn_W_img ,[7 , 8] , pawn_Ws_img)
    
    queen_B = Queen("queen" , "black" , queen_B_img ,[1 , 4] , queen_Bs_img )
    
    king_B = King("king" , "black" , king_B_img ,[1 , 5] , king_Bs_img) 
    
    bishop_BL = Bishop("bishop" , "black" , bishop_B_img ,[1 , 3] , bishop_Bs_img)
    bishop_BR = Bishop("bishop" , "black" , bishop_B_img ,[1 , 6] , bishop_Bs_img)
    
    knight_BL = Knight("knight" , "black" , knight_B_img ,[1 , 2] , knight_Bs_img)
    knight_BR = Knight("knight" , "black" , knight_B_img ,[1 , 7] , knight_Bs_img)
    
    rook_BL = Rook("rook" , "black" , rook_B_img ,[1 , 1] ,rook_Bs_img)
    rook_BR = Rook("rook" , "black" , rook_B_img ,[1 , 8] , rook_Bs_img)
    Board.rookBL =  rook_BL
    Board.rookBR = rook_BR
    pawn_B1 =  Pawn("pawn" , "black" , pawn_B_img ,[2 , 1] , pawn_Bs_img)
    pawn_B2 =  Pawn("pawn" , "black" , pawn_B_img ,[2 , 2] , pawn_Bs_img)
    pawn_B3 =  Pawn("pawn" , "black" , pawn_B_img ,[2 , 3] , pawn_Bs_img)
    pawn_B4 =  Pawn("pawn" , "black" , pawn_B_img ,[2 , 4] , pawn_Bs_img)
    pawn_B5 =  Pawn("pawn" , "black" , pawn_B_img ,[2 , 5] , pawn_Bs_img)
    pawn_B6 =  Pawn("pawn" , "black" , pawn_B_img ,[2 , 6] , pawn_Bs_img)
    pawn_B7 =  Pawn("pawn" , "black" , pawn_B_img ,[2 , 7] , pawn_Bs_img)
    pawn_B8 =  Pawn("pawn" , "black" , pawn_B_img ,[2 , 8] , pawn_Bs_img)
    
    Board.pieces = [queen_B , bishop_BL , bishop_BR , king_B , knight_BR , knight_BL , pawn_B1,pawn_B2,pawn_B3,pawn_B4,pawn_B5,pawn_B6,pawn_B7,pawn_B8 , rook_BL , rook_BR  ,
                queen_W , bishop_WL , bishop_WR , king_W , knight_WR , knight_WL , pawn_W1 ,pawn_W2,pawn_W3,pawn_W4,pawn_W5,pawn_W6,pawn_W7,pawn_W8 , rook_WL , rook_WR  ]
    Board.whiteSideDead = []
    Board.blackSideDead = []
    Board.log = []
    Board.logTxt = ""
    Board.turn = "white"
    Board.won = ""
    Board.pot = False
    Board.i = 0
    Board.pop = False
    Board.selectedPiece = None
    Board.pawnPro = None
    Board.undo = Stack()
    Board.redo = Stack()
    Board.undoLog = Stack()
    Board.redoLog = Stack()
    Board.timer = time.time()

    
def DrawPieces():      
    for piece in Board.pieces :   
            piece.Draw()
            

def DrawWinner():
    
    if Board.won == "white" :
        font = pygame.font.Font("freesansbold.ttf" , 65)
        Board.screen.blit(font.render(("White won"), True, "white"),[ Board.startingPoint[0] + 5/4 * Board.sideOfTheSquare , Board.startingPoint[1] - 5/4 * Board.sideOfTheSquare])
        
    elif Board.won == "black" :
        font = pygame.font.Font("freesansbold.ttf" , 65)
        Board.screen.blit(font.render(("Black won"), True, "white"), [ Board.startingPoint[0] + 5/4 * Board.sideOfTheSquare , Board.startingPoint[1] - 5/4 * Board.sideOfTheSquare])
    elif Board.pot :
        font = pygame.font.Font("freesansbold.ttf" , 65)
        Board.screen.blit(font.render(("Stalemate"), True, "white"), [ Board.startingPoint[0] + 5/4 * Board.sideOfTheSquare , Board.startingPoint[1] - 5/4 * Board.sideOfTheSquare])
        

def Counter() :
    now = time.time()
    
    print(str(int(now - Board.timer)), end="\r")
    timer = str(30 - int(now - Board.timer))
    text = veryBigFont.render(timer, True, (255 ,255 ,255))
    
    if Board.turn == "white" :
        sub = "White's Turn"
    else :
        sub = "Black's Turn"
        
    subText = font.render(sub, True, (255 ,255 ,255))
    X = Board.startingPoint[0] + 10.4 * Board.sideOfTheSquare
    Y = Board.startingPoint[1] + .1 * Board.sideOfTheSquare
    Board.screen.blit(text ,(X,Y) )
    Board.screen.blit(subText ,(X - .4 * Board.sideOfTheSquare , Y + 2 * Board.sideOfTheSquare ) )
    if now - Board.timer >= 30 :
        Board.SwitchTurn()
        
        if Board.turn == "white" :
            Board.won = "white"
            Board.log.append("1-0")
            Board.PrintLog()
        else :
            Board.won = "black"
            Board.log.append("0-1")
            Board.PrintLog()
        Board.SwitchTurn()
 

def DrawLog() :
    
    x_start = Board.startingPoint[0] + 10 * Board.sideOfTheSquare
    y_start = Board.startingPoint[1] + 3.5 * Board.sideOfTheSquare
    x_end = Board.startingPoint[0] + 13 * Board.sideOfTheSquare
    y_end =  Board.startingPoint[1] + 8.7 * Board.sideOfTheSquare
    
    x = x_start
    y = y_start
    
    
    words = Board.logTxt.split(",")
    
    while "" in words :
        words.remove("")
    
    for k in range(Board.i ,len(words)):
        
        word_t = smallfont.render(words[k], True, "white")        
        Board.screen.blit(word_t, (x, y))  
        
        y += word_t.get_height() * 1.1
        if y + word_t.get_height() > y_end :  
            print("aouhrgiu;begroun;ergo;nerg;onesgr;jnergs;kbj")
            Board.i+=1
   
       
   
def DrawDead() :
    
    j = 1
    for i in range(len(Board.whiteSideDead)) :
        
        if i % 4 == 0 :
            j += 1
        
        piece = Board.whiteSideDead[i]
        position = Board.getPositionOnGivenSquareForDead([j ,i%4] , piece.color)
        screen.blit(piece.smallSprite ,( position[0] , position[1]) )
    j = 1
    for i in range(len(Board.blackSideDead)) :
        
        if i % 4 == 0 :
            j += 1
        
        piece = Board.blackSideDead[i]
        position = Board.getPositionOnGivenSquareForDead([j ,i%4] , piece.color)
        screen.blit(piece.smallSprite ,( position[0] , position[1]) )
        
def DrawPromotionMenu() :
    
    
   
    if Board.pawnPro.color == "white" :
        position = Board.getPoistionOnGivenSquare(1 , -1 )
        pygame.draw.rect(Board.screen,(80, 84, 143), pygame.Rect( position[0] ,position[1] ,1 * Board.sideOfTheSquare , 4 * Board.sideOfTheSquare ) )
    
        queen = Board.getPoistionOnGivenSquare(1 , -1 )
        screen.blit(queen_W_img ,( queen[0] , queen[1]) )
    
        knight = Board.getPoistionOnGivenSquare(2 , -1 )
        screen.blit(knight_W_img ,( knight[0] , knight[1]) )
    
        rook = Board.getPoistionOnGivenSquare(3 , -1 )
        screen.blit(rook_W_img ,( rook[0] , rook[1]) )
    
        bishop = Board.getPoistionOnGivenSquare(4 , -1 )
        screen.blit(bishop_W_img ,( bishop[0] , bishop[1]) )
    else :
       
        position = Board.getPoistionOnGivenSquare(5 , -1 )
        pygame.draw.rect(Board.screen,(104, 80, 143), pygame.Rect( position[0] ,position[1] ,1 * Board.sideOfTheSquare , 4 * Board.sideOfTheSquare ) )
    
        queen = Board.getPoistionOnGivenSquare(5 , -1 )
        screen.blit(queen_B_img ,( queen[0] , queen[1]) )
    
        knight = Board.getPoistionOnGivenSquare(6 , -1 )
        screen.blit(knight_B_img ,( knight[0] , knight[1]) )
    
        rook = Board.getPoistionOnGivenSquare(7 , -1 )
        screen.blit(rook_B_img ,( rook[0] , rook[1]) )
    
        bishop = Board.getPoistionOnGivenSquare(8 , -1 )
        screen.blit(bishop_B_img ,( bishop[0] , bishop[1]) )
    
def Promotion() :
    if Board.pawnPro.color == "white" :
                     
        if rowCol == [1 , -1] :
            queenPro = Queen("queen" , "white" , queen_W_img ,[Board.pawnPro.row , Board.pawnPro.column ]  ,queen_Ws_img)
            temp = Board.undo.Pop()
            Board.undo.Push(TransitionNode(temp.turn , temp.movedPiece ,temp.startingPoint, temp.destination , firstMove= temp.firstMove  ,captured= temp.captured ,secondMove= temp.secondMove , pot= temp.pot ,promotion= queenPro )) 
            Board.pieces.remove(Board.pawnPro)
            Board.pieces.append(queenPro)
            posFileRank = Board.FileRank([Board.pawnPro.row , Board.pawnPro.column ])
            Board.log.append(posFileRank + " = " + "Q") 
            Board.pawnPro = None
            Board.undoLog.Push(posFileRank + " = " + "Q") 
            Board.PrintLog()
                        
        elif rowCol == [2 , -1] :
            knightPro = Knight("knight" , "white" , knight_W_img ,[Board.pawnPro.row , Board.pawnPro.column ]  , knight_Ws_img)
            temp = Board.undo.Pop()
            Board.undo.Push(TransitionNode(temp.turn , temp.movedPiece ,temp.startingPoint, temp.destination , firstMove= temp.firstMove  ,captured= temp.captured ,secondMove= temp.secondMove , pot= temp.pot ,promotion= knightPro )) 
            Board.pieces.remove(Board.pawnPro)
            Board.pieces.append(knightPro)
            posFileRank = Board.FileRank([Board.pawnPro.row , Board.pawnPro.column ])
            Board.log.append(posFileRank + " = " + "N") 
            Board.pawnPro = None 
            Board.undoLog.Push(posFileRank + " = " + "N") 
            Board.PrintLog()
                        
        elif rowCol == [3 , -1] :
            rookPro = Rook("rook" , "white" , rook_W_img ,[Board.pawnPro.row , Board.pawnPro.column ], rook_Ws_img )
            temp = Board.undo.Pop()
            Board.undo.Push(TransitionNode(temp.turn , temp.movedPiece ,temp.startingPoint, temp.destination , firstMove= temp.firstMove  ,captured= temp.captured ,secondMove= temp.secondMove , pot= temp.pot ,promotion= rookPro )) 
            Board.pieces.remove(Board.pawnPro)
            Board.pieces.append(rookPro)
            posFileRank = Board.FileRank([Board.pawnPro.row , Board.pawnPro.column ])
            Board.log.append(posFileRank + " = " + "R") 
            Board.pawnPro = None
            Board.undoLog.Push(posFileRank + " = " + "R") 
            Board.PrintLog()
                        
        elif rowCol == [4 , -1] :
            bishopPro = Bishop("bishop" , "white" , bishop_W_img ,[Board.pawnPro.row , Board.pawnPro.column ] , bishop_Ws_img) 
            temp = Board.undo.Pop()
            Board.undo.Push(TransitionNode(temp.turn , temp.movedPiece ,temp.startingPoint, temp.destination , firstMove= temp.firstMove  ,captured= temp.captured ,secondMove= temp.secondMove , pot= temp.pot ,promotion= bishopPro )) 
            Board.pieces.remove(Board.pawnPro)
            Board.pieces.append(bishopPro)      
            posFileRank = Board.FileRank([Board.pawnPro.row , Board.pawnPro.column ])
            Board.log.append(posFileRank + " = " + "B") 
            Board.pawnPro = None
            Board.undoLog.Push(posFileRank + " = " + "B") 
            Board.PrintLog()
            
    else :
        
        if rowCol == [5 , -1] :
            queenPro = Queen("queen" , "black" , queen_B_img ,[Board.pawnPro.row , Board.pawnPro.column ]  ,queen_Bs_img)
            temp = Board.undo.Pop()
            Board.undo.Push(TransitionNode(temp.turn , temp.movedPiece ,temp.startingPoint, temp.destination , firstMove= temp.firstMove  ,captured= temp.captured ,secondMove= temp.secondMove , pot= temp.pot ,promotion= queenPro )) 
            Board.pieces.remove(Board.pawnPro)
            Board.pieces.append(queenPro)
            posFileRank = Board.FileRank([Board.pawnPro.row , Board.pawnPro.column ])
            Board.log.append(posFileRank + " = " + "Q") 
            Board.pawnPro = None
            Board.undoLog.Push(posFileRank + " = " + "Q") 
            Board.PrintLog()
                        
        elif rowCol == [6 , -1] :
            knightPro = Knight("knight" , "black" , knight_B_img ,[Board.pawnPro.row , Board.pawnPro.column ]  , knight_Bs_img)
            temp = Board.undo.Pop()
            Board.undo.Push(TransitionNode(temp.turn , temp.movedPiece ,temp.startingPoint, temp.destination , firstMove= temp.firstMove  ,captured= temp.captured ,secondMove= temp.secondMove , pot= temp.pot ,promotion= knightPro )) 
            Board.pieces.remove(Board.pawnPro)
            Board.pieces.append(knightPro)
            posFileRank = Board.FileRank([Board.pawnPro.row , Board.pawnPro.column ])
            Board.log.append(posFileRank + " = " + "N") 
            Board.pawnPro = None 
            Board.undoLog.Push(posFileRank + " = " + "N") 
            Board.PrintLog()
                        
        elif rowCol == [7 , -1] :
            rookPro = Rook("rook" , "black" , rook_B_img ,[Board.pawnPro.row , Board.pawnPro.column ], rook_Bs_img )
            temp = Board.undo.Pop()
            Board.undo.Push(TransitionNode(temp.turn , temp.movedPiece ,temp.startingPoint, temp.destination , firstMove= temp.firstMove  ,captured= temp.captured ,secondMove= temp.secondMove , pot= temp.pot ,promotion= rookPro )) 
            Board.pieces.remove(Board.pawnPro)
            Board.pieces.append(rookPro)
            posFileRank = Board.FileRank([Board.pawnPro.row , Board.pawnPro.column ])
            Board.log.append(posFileRank + " = " + "R") 
            Board.pawnPro = None
            Board.undoLog.Push(posFileRank + " = " + "R") 
            Board.PrintLog()
                        
        elif rowCol == [8 , -1] :
            bishopPro = Bishop("bishop" , "black" , bishop_B_img ,[Board.pawnPro.row , Board.pawnPro.column ] , bishop_Bs_img) 
            temp = Board.undo.Pop()
            Board.undo.Push(TransitionNode(temp.turn , temp.movedPiece ,temp.startingPoint, temp.destination , firstMove= temp.firstMove  ,captured= temp.captured ,secondMove= temp.secondMove , pot= temp.pot ,promotion= bishopPro )) 
            Board.pieces.remove(Board.pawnPro)
            Board.pieces.append(bishopPro)      
            posFileRank = Board.FileRank([Board.pawnPro.row , Board.pawnPro.column ])
            Board.log.append(posFileRank + " = " + "B") 
            Board.pawnPro = None
            Board.undoLog.Push(posFileRank + " = " + "B") 
            Board.PrintLog()
            
def DrawMouse():
    rowcol = Board.getRowColOnGivenPosition(pygame.mouse.get_pos()[0] , pygame.mouse.get_pos()[1])
    if rowcol[0] > 0 and rowcol[1] > 0 and rowcol[0] <= 8 and rowcol[1] <= 8 :
        
        position = Board.getPoistionOnGivenSquare(rowcol[0] , rowcol[1])
    
        if Board.turn == "white" :
            pygame.draw.rect(Board.screen , (101, 64, 130), pygame.Rect(position[0] , position[1] , Board.sideOfTheSquare , Board.sideOfTheSquare))
        else :
            pygame.draw.rect(Board.screen , (93, 137, 179), pygame.Rect(position[0] , position[1] , Board.sideOfTheSquare , Board.sideOfTheSquare))
        
   
    
    
while Board.run : 
    timer.tick(fps)
    
    screen.blit(Board.board ,(0,0))
    DrawMouse()
    DrawPieces()
    DrawLog()
    DrawDead()
    DrawWinner()
    if Board.pawnPro :
        DrawPromotionMenu()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            file = open("log" + str(random.randrange(0 , 1000)) + ".txt", 'w')
            words = Board.logTxt.replace("," , "\n")
            file.writelines(words)
            file.close()
            Board.run = False
            
            
        undoButPosStart = [Board.startingPoint[0] + 9.8 * Board.sideOfTheSquare , Board.startingPoint[0] + 4.6 * Board.sideOfTheSquare ]  
        undoButPosEnd =  [Board.startingPoint[0] + 10.8 * Board.sideOfTheSquare , Board.startingPoint[0] + 5 * Board.sideOfTheSquare ]  
        #print(undoButPosStart[0] + 7/6 * Board.sideOfTheSquare ,undoButPosEnd[0] + 7/6 * Board.sideOfTheSquare)
        
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] >= undoButPosStart[0] and pygame.mouse.get_pos()[1] >= undoButPosStart[1] and pygame.mouse.get_pos()[0] <= undoButPosEnd[0]  and pygame.mouse.get_pos()[1] <= undoButPosEnd[1] :
             print("Button Undo has been pressed")
             Board.Undo()    
        if event.type == pygame.KEYDOWN  :

            if event.key == pygame.K_z:
                print("Key A has been pressed")
                Board.Undo()
              
                
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] >= undoButPosStart[0] + 7/6 * Board.sideOfTheSquare and pygame.mouse.get_pos()[1] >= undoButPosStart[1] and pygame.mouse.get_pos()[0] <= undoButPosEnd[0] + 7/6 * Board.sideOfTheSquare and pygame.mouse.get_pos()[1] <= undoButPosEnd[1] :
            print("Button Redo has been pressed")
            Board.Redo()
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_r:
                print("Key R has been pressed")
                Board.Redo()
         
                
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] >= undoButPosStart[0] + 14/6 * Board.sideOfTheSquare and pygame.mouse.get_pos()[1] >= undoButPosStart[1] and pygame.mouse.get_pos()[0] <= undoButPosEnd[0] + 14/6 * Board.sideOfTheSquare and pygame.mouse.get_pos()[1] <= undoButPosEnd[1] :
            print("Button has been pressed")
            Reset()
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_x:
                print("Key X has been pressed")
                Reset()
                
        if event.type == pygame.MOUSEBUTTONDOWN and not Board.won :
             #print(pygame.mouse.get_pos[0]) 
            # (x,y) = 
             rowCol = Board.getRowColOnGivenPosition(pygame.mouse.get_pos()[0] , pygame.mouse.get_pos()[1] )
             piece = Board.getPieceOnGivenSquare(rowCol[0] , rowCol[1])
             
             if piece is None and not Board.pawnPro :                
                targetPiece = Board.selectedPiece 
                
                if targetPiece :   
                     targetPiece.MovementSelection()
                     gi = copy.deepcopy(targetPiece.MovementSelection())
                     if rowCol in gi :
                           targetPiece.MovementSelection()
                           targetPiece.Move(rowCol)  
                           print(Board.Check() , "check1")
                           Board.saveLog(targetPiece , targetPiece.FileRank(rowCol) ) 
                           print(Board.Check() , "check2")
                           if Board.pop :
                               Board.log.pop()
                               Board.undoLog.Pop()
                               Board.PrintLog()
                               Board.pop = False
             elif piece == None and Board.pawnPro :
                 Promotion()
           
             elif not piece.selected and Board.turn == piece.color :  
                piece.MovementSelection()
                Board.selectPiece(piece)
                
             elif not piece.selected and Board.turn != piece.color :  
                  targetPiece = Board.selectedPiece   
                   
                  if targetPiece : 
                      targetPiece.MovementSelection()
                      targetPiece.KillOpponent(piece)   
                      
             else : 
                piece.selected = False
                Board.selectedPiece = None
    #king_B.check = king_B.Check() 
    #king_W.check = king_W.Check() 
       
    if Board.won == None or Board.won == "" and not Board.pot :
        Counter()
        
    
    #Board.Check()
    
    #king_W.Checkmate() 
    #king_B.Checkmate() 
    pygame.display.flip()
    #print(pygame.mouse.get_pos() )
       
pygame.quit()



