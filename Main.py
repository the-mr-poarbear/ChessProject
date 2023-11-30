import pygame 

class Main:
    
    #initialize 
    pygame.init()
    width = 1000 
    height = 700 
    
    screen = pygame.display.set_mode([width , height])
    pygame.display.set_caption("Data Structure Project Chess Game")
    font = pygame.font.Font("freesansbold.ttf" , 20)
    bigFont = pygame.font.Font("freesansbold.ttf" , 50)
    timer = pygame.time.Clock()
    fps = 60 
    
    run = True 
    
    #run loop 
    while run : 
        timer.tick(fps)
        screen.fill("dark gray")
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                run = False
                
        pygame.display.flip()
        
    pygame.quit()



