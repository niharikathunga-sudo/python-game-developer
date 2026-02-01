import pygame
pygame.init()

screen=pygame.display.set_mode((200,200))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    if event.type==pygame.MOUSEBUTTONDOWN:
            image=pygame.image.load("onbulb.jpg")
            screen.blit(image,(0,0))
            pygame.display.update()
    elif event.type==pygame.MOUSEBUTTONUP:
         image=pygame.image.load("offbulb.jpg")
         screen.blit(image,(0,0))
         pygame.display.update()
            