from ast import List
import pygame

from Board import Board 
from Piece import Piece 


    
#initialize 

pygame.init()
width = 1000 
height = 700 
    

    
    
blackPieces = ["rook" , "knight" , "bishop" , "king" , "queen" , "bishop" , "knight" , "rook" ,
                "pawn" , "pawn" , "pawn" , "pawn" , "pawn" , "pawn" , "pawn" , "pawn"]
    
capturedBlackPieces = []
capturedWhitePieces = []
    
# state = 0 => white s turn no selection . 1 => white s turn , selection made .
# 2 => black s turn no selection . 3 => black s turn selection made 
state = 0 
    
   
    

#Board 
board = pygame.image.load("ChessProject\Board\APossant.png")
    

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
queen_B_img = pygame.transform.scale(queen_B_img , (80,80) )
    
bishop_B_img = pygame.image.load("ChessProject\Pieces\BlackPieces\BishopB.png")
bishop_B_img = pygame.transform.scale(bishop_B_img , (80,80) )
    
king_B_img = pygame.image.load("ChessProject\Pieces\BlackPieces\Kingb.png")
king_B_img = pygame.transform.scale(king_B_img , (80,80) )
    
knight_B_img = pygame.image.load("ChessProject\Pieces\BlackPieces\KnightB.png")
knight_B_img = pygame.transform.scale(knight_B_img , (80,80) )
    
pawn_B_img = pygame.image.load("ChessProject\Pieces\BlackPieces\PawnB.png")
pawn_B_img = pygame.transform.scale(pawn_B_img , (80,80) )
    
rook_B_img = pygame.image.load("ChessProject\Pieces\BlackPieces\RookB.png")
rook_B_img = pygame.transform.scale(rook_B_img , (80,80) )
    
    
      
queen_W = Piece("queen" , "white" , queen_W_img ,[8 , 5])
    
king_W = Piece("king" , "white" , king_W_img ,[8 , 4]) 
    
bishop_WL = Piece("bishop" , "white" , bishop_W_img ,[8 , 3])
bishop_WR = Piece("bishop" , "white" , bishop_W_img ,[8 , 6])
    
knight_WL = Piece("knight" , "white" , knight_W_img ,[8 , 2])
knight_WR = Piece("knight" , "white" , knight_W_img ,[8 , 7])
    
rook_WL = Piece("rook" , "white" , rook_W_img ,[8 , 1])
rook_WR = Piece("rook" , "white" , rook_W_img ,[8 , 8])
    
pawn_W = []
for i in range(8) :       
    pawn_W.append(Piece("pawn" , "white" , pawn_W_img ,[7 , i+1]))
    

whitePieces = [queen_W , bishop_WL , bishop_WR , king_W , knight_WR , knight_WL , pawn_W , rook_WL , rook_WR ]
    
#blackSprites = [queen_B , bishop_B , king_B , knight_B , pawn_B , rook_B]
    

screen = Board.screen
pygame.display.set_caption("Data Structure Project Chess Game")
font = pygame.font.Font("freesansbold.ttf" , 20)
bigFont = pygame.font.Font("freesansbold.ttf" , 50)
timer = pygame.time.Clock()
fps = 60  
    
    
run = True 
    
def DrawPieces():
        
    for piece in whitePieces : 
        if type(piece) != type(pawn_W) :
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
                
    #print(pygame.mouse.get_pos())       
    pygame.display.flip()
        
pygame.quit()



