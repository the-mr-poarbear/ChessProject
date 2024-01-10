import copy
import time
import pygame
from Stack import Stack

class Board:
    pot = False
    logTxt = ""
    won = ""
    i = 0
    startingPoint = [554,138]
    sideOfTheSquare = 101.87
    board = pygame.image.load("ChessProject\Board\APossant5.png")
    pop = False
    scaleRate = 0.6
    #board = pygame.transform.scale(board , (board.get_width()*scaleRate , board.get_height()*scaleRate)) 
    startingPoint[0] =  startingPoint[0]*scaleRate
    startingPoint[1] =  startingPoint[1]*scaleRate
    sideOfTheSquare = sideOfTheSquare*scaleRate
    run = True 
    screen = pygame.display.set_mode([board.get_width() , board.get_height()])
    pieces = []
    selectedPiece = None
    king = []
    turn = "white"
    pawnPro = None
    # num , piece , captured sign ,destination , checkOrCheckmate 
    log = []
    timer = time.time()
    
    startingPointDeadW = [90 , 1000]
    startingPointDeadB = [90 , 0]
    whiteSideDead = []
    sideDeadGrave = 80
    blackSideDead = []
    
    sideDeadGrave *= scaleRate
    startingPointDeadW [0] *= scaleRate
    startingPointDeadW [1] *= scaleRate
    startingPointDeadB [0] *= scaleRate
    startingPointDeadB [1] *= scaleRate
    
    
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
            
        print(Board.Check() , "check4")
        color = None
        temp = Board.Check()
        if temp :
            color = Board.Check()[0]
        
            
        print("color" , color)
        
        print(color , "color")
        if color != None and color != piece.color :
            check = True 
        else:
            check = False 
        print("check" , check) 
        print("color" , color)
        
        if not Board.pot :   
            checkmateCol = Board.CheckMate()
            if checkmateCol != None and checkmateCol != piece.color :
               checkmate = True    
            else :
               checkmate = False 
            print(checkmate)
            
        print("pottt" , Board.pot)
        if piece.tag != "pawn" :
            
            if Board.pot :
                 Board.log.append("1/2 - 1/2")  
                 
            elif piece.tag == "king" and destination == Board.FileRank(piece.castleHousesQ[1]) and piece.canQcastle :
                 
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
                 if Board.won == "white" :
                    Board.log.append(piece.shorten + destination + "# 1-0") 
                 else :
                    Board.log.append(piece.shorten + destination + "# 0-1") 
                    
            elif captured and checkmate :
                 if Board.won == "white" :
                    Board.log.append(piece.shorten + "x" + destination + "# 1-0") 
                 else :
                    Board.log.append(piece.shorten +"x"+ destination + "# 0-1") 
                    
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
        num = 1
        j = -1
        for i in range (len(Board.log)) :
                
            if not (Board.log[i] and (Board.log[i][0] == "U" or ( Board.log[i][0] == "R" and len(Board.log[i]) >= 4 and Board.log[i][3] == "o"))) :
                
                j+=1
                
                
                num += 1/2
                if j%2 == 0 :
                    print( str(int(num)) + ".")
                    Board.logTxt += (" " + str(int(num)) + ". ")
                    Board.logTxt += ( Board.log[i] )
                else :                
                    Board.logTxt += (" " +  Board.log[i] + ",")
                    
                   
                    
            else :
                if Board.log[i] and Board.log[i][0] == "U" :
                    j-=1
                    num-= 1/2
                else :
                    j+=1
                    num+=1/2
                    
                Board.logTxt += (", " +  Board.log[i] + ",")
                
    
    def getPieceOnGivenSquare( row , column) :     

        for piece in Board.pieces :            
            #print(piece.row , row)
            #print(piece.column , column)
            if piece.row == row and piece.column == column :
                return piece
        return None 
    
    def getPoistionOnGivenSquare(row , column ) :
        positionX = Board.startingPoint[0] + column * Board.sideOfTheSquare - Board.sideOfTheSquare
        positionY = Board.startingPoint[1] + row * Board.sideOfTheSquare - Board.sideOfTheSquare
        return [positionX , positionY]
        
    def getPositionOnGivenSquareForDead(rowCol , color) :
        if color == "white" :

            positionX = Board.startingPointDeadW[0] + rowCol[1] * Board.sideDeadGrave 
            positionY = Board.startingPointDeadW[1] - rowCol[0] * Board.sideDeadGrave 
            return [positionX , positionY]
        else :
      
            positionX = Board.startingPointDeadB[0] + rowCol[1] * Board.sideDeadGrave 
            positionY = Board.startingPointDeadB[1] + rowCol[0] * Board.sideDeadGrave 
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
                if piece.color == "white" :
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
            Board.pot = node.pot
            Board.won = None
            if node.movedPiece.tag == "pawn"  :
                node.movedPiece.firstMove = node.firstMove
                node.movedPiece.secondMove = node.secondMove
                pawn = node.movedPiece 
                
                left = Board.getPieceOnGivenSquare(node.movedPiece.row , node.movedPiece.column - 1)
                right = Board.getPieceOnGivenSquare(node.movedPiece.row , node.movedPiece.column + 1) 
                if left != None and left.tag == "pawn" and left.color != pawn.color and left.secondMove and (left.row == 5 or left.row == 4):
                    left.enPassant = True
                if right != None and right.tag == "pawn" and right.color != pawn.color and right.secondMove  and (right.row == 5 or right.row == 4) :
                    right.enPassant = True
                    
                if node.promotion :
                    Board.pieces.remove(node.promotion)
                    Board.pieces.append(node.movedPiece)
                    
                
                
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
                 node.movedPiece.castle = node.firstMove  #ya its right!.. frist move
                 if node.firstMove :
                     if node.movedPiece.color == "white" :
                         if Board.rookWR.firstMove and [Board.rookWR.row , Board.rookWR.column] == [8 , 8] :
                            Board.whiteKingsideCastle = True  
                         if Board.rookWL.firstMove and [Board.rookWL.row , Board.rookWL.column] == [8 , 1] :
                            Board.whiteQueensideCastle = True  
                     else :
                         
                         if Board.rookBR.firstMove and [Board.rookBR.row , Board.rookBR.column] == [1 , 8] :
                            Board.blackKingsideCastle = True  
                         if Board.rookBL.firstMove and [Board.rookBL.row , Board.rookBL.column] == [1 , 1] :
                            Board.blackQueensideCastle = True  
                         
                       

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
                if node.captured.color == "white" :
                    Board.whiteSideDead.remove(node.captured)
                else :
                    Board.blackSideDead.remove(node.captured)
                    
                Board.pieces.append(node.captured)
                #node.captured.sprite = pygame.transform.scale(node.captured.sprite , (60,60))
            

                
            tempLog = Board.undoLog.Pop()
            Board.redoLog.Push(tempLog)
            Board.log.append("Undo " +tempLog)
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
            Board.won = node.won
            Board.pot = node.pot

            if node.movedPiece.tag == "pawn" :
                node.movedPiece.firstMove = False
                if node.movedPiece.secondMove and node.movedPiece.row == 5 or node.movedPiece.row == 4 :
                    left = Board.getPieceOnGivenSquare(node.movedPiece.row , node.movedPiece.column - 1)
                    right = Board.getPieceOnGivenSquare(node.movedPiece.row , node.movedPiece.column + 1) 
                    if left != None and left.tag == "pawn" and left.color != node.movedPiece.color :
                        node.movedPiece.enPassant = True
                    if right != None and right.tag == "pawn" and right.color != node.movedPiece.color :
                        node.movedPiece.enPassant = True
                    print("node pro" , node.promotion) 
            if node.promotion :
                Board.pieces.remove(node.movedPiece) 
                Board.pieces.append(node.promotion)
                        
                        
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
                
                if node.captured.color == "white" :
                    Board.whiteSideDead.append(node.captured)
                else :
                    Board.blackSideDead.append(node.captured)
                
                #node.captured.sprite = pygame.transform.scale(node.captured.sprite , (60,60))
                #remember to add the dead in white or blackside graves
            
           # Board.log.append(Board.redoLog.Pop())
            
            tempLog = Board.redoLog.Pop()
            Board.undoLog.Push(tempLog)
            Board.log.append("Redo " + tempLog)
            
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
        result = [] 
        kingW.check = False
        kingB.check = False
        for piece in Board.pieces : 
            if not piece.isDead :
                
                if piece.color == "black" :
                    tempMoves = copy.deepcopy(piece.MovementSelection(ignoreCheck = True) )
                    
                    for tempMove2 in tempMoves :
                        if tempMove2 == [kingW.row , kingW.column] :
                            #print("white check")
                            kingW.check = True
                            result.append("white")
                            
                    
                    
                elif piece.color == "white" : 
                    
                    tempMoves2 = copy.deepcopy(piece.MovementSelection(ignoreCheck = True) )
                    for tempMove in tempMoves2 :
                        if tempMove == [kingB.row , kingB.column] :
                            #print("black check")
                            kingB.check = True
                            result.append("black") 
                    
                    
                    
        return result

    def CheckMate() :
        
        if Board.king[0].color == "white" :
                kingW =  Board.king[0]
                kingB = Board.king[1]
        else :
                kingB =  Board.king[0]
                kingW = Board.king[1] 
  
        if "white"  in Board.Check() and Board.turn == "white" :
            
            moves = []
            for piece in Board.pieces :
                if piece.color == "white" :
                   moves += piece.MovementSelection()
            
            if moves == [] :
                print("Black Won")
                               
                Board.won = "black"
                node = Board.undo.Pop()
                node.won = "black"
                Board.undo.Push(node)
                
                return "white"
            else :
                Board.won = None
            
        elif "black" in Board.Check() and Board.turn == "black" :
            moves = []
            for piece in Board.pieces :
                if piece.color == "black" :
                   print(piece.tag)
                   moves += piece.MovementSelection()
                   
            print("Kmoves" , kingB.MovementSelection())      
            if moves == []:
                print("White Won") 
                
                Board.won = "white"
                node = Board.undo.Pop()
                node.won = "white"
                Board.undo.Push(node)



                return "black"
            else :
                Board.won = None

        elif Board.turn == "black" :
            movesB = []
            for piece in Board.pieces :
                if piece.color == "black" :
                    movesB += piece.MovementSelection()
                   
                    if movesB != [] :
                        #Board.check = False
                        Board.pot = False
                        return
                   
            Board.pot = True          
            Board.saveLog(Board.king[0] , [5 ,4])
            print("Pot" , Board.pot)     
           
        else :
               movesW = []   
               for piece in Board.pieces :
                    if piece.color == "white" :
                        movesW += piece.MovementSelection()
                        if movesW != [] :
                            Board.pot = False
                            return
                        
 
               Board.pot = True
               Board.saveLog(Board.king[0] , [5 ,4])
               print("Pot" , Board.pot)
                     
        print("-1")
            
            
            
    