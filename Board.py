import time
import pygame



from Stack import Stack

class Board:
    won = ""
    startingPoint = [560,140]
    sideOfTheSquare = 100
    board = pygame.image.load("ChessProject\Board\APossant.png")
    scaleRate = 0.6
    board = pygame.transform.scale(board , (board.get_width()*scaleRate , board.get_height()*scaleRate)) 
    startingPoint[0] =  startingPoint[0]*scaleRate
    startingPoint[1] =  startingPoint[1]*scaleRate
    sideOfTheSquare = sideOfTheSquare*scaleRate
    run = True 
    screen = pygame.display.set_mode([board.get_width() , board.get_height()])
    pieces = []
    selectedPiece = None
    king = []
    turn = "white"
    # num , piece , captured sign ,destination , checkOrCheckmate 
    log = []
    timer = time.time()
    
    whiteSideDead = []
    whiteSideDeadPos = []
    whiteSideDeadGrave = 50

    blackSideDead = []
    undo = Stack()
    redo = Stack()
    def __init__(self) :
        
        pass
    
    def saveLog(piece ,destination , kingCheck , captured = False   , checkmate = False ,lastFR = []):
        
        color = kingCheck
        if color != None and color != piece.color :
            check = True 
        else:
            check = False 
        
        if piece.tag != "pawn" :
            if not captured and not check and not checkmate :
                 Board.log.append(piece.shorten + destination ) 
                 
            elif captured and not check and not checkmate :
                 Board.log.append(piece.shorten + "x" + destination ) 
                 
            elif not captured and check and not checkmate :
                 Board.log.append(piece.shorten + destination + "+" )
                 
            elif captured and check and not checkmate :
                 Board.log.append(piece.shorten + "x" + destination + "+" )
                 
            elif not captured and checkmate :
                 Board.log.append(piece.shorten + destination + "#" )
                 if Board.won == "white" :
                    Board.log.append("1-0") 
                 else :
                    Board.log.append("0-1") 
            elif captured and checkmate :
                 Board.log.append(piece.shorten + "x" + destination + "#" )
                 if Board.won == "white" :
                    Board.log.append("1-0") 
                 else :
                    Board.log.append("0-1") 
        else :
            if not captured and not check and not checkmate :
                    #print("1")    
                    Board.log.append( destination ) 
                 
            elif captured and not check and not checkmate :
                    #print("2")     
                    Board.log.append(lastFR[0] + "x" + destination ) 
                 
            elif not captured and check and not checkmate :
                    #print("3")     
                    Board.log.append( destination + "+" )
                 
            elif captured and check and not checkmate :
                    #print("4")     
                    Board.log.append(lastFR[0] + "x" + destination + "+" )
                 
            elif not captured and checkmate :
                    #print("5")     
                    Board.log.append( destination + "#" )
                    if Board.won == "white" :
                        Board.log.append("1-0") 
                    else :
                        Board.log.append("0-1") 
            elif  captured and checkmate :
                    #print("6")     
                    Board.log.append( piece.FileRank([piece.row , piece.column])[0] + "x" + destination + "#" )
                    
                    if Board.won == "white" :
                        Board.log.append("1-0") 
                    else :
                        Board.log.append("0-1") 
          
        Board.PrintLog() 
        
            
    def PrintLog() :
        num = 0
        for i in range (len(Board.log)) :
            if i%2 == 0 :
                num +=1
                print(str(num) + ". ")
                
            print(Board.log[i])   
            
                          
    def Undo():
        pass
    
    def getPieceOnGivenSquare( row , column) :     
        #file is a to h and rank is 1 to 8
        for piece in Board.pieces :
            
            
            #print(piece.row , row)
            #print(piece.column , column)
            if piece.row == row and piece.column == column :
                return piece
        return None  
    def getPoistionOnGivenSquare(row , column ) :
        positionX = Board.startingPoint[0] + column * Board.sideOfTheSquare - Board.sideOfTheSquare
        positionY = Board.startingPoint[1] + row * Board.sideOfTheSquare - 16*Board.sideOfTheSquare/16
        return [positionX , positionY]
        

    def getRowColOnGivenPosition(positionX , positionY) :
        row = (positionY - Board.startingPoint[1]) //  Board.sideOfTheSquare + 1
        col = (positionX - Board.startingPoint[0]) //  Board.sideOfTheSquare + 1
        
        return [int(row),int(col)]

    def selectPiece(piece) :
          #print("notagn")
          for tPiece in Board.pieces :
                tPiece.selected = False  
          piece.selected = True 
          Board.selectedPiece = piece   
                
    def SwitchTurn():
        Board.timer = time.time()
        if Board.turn == "white" :
            #print("1")
            Board.turn = "black"
        else :
            #print("2")
            Board.turn = "white"
        Board.selectedPiece = None
        #print("switched")
    
    def CheckColor(kingWch , kingBch) :
        if kingWch :
             return "white"
        elif kingBch :
            return "black" 
    
    def Remove(piece ) :
        piece.isDead = True
        piece.sprite = pygame.transform.scale(piece.sprite , (30,30) )
        Board.pieces.remove(piece) 
        if piece.color == "white" :
            Board.whiteSideDead.append(piece) 
        else :
            Board.blackSideDead.append(piece)  