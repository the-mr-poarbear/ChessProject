# Chess Data Structure Project
## Dr.Hassanpoor's class
starting day 2023/11/29


def MovementSelection(self , draw = True , ignoreCheck = False) :
            self.validMoves = [] 
            for pattern in self.patterns:
                    tempRow = self.row
                    tempCol =  self.column
                    tempRow += pattern[0]  
                    tempCol += pattern[1]     
                         
                    if tempRow <= 0 or tempCol <=0 or tempRow > 8 or tempCol >8 :
                        pass 
                    elif Board.getPieceOnGivenSquare(tempRow , tempCol) is None :  
                        self.validMoves.append([tempRow,tempCol])
                            
                    elif Board.getPieceOnGivenSquare(tempRow , tempCol).color != self.color :
                            
                        self.validMoves.append([tempRow,tempCol])  
                    else :
                        pass
                    
            if not ignoreCheck :       
                    self.CheckValidMoves(self.validMoves) 
         
            return self.validMoves   