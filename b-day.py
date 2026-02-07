import pygame
import time
pygame.init()
screen=pygame.display.set_mode((600,600))

pygame.display.set_caption("Birthday Wishes")
image=pygame.image.load("bdaybanner.jpg")

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    
    image=pygame.image.load("bdaybanner.jpg")
    font=pygame.font.SysFont("calligrapher",50)
    fonttext1=font.render("Happy birthday",True,"black")
    fonttext2=font.render("HUMAN!!:)",True,"black")
    screen.blit(image,(0,0))
    screen.blit(fonttext1,(190,250))
    screen.blit(fonttext2,(210,300))
    pygame.display.update()
    time.sleep(3)

    image=pygame.image.load("cake.jpg")
    font=pygame.font.SysFont("calligrapher",50)
    fonttext1=font.render("YOUR CAKE!!",True,"black")
    screen.blit(image,(0,0))
    screen.blit(fonttext1,(190,250))
    pygame.display.update()
    time.sleep(3)

    image=pygame.image.load("explodingpresent.jpg")
    font=pygame.font.SysFont("calligrapher",45)
    fonttext1=font.render("HOPE YOU HAVE A GOOD DAY",True,"black")
    screen.blit(image,(0,0))
    screen.blit(fonttext1,(0,0))
    pygame.display.update()
    time.sleep(3)
