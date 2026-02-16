import pygame,random
pygame.init()
screen=pygame.display.set_mode((640,500))
font=pygame.font.SysFont("pacifico",50)

subsurf=pygame.image.load("subway surfers.png")
temprun=pygame.image.load("temple run.png")
candcrush=pygame.image.load("candy crush.jpg")
ludo=pygame.image.load("ludo.png")

screen.blit(subsurf,(30,50))
screen.blit(temprun,(30,150))
screen.blit(candcrush,(30,250))
screen.blit(ludo,(30,350))
fonttext1=font.render("Subway Surfers",True,"white")
fonttext2=font.render("Temple Run",True,"white")
fonttext3=font.render("Candy Crush",True,"white")
fonttext4=font.render("Ludo",True,"white")

screen.blit(fonttext1,(350,150))
screen.blit(fonttext2,(350,350))
screen.blit(fonttext3,(350,250))
screen.blit(fonttext4,(350,50))


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

    event=pygame.event.poll()
    if event.type==pygame.MOUSEBUTTONDOWN:
        pos=pygame.mouse.get_pos()
        pygame.draw.circle(screen,"blue",pos,5,0)
        pygame.display.update()

    elif event.type==pygame.MOUSEBUTTONUP:
        pos2=pygame.mouse.get_pos()
        pygame.draw.circle(screen,"light pink",pos2,5,0)
        pygame.draw.line(screen,"light pink",pos,pos2,5)
        pygame.display.update()

    pygame.display.update()
