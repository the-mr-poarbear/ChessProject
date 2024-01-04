import copy
import time
import pygame





from Stack import Stack

class Board:
    
    logTxt = ""
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
    undoLog = Stack()
    redoLog = Stack()
    def __init__(self) :
        
        pass
    
    def saveLog(piece ,destination , captured = False  ,lastFR = []):
        
        while not Board.redoLog.IsEmpty():
            Board.redoLog.Pop()   
        
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
        Board.undoLog.Push(Board.log[len(Board.log)-1]) 
        Board.PrintLog() 
        
            
    def PrintLog() :
        Board.logTxt = ""
        num = 0
        for i in range (len(Board.log)) :
            if i%2 == 0 :
                num +=1   
                print(" " + str(num) + ".")
                Board.logTxt += (" " + str(num) + ". ")
                
            print(Board.log[i])   
            Board.logTxt += ( Board.log[i] + ",")
    
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
                if piece.color =="white" :
                    Board.whiteSideDead.append(piece)
                else :
                     Board.blackSideDead.append(piece)
                break
             
        piece.isDead = True
        #piece.sprite = pygame.transform.scale(piece.sprite , (30,30) )
          
            

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
    
    def Undo() :
        if not Board.undo.IsEmpty() :

            node = Board.undo.Pop()
            node.movedPiece.row = node.startingPoint[0]
            node.movedPiece.column = node.startingPoint[1]
        
            if node.movedPiece.tag == "pawn"  :
                node.movedPiece.firstMove = node.firstMove
                
            elif node.movedPiece.tag == "rook" :
                node.movedPiece.firstMove = node.firstMove
                
                if node.firstMove :
                    rook = node.movedPiece
                    
                    for king in Board.king :
                       if rook.color == king.color and king.castle :
                           print("brr")
                           #king.castle = True           
                           if rook == Board.rookWL :
                               Board.whiteQueensideCastle = True
                           elif rook == Board.rookBL :
                               Board.blackQueensideCastle = True 
                               
                           elif rook == Board.rookWR : 
                               print("brrrrr")
                               Board.whiteKingsideCastle = True
                           elif rook == Board.rookBR :
                               Board.blackKingsideCastle = True  
                               

                        
                    
            elif node.movedPiece.tag == "king" :
                 
                 node.movedPiece.firstMove = node.firstMove 
                 
                 if node.castleQ :
                     #node.movedPiece.
                     if node.castleQ.color == "white" :                     
                         Board.rookWL.column -= 3
                         Board.rookWL.firstMove = True
                         Board.whiteQueensideCastle = True
                         if Board.rookWR.firstMove and [Board.rookWR.row , Board.rookWR.column] == [8 , 8] :
                            Board.whiteKingsideCastle = True   
                             
                         
                     else :                   
                         Board.rookBL.column -= 3
                         Board.rookBL.firstMove = True
                         Board.blackQueensideCastle = True
                         if Board.rookBR.firstMove and [Board.rookBR.row , Board.rookBR.column] == [1 , 8] :
                            Board.blackKingsideCastle = True  
                            
                     node.movedPiece.canQcastle = True
                     node.movedPiece.castle = True
                     
                 elif node.castleK :
                     if node.castleK.color == "white" :
                         print("all in")
                         Board.rookWR.column += 2
                         Board.rookWR.firstMove = True
                         Board.whiteKingsideCastle = True
                         if Board.rookWL.firstMove and [Board.rookWL.row , Board.rookWL.column] == [8 , 1] :
                            Board.whiteQueensideCastle = True  
                     else :
                         Board.rookBR.column += 2
                         Board.rookBR.firstMove = True
                         Board.blackKingsideCastle = True
                         if Board.rookBL.firstMove and [Board.rookBL.row , Board.rookBL.column] == [1 , 1] :
                            Board.blackQueensideCastle = True  
                         
                     node.movedPiece.canKcastle = True
                     node.movedPiece.castle = True
                     
            if node.captured != None :
                node.captured.isDead = False
                Board.pieces.append(node.captured)
                #node.captured.sprite = pygame.transform.scale(node.captured.sprite , (60,60))
            Board.redoLog.Push(Board.log.pop())
            print("hubji")
            print(Board.undoLog.IsEmpty())
            Board.redo.Push(node)
            Board.Check()
            Board.SwitchTurn()
            Board.PrintLog()
            #dont forget to return the dead and add it to Board.pieces otherwise theyl stay ghosty

    def Redo() :
        if not Board.redo.IsEmpty() :
            
            node = Board.redo.Pop()
            node.movedPiece.row = node.destination[0]
            node.movedPiece.column = node.destination[1]
        
            if node.movedPiece.tag == "pawn" :
                node.movedPiece.firstMove = False
                if node.movedPiece.secondMove and node.movedPiece.row == 5 or node.movedPiece.row == 4 :
                    left = Board.getPieceOnGivenSquare(node.movedPiece.row , node.movedPiece.column - 1)
                    right = Board.getPieceOnGivenSquare(node.movedPiece.row , node.movedPiece.column + 1) 
                    if left != None and left.tag == "pawn" and left.color != node.movedPiece.color :
                        node.movedPiece.enPassant = True
                    if right != None and right.tag == "pawn" and right.color != node.movedPiece.color :
                        node.movedPiece.enPassant = True
                        
            elif node.movedPiece.tag == "king" :

                 if node.castleQ :
                     if node.castleQ.color == "white" :
                         
                         Board.rookWL.column += 3
                     else :
                         Board.rookBL.column += 3
                 elif node.castleK :
                     if node.castleK.color == "white" :
                         
                         Board.rookWR.column -= 2
                     else :
                         Board.rookBR.column -= 2
            if node.captured != None :
                node.captured.isDead = True
                Board.pieces.remove(node.captured)
                #node.captured.sprite = pygame.transform.scale(node.captured.sprite , (60,60))
                #remember to add the dead in white or blackside graves
            Board.log.append(Board.redoLog.Pop())
            Board.undo.Push(node)
            Board.Check()
            Board.SwitchTurn()
            Board.PrintLog()
        
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
                Board.won = "black"
                return "white"
        elif Board.Check() == "black" and Board.turn == "black" :
            moves = []
            for piece in Board.pieces :
                if piece.color == "black" :
                   moves += piece.MovementSelection()
            if moves == []:
                print("White Won")
                Board.won = "white"
                #Board.run = False
                return "black"
            
    