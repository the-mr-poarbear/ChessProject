from ast import List
import copy
from tabnanny import check
import time
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
    

# White Pieces Sprite    
queen_W_img = pygame.image.load("ChessProject\Pieces\WhitePieces\QueenW.png")
queen_W_img = pygame.transform.scale(queen_W_img , (60,60) )
    
bishop_W_img = pygame.image.load("ChessProject\Pieces\WhitePieces\BishopW.png")
bishop_W_img = pygame.transform.scale(bishop_W_img ,(60,60) )
    
king_W_img = pygame.image.load("ChessProject\Pieces\WhitePieces\KingW.png")
king_W_img = pygame.transform.scale(king_W_img , (60,60) )
    
knight_W_img = pygame.image.load("ChessProject\Pieces\WhitePieces\KnightW.png")
knight_W_img = pygame.transform.scale(knight_W_img , (60,60))
    
pawn_W_img = pygame.image.load("ChessProject\Pieces\WhitePieces\PawnW.png")
pawn_W_img = pygame.transform.scale(pawn_W_img ,(60,60) )
    
rook_W_img = pygame.image.load("ChessProject\Pieces\WhitePieces\RookW.png")
rook_W_img = pygame.transform.scale(rook_W_img , (60,60))
    
   
# Black Pieces Sprite
queen_B_img = pygame.image.load("ChessProject\Pieces\BlackPieces\QueenB.png")
queen_B_img = pygame.transform.scale(queen_B_img , (60,60) )
    
bishop_B_img = pygame.image.load("ChessProject\Pieces\BlackPieces\BishopB.png")
bishop_B_img = pygame.transform.scale(bishop_B_img , (60,60) )
    
king_B_img = pygame.image.load("ChessProject\Pieces\BlackPieces\Kingb.png")
king_B_img = pygame.transform.scale(king_B_img , (60,60) )
    
knight_B_img = pygame.image.load("ChessProject\Pieces\BlackPieces\KnightB.png")
knight_B_img = pygame.transform.scale(knight_B_img , (60,60) )
    
pawn_B_img = pygame.image.load("ChessProject\Pieces\BlackPieces\PawnB.png")
pawn_B_img = pygame.transform.scale(pawn_B_img , (60,60) )
    
rook_B_img = pygame.image.load("ChessProject\Pieces\BlackPieces\RookB.png")
rook_B_img = pygame.transform.scale(rook_B_img , (60,60) )
    
    
#white pieces initializeation   
queen_W = Queen("queen" , "white" , queen_W_img ,[8 , 4] )
    
king_W = King("king" , "white" , king_W_img ,[8 , 5]) 
    
bishop_WL = Bishop("bishop" , "white" , bishop_W_img ,[8 , 3] )
bishop_WR = Bishop("bishop" , "white" , bishop_W_img ,[8 , 6] )
    
knight_WL = Knight("knight" , "white" , knight_W_img ,[8 , 2])
knight_WR = Knight("knight" , "white" , knight_W_img ,[8 , 7])
    
rook_WL = Rook("rook" , "white" , rook_W_img ,[8 , 1] )
rook_WR = Rook("rook" , "white" , rook_W_img ,[8 , 8] )
Board.rookWL =  rook_WL
Board.rookWR = rook_WR

pawn_W1 =  Pawn("pawn" , "white" , pawn_W_img ,[7 , 1])
pawn_W2 =  Pawn("pawn" , "white" , pawn_W_img ,[7 , 2])
pawn_W3 =  Pawn("pawn" , "white" , pawn_W_img ,[7 , 3])
pawn_W4 =  Pawn("pawn" , "white" , pawn_W_img ,[7 , 4])
pawn_W5 =  Pawn("pawn" , "white" , pawn_W_img ,[7 , 5])
pawn_W6 =  Pawn("pawn" , "white" , pawn_W_img ,[7 , 6])
pawn_W7 =  Pawn("pawn" , "white" , pawn_W_img ,[7 , 7])
pawn_W8 =  Pawn("pawn" , "white" , pawn_W_img ,[7 , 8])


    

whitePieces = [queen_W , bishop_WL , bishop_WR , king_W , knight_WR , knight_WL , pawn_W1 ,pawn_W2,pawn_W3,pawn_W4,pawn_W5,pawn_W6,pawn_W7,pawn_W8 , rook_WL , rook_WR ]
  
#black pieces initializeation   
queen_B = Queen("queen" , "black" , queen_B_img ,[1 , 4] )
    
king_B = King("king" , "black" , king_B_img ,[1 , 5]) 
    
