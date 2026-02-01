#reporting and initialising pygame
import pygame
pygame.init()

#set dimensions of the screen
screen=pygame.display.set_mode((1000,500))


ball=pygame.draw.circle(screen,"red",(245,370),30)
speed=[1,1]
clock=pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    clock.tick(5020)
    screen.fill("black")
    ball=ball.move(speed)
    if ball.left<=0 or ball.right>=1000:
        speed[0]=-speed[0]
    if ball.top<=0 or ball.bottom>=500:
        speed[1]=-speed[1]
    pygame.draw.circle(screen,"red",center=ball.center,radius=30)   
    pygame.display.update()