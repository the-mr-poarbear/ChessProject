from ast import List
import pygame

from Board import Board 
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
queen_W = Piece("queen" , "white" , queen_W_img ,[8 , 5] , True)
    
king_W = Piece("king" , "white" , king_W_img ,[8 , 4]) 
    
bishop_WL = Piece("bishop" , "white" , bishop_W_img ,[8 , 3] , True)
bishop_WR = Piece("bishop" , "white" , bishop_W_img ,[8 , 6] , True)
    
knight_WL = Piece("knight" , "white" , knight_W_img ,[8 , 2])
knight_WR = Piece("knight" , "white" , knight_W_img ,[8 , 7])
    
rook_WL = Piece("rook" , "white" , rook_W_img ,[8 , 1] , True)
rook_WR = Piece("rook" , "white" , rook_W_img ,[8 , 8] , True)
    
pawn_W = []
for i in range(8) :       
    pawn_W.append(Piece("pawn" , "white" , pawn_W_img ,[7 , i+1]))
    

whitePieces = [queen_W , bishop_WL , bishop_WR , king_W , knight_WR , knight_WL , pawn_W , rook_WL , rook_WR ]
  
#black pieces initializeation   
queen_B = Piece("queen" , "white" , queen_B_img ,[1 , 5])
    
king_B = Piece("king" , "white" , king_B_img ,[1 , 4]) 
    
bishop_BL = Piece("bishop" , "white" , bishop_B_img ,[1 , 3])
bishop_BR = Piece("bishop" , "white" , bishop_B_img ,[1 , 6])
    
knight_BL = Piece("knight" , "white" , knight_B_img ,[1 , 2])
knight_BR = Piece("knight" , "white" , knight_B_img ,[1 , 7])
    
rook_BL = Piece("rook" , "white" , rook_B_img ,[1 , 1])
rook_BR = Piece("rook" , "white" , rook_B_img ,[1 , 8])
    
pawn_B = []
for i in range(8) :       
    pawn_B.append(Piece("pawn" , "white" , pawn_B_img ,[2 , i+1]))
    

blackPieces = [queen_B , bishop_BL , bishop_BR , king_B , knight_BR , knight_BL , pawn_B , rook_BL , rook_BR ]
  
    

screen = Board.screen
pygame.display.set_caption("Data Structure Project Chess Game")
font = pygame.font.Font("freesansbold.ttf" , 20)
bigFont = pygame.font.Font("freesansbold.ttf" , 50)
timer = pygame.time.Clock()
fps = 60  
    
    
run = True 

Board.pieces = [queen_B , bishop_BL , bishop_BR , king_B , knight_BR , knight_BL , pawn_B , rook_BL , rook_BR ,
                queen_W , bishop_WL , bishop_WR , king_W , knight_WR , knight_WL , pawn_W , rook_WL , rook_WR ]
def DrawPieces():
        
    for piece in whitePieces : 
        if type(piece) != type(pawn_W) :
            piece.Draw()
        else :
            for i in piece :
                i.Draw()
                pass
                
    for piece in blackPieces : 
        if type(piece) != type(pawn_B) :
            piece.Draw()
        else :
            for i in piece :
                i.Draw()
#run loop 
while run : 
    timer.tick(fps)
        
    screen.blit(Board.board ,(0,0))
    DrawPieces()
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN :
             #print(pygame.mouse.get_pos[0]) 
            # (x,y) = 
             rowCol = Board.getRowColOnGivenPosition(pygame.mouse.get_pos()[0] , pygame.mouse.get_pos()[1] )
             print(rowCol)
             piece = Board.getPieceOnGivenSquare(rowCol[0] , rowCol[1])
             while(True) :
                 print("hi")
                 piece.MovementSelection()
                 pygame.display.flip()
    #print(pygame.mouse.get_pos())       
    pygame.display.flip()
        
pygame.quit()



