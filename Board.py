import copy
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
    
    whiteKingsideCastle = True
    blackKingsideCastle = True
    
    whiteQueensideCastle = True
    blackQueensideCastle = True
    rookBL = None
    rookBR = None
    rookWL = None
    rookWR = None 
    undo = Stack()
    redo = Stack()
    def __init__(self) :
        
        pass
    
    def saveLog(piece ,destination , captured = False  ,lastFR = []):
        
        color = Board.Check()
        if color != None and color != piece.color :
            check = True 
        else:
            check = False 
            
        checkmateCol = Board.CheckMate()
        
        print(checkmateCol)
        if checkmateCol != None and checkmateCol != piece.color :
           checkmate = True    
        else :
           checkmate = False 
        print(checkmate)
        if piece.tag != "pawn" :
            
            if piece.tag == "king":
                print("hi")
                print(piece.canQcastle)
                print(destination )
            if piece.tag == "king" and destination == Board.FileRank(piece.castleHousesQ[1]) and piece.canQcastle :
                 Board.log.append("O-O-O")
                 piece.canQcastle = False
            elif piece.tag == "king" and destination == Board.FileRank(piece.castleHousesK[1]) and piece.canKcastle  :
                 Board.log.append("O-O")
                 piece.canKcastle = False
                
            elif not captured and not check and not checkmate :
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
        
        #Board.pieces.remove(piece) 
        for i in range(len(Board.pieces)) :
            
            if Board.pieces[i] == piece :
                print("hi")
                Board.pieces.pop(i)
                break
             
        piece.isDead = True
        piece.sprite = pygame.transform.scale(piece.sprite , (30,30) )
          
            

    def FileRank(rowCol) :
            row = rowCol[0]
            col = rowCol[1]
            if row<9 and row>0 and col < 9 and col >0:
                if row == 1 :
                    rank = 8
                elif row ==2 :
                    rank = 7
                elif row ==3 :
                    rank = 6
                elif row ==4 :
                    rank = 5
                elif row ==5 :
                    rank = 4
                elif row ==6 :
                    rank = 3
                elif row ==7 :
                    rank = 2
                elif row ==8 :
                    rank = 1
            

                if col == 1 :
                    file = "a"
                elif col ==2 :
                    file = "b"
                elif col ==3 :
                    file = "c"
                elif col ==4 :
                    file = "d"
                elif col ==5 :
                    file = "e"
                elif col ==6 :
                    file = "f"
                elif col ==7 :
                    file = "g"
                elif col ==8 :
                    file = "h"
        
                return file + str(rank)
            
    def Check():
        
        if Board.king[0].color == "white" :
                kingW =  Board.king[0]
                kingB = Board.king[1]
        else :
                kingB =  Board.king[0]
                kingW = Board.king[1] 
                
        for piece in Board.pieces : 
            if not piece.isDead :
                if piece.color == "black" :
                    tempMoves = copy.deepcopy(piece.MovementSelection(ignoreCheck = True) )
          
                    for tempMove2 in tempMoves :
                        if tempMove2 == [kingW.row , kingW.column] :
                            #print("white check")
                            kingW.check = True
                            return "white"
                    kingW.check = False
                   
                elif piece.color == "white" : 
                
                    tempMoves2 = copy.deepcopy(piece.MovementSelection(ignoreCheck = True) )
                    for tempMove in tempMoves2 :
                        if tempMove == [kingB.row , kingB.column] :
                            #print("black check")
                            kingB.check = True
                            return "black" 
                    
                    kingB.check = False
                    

    def CheckMate() :
        
        if Board.Check() == "white" and Board.turn == "white" :
            
            moves = []
            for piece in Board.pieces :
                if piece.color == "white" :
                   moves += piece.MovementSelection()
            
            if moves == [] :
                print("Black Won")
                #Board.run = False
                return "white"
        elif Board.Check() == "black" and Board.turn == "black" :
            moves = []
            for piece in Board.pieces :
                if piece.color == "black" :
                   moves += piece.MovementSelection()
            if moves == []:
                print("White Won")
                #Board.run = False
                return "black"