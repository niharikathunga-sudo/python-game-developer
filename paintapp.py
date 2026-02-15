import pygame,random
pygame.init()
screen=pygame.display.set_mode((1000,500))
pygame.display.set_caption("Paint App!!")
colors=["red","orange","yellow","green","blue","purple","pink","black","brown"]
color="blue"
screen.fill("white")

lastpos=None
drawing=False

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        
        if event.type==pygame.MOUSEBUTTONDOWN:
            drawing=True
            lastpos=event.pos
            pygame.display.update()
        
        elif event.type==pygame.MOUSEBUTTONUP:
            drawing=False
            pygame.display.update()

        elif event.type==pygame.MOUSEMOTION:
            if drawing==True:
                pos=event.pos
                pygame.draw.line(screen,color,lastpos,pos)
                lastpos=pos
                pygame.display.update()
        
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_1:
                colorindex=colors.index(color)
                color=colors[(colorindex+1)%len(colors)]
                pygame.display.update()


