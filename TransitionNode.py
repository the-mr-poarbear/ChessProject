class TransitionNode:
    
    def __init__( self , turn , movedPiece ,startingPoint , destination , firstMove = None , isDead = False , captured = None , castleQ = None , castleK = None , secondMove = None) :
        self.turn = turn
        self.movedPiece = movedPiece
        self.destination = destination
        self.firstMove = firstMove
        self.startingPoint = startingPoint
        self.isDead = isDead
        self.captured = captured
        self.castleQ = castleQ
        self.castleK = castleK
        self.secondMove = secondMove



