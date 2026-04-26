import pygame, random
pygame.init()
screen=pygame.display.set_mode((864,850))
clock=pygame.time.Clock()
pygame.display.set_caption("WELCOME TO THE FLAPPY BIRD GAME, HOW FAR CAN YOU GO..?!")

bg=pygame.image.load("bg1.png")
ground=pygame.image.load("groundbg2.png")
button=pygame.image.load("restartbutton.png")
pipefreq=1500
lastpipe=pygame.time.get_ticks()-pipefreq
flying=False
gameover=False
font=pygame.font.SysFont("calligrapher",50)
score=0

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

class pipes(pygame.sprite.Sprite):
    def __init__(self,x,y,position):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("pipes.png")
        self.rect=self.image.get_rect()
        if position==1:
            self.image=pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft=[x,y-75]
        elif position==-1:
            self.rect.topleft=[x,y+75]

    def update(self):
        self.rect.x-=4
        if self.rect.right<0:
            self.kill()


groundscroll=0
birdgroup=pygame.sprite.Group()
angrybird=birds(50,450)
pipegroup=pygame.sprite.Group()
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
    pipegroup.draw(screen)
    birdgroup.update()
    screen.blit(ground,(groundscroll,682))
    fonttext1=font.render(str(score),True,"black")
    screen.blit(fonttext1,(20,20))
    if angrybird.rect.bottom>=682:
        gameover=True
        flying=False 
    if flying==True and gameover==False:
        timenow=pygame.time.get_ticks()
        if timenow-lastpipe>pipefreq:
            pipeheight=random.randint(-100,100)
            bottompipe=pipes(864,425+pipeheight,-1)
            toppipe=pipes(864,425+pipeheight,1)
            pipegroup.add(bottompipe)
            pipegroup.add(toppipe)
            lastpipe=timenow
        pipegroup.update()

        groundscroll-=4

        if groundscroll<-36:
            groundscroll=0

    pygame.display.update()