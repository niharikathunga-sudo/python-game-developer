import pygame, random
pygame.init()
screen=pygame.display.set_mode((864,850))
clock=pygame.time.Clock()
pygame.display.set_caption("WELCOME TO THE FLAPPY BIRD GAME, HOW FAR CAN YOU GO..?!")

bg=pygame.image.load("bg1.png")
ground=pygame.image.load("groundbg2.png")
button=pygame.image.load("restartbutton.png")
flying=False
gameover=False

class birds(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.counter=0
        self.images=[]
        self.index=0
        for i in range(1,4):
            img=pygame.image.load(f"bird{i}.png")
            self.images.append(img)
        self.image=self.images[self.index]
        self.rect=self.image.get_rect()
        self.rect.center=[x,y]
        self.velocity=0
        self.click=False

    def update(self):
        if flying==True:
            self.velocity+=0.5
            if self.velocity>8:
                self.velocity==8
            if self.rect.bottom<682:
                self.rect.y+=self.velocity
        if gameover==False:
            if pygame.mouse.get_pressed()[0]==1:
                self.velocity=-8
            self.counter+=1
            if self.counter>5:
                self.counter=0
                self.index+=1
                if self.index>=3:
                    self.index=0
                self.image=self.images[self.index]
groundscroll=0
birdgroup=pygame.sprite.Group()
angrybird=birds(50,450)
birdgroup.add(angrybird)

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN and flying==False and gameover==False:
            flying=True
    
    screen.blit(bg,(0,0))
    birdgroup.draw(screen)
    birdgroup.update()
    screen.blit(ground,(groundscroll,682))
    groundscroll-=4

    if groundscroll<-36:
        groundscroll=0

    pygame.display.update()