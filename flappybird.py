import pygame, random
pygame.init()
screen=pygame.display.set_mode((864,850))
pygame.display.set_caption("WELCOME TO THE FLAPPY BIRD GAME, HOW FAR CAN YOU GO..?!")

bg=pygame.image.load("bg1.png")
ground=pygame.image.load("groundbg2.png")
button=pygame.image.load("restartbutton.png")
flying=False
gameover=False

class birds(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        self.index=0
        for i in range(1,4):
            img=pygame.image.load(f"bird{i}.png")
            self.images.append(img)
        self.image=self.images[self.index]
        self.rect=self.image.get_rect()
        self.rect.center=[x,y]
        self.velocity=0

    def update(self):
        pass

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    
    screen.blit(bg,(0,0))
    screen.blit(ground,(0,682))

    pygame.display.update()