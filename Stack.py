class Stack :
    def __init__ (self) :
        self.stackArray = []
        
    
    def Push(self ,data):
        self.stackArray.append(data)  
        
    def Pop(self) :
       if not self.IsEmpty() :
           return self.stackArray.pop()
       else :
          
           print("Stack Is Empty")
           return ""
   
    def IsEmpty(self) :
        if len(self.stackArray) == 0 :
            return True
        else :
            return False 
        