bishop_BL = Bishop("bishop" , "black" , bishop_B_img ,[1 , 3])
bishop_BR = Bishop("bishop" , "black" , bishop_B_img ,[1 , 6])
    
knight_BL = Knight("knight" , "black" , knight_B_img ,[1 , 2])
knight_BR = Knight("knight" , "black" , knight_B_img ,[1 , 7])
    
rook_BL = Rook("rook" , "black" , rook_B_img ,[1 , 1])
rook_BR = Rook("rook" , "black" , rook_B_img ,[1 , 8])
Board.rookBL =  rook_BL
Board.rookBR = rook_BR
pawn_B1 =  Pawn("pawn" , "black" , pawn_B_img ,[2 , 1])
pawn_B2 =  Pawn("pawn" , "black" , pawn_B_img ,[2 , 2])
pawn_B3 =  Pawn("pawn" , "black" , pawn_B_img ,[2 , 3])
pawn_B4 =  Pawn("pawn" , "black" , pawn_B_img ,[2 , 4])
pawn_B5 =  Pawn("pawn" , "black" , pawn_B_img ,[2 , 5])
pawn_B6 =  Pawn("pawn" , "black" , pawn_B_img ,[2 , 6])
pawn_B7 =  Pawn("pawn" , "black" , pawn_B_img ,[2 , 7])
pawn_B8 =  Pawn("pawn" , "black" , pawn_B_img ,[2 , 8])

blackPieces = [queen_B , bishop_BL , bishop_BR , king_B , knight_BR , knight_BL , pawn_B1,pawn_B2,pawn_B3,pawn_B4,pawn_B5,pawn_B6,pawn_B7,pawn_B8 , rook_BL , rook_BR ]
  
    

screen = Board.screen
pygame.display.set_caption("Data Structure Project Chess Game")
font = pygame.font.Font("freesansbold.ttf" , 30)
bigFont = pygame.font.Font("freesansbold.ttf" , 50)
veryBigFont = pygame.font.Font("freesansbold.ttf" , 120)
timer = pygame.time.Clock()
fps = 60  
    
    


Board.pieces = [queen_B , bishop_BL , bishop_BR , king_B , knight_BR , knight_BL , pawn_B1,pawn_B2,pawn_B3,pawn_B4,pawn_B5,pawn_B6,pawn_B7,pawn_B8 , rook_BL , rook_BR  ,
                queen_W , bishop_WL , bishop_WR , king_W , knight_WR , knight_WL , pawn_W1 ,pawn_W2,pawn_W3,pawn_W4,pawn_W5,pawn_W6,pawn_W7,pawn_W8 , rook_WL , rook_WR  ]
def DrawPieces():      
    for piece in Board.pieces :   
            piece.Draw()
            
    #for pieceW in Board.whiteSideDead :
    #    pieceW.DrawDeadW()
        
    #for pieceB in Board.blackSideDead :
    #    pieceB.DrawDeadB()
       
#run loop 
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
    
while Board.run : 
    timer.tick(fps)
    
    screen.blit(Board.board ,(0,0))
    DrawPieces()
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            Board.run = False
            
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_z:
                print("Key A has been pressed")
                Board.Undo()
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_r:
                print("Key A has been pressed")
                Board.Redo()
        if event.type == pygame.MOUSEBUTTONDOWN :
             #print(pygame.mouse.get_pos[0]) 
            # (x,y) = 
             rowCol = Board.getRowColOnGivenPosition(pygame.mouse.get_pos()[0] , pygame.mouse.get_pos()[1] )
             piece = Board.getPieceOnGivenSquare(rowCol[0] , rowCol[1])
             
             if piece is None :                
                targetPiece = Board.selectedPiece 
                if targetPiece :          
                     gi = copy.deepcopy(targetPiece.MovementSelection())
                     if rowCol in gi :
                           targetPiece.Move(rowCol)   
                           Board.saveLog(targetPiece , targetPiece.FileRank(rowCol) ) 
                                  
                                          
             elif not piece.selected and Board.turn == piece.color :   
                Board.selectPiece(piece)
                
             elif not piece.selected and Board.turn != piece.color : 
                  targetPiece = Board.selectedPiece                      
                  if targetPiece :
                      
                      targetPiece.KillOpponent(piece)   
                      
             else : 
                piece.selected = False
                Board.selectedPiece = None
    #king_B.check = king_B.Check() 
    #king_W.check = king_W.Check() 
    Counter()
    
    #king_W.Checkmate() 
    #king_B.Checkmate() 
    pygame.display.flip()
    #print(mouse.get_position() )
       
pygame.quit()



