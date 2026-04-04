import pygame, random
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("SPACE GETS INVADED... OR DOES IT?")

bot1=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("bot1.png"),(50,50)),90)
bot2=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("bot2.png"),(50,50)),270)
bot1rt=pygame.Rect(10,300,50,50)
bot2rt=pygame.Rect(700,300,50,50)
bg=pygame.image.load("spaceeeeeee.png")
bot1health=10
bot2health=10
font=pygame.font.SysFont("calligrapher",50)
winner=""
gameover=False
bot1bull=[]
bot2bull=[]

def draw():
    screen.blit(bg,(0,0))
    pygame.draw.rect(screen,"black",pygame.Rect(400,0,25,600))
    screen.blit(bot1,(bot1rt.x,bot1rt.y))
    screen.blit(bot2,(bot2rt.x,bot2rt.y))
    fonttext1=font.render(f"Health:{bot1health}",True,"White")
    fonttext2=font.render(f"Health:{bot2health}",True,"White")
    gameovertext=font.render(f"GAMEOVER!.. The winner is...{winner}!!",True,"White")
    screen.blit(fonttext1,(10,30))
    screen.blit(fonttext2,(600,30))
    if gameover:
        screen.blit(bg,(0,0))
        screen.blit(gameovertext,(50,67))
    for i in bot1bull:
        pygame.draw.rect(screen,"yellow",i)

    for i in bot2bull:
        pygame.draw.rect(screen,"pink",i)


def yellowattack(keys):
    if keys[pygame.K_a] and bot1rt.x>0:
        bot1rt.x-=1
    if keys[pygame.K_s] and bot1rt.y<550:
        bot1rt.y+=1
    if keys[pygame.K_d] and bot1rt.x<360:
        bot1rt.x+=1
    if keys[pygame.K_w] and bot1rt.y>0:
        bot1rt.y-=1


def pinkattack(keys):
    if keys[pygame.K_LEFT] and bot2rt.x>425:
        bot2rt.x-=1
    if keys[pygame.K_DOWN] and bot2rt.y<550:
        bot2rt.y+=1
    if keys[pygame.K_RIGHT] and bot2rt.x<750:
        bot2rt.x+=1
    if keys[pygame.K_UP] and bot2rt.y>0:
        bot2rt.y-=1





while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    draw()
    keys=pygame.key.get_pressed()
    yellowattack(keys)
    pinkattack(keys)
    pygame.display.update()
