import pygame,random
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("SPACE GETS INVADED... OR DOES IT?")

bot1=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("bot1.png"),(50,50)),90)
bot2=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("bot2.png"),(50,50)),270)
bg=pygame.image.load("spaceeeeeee.png")
border=pygame.Rect(400,0,25,600)

class bots(pygame.sprite.Sprite):
    def __init__(self,x,y,image,controls,side):
        super().__init__()
        self.image=image
        self.rect=self.image.get_rect(topleft=(x,y))
        self.controls=controls
        self.side=side
        self.health=10

    def move(self,keys):
        if keys[self.controls["up"]] and self.rect.y>0:
            self.rect.y-=3
        if keys[self.controls["down"]] and self.rect.y<550:
            self.rect.y+=3
        if keys[self.controls["left"]]:
            if self.side=="left" and self.rect.x>0:
                self.rect.x-=3
            if self.side=="right" and self.rect.x>400:
                self.rect.x-=3
        if keys[self.controls["right"]]:
            if self.side=="right" and self.rect.x<800:
                self.rect.x+=3
            if self.side=="left" and self.rect.x<380:
                self.rect.x+=3

    def shoot(self,bullets):
        if self.side=="left":
            bullet=Bullet(self.rect.right,self.rect.centery,5,"yellow")
        else:
            bullet=Bullet(self.rect.left,self.rect.centery,-5,"pink")
        bullets.add(bullet)

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,speed,color):
        super().__init__()
        self.image=pygame.Surface((10,5))
        self.image.fill(color)
        self.rect=self.image.get_rect(topleft=(x,y))
        self.speed=speed

    def update(self):
        self.rect.x+=self.speed
        if self.rect.right<0 or self.rect.left>800:
            self.kill()

#maingame
yellowship=bots(20,30,bot1,{"up":pygame.K_w,"down":pygame.K_s,"left":pygame.K_a,"right":pygame.K_d,"shoot":pygame.K_LSHIFT},"left")
pinkship=bots(760,30,bot2,{"up":pygame.K_UP,"down":pygame.K_DOWN,"left":pygame.K_LEFT,"right":pygame.K_RIGHT,"shoot":pygame.K_RSHIFT},"right")

#creating groups
allsprites=pygame.sprite.Group(yellowship,pinkship)
bullets=pygame.sprite.Group()

gameover=False
winner=""

#gameloop

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

        if event.type==pygame.KEYDOWN and not gameover:
            if event.key==yellowship.controls["shoot"]:
                yellowship.shoot(bullets)

            if event.key==pinkship.controls["shoot"]:
                pinkship.shoot(bullets)
    
    keys=pygame.key.get_pressed()
    
    if not gameover:
        yellowship.move(keys)
        pinkship.move(keys)
        bullets.update()

        #bullet collisions
        for bullet in bullets:
            if bullet.speed>0 and pinkship.rect.colliderect(bullet.rect):
                pinkship.health-=1
                bullet.kill()
            elif bullet.speed<0 and yellowship.rect.colliderect(bullet.rect):
                yellowship.health-=1
                bullet.kill()

        if yellowship.health<=0:
            winner="Pinkship is the Winner!!!"
            gameover=True
        elif pinkship.health<=0:
            winner="Yellowship is the Winner!!!"
            gameover=True

    #draw
    screen.blit(bg,(0,0))
    pygame.draw.rect(screen,"black",border)
    allsprites.draw(screen)
    bullets.draw(screen)
    font=pygame.font.SysFont("calligrapher",30)
    fonttext1=font.render(f"Pinkship Health={pinkship.health}",True,"white")
    fonttext2=font.render(f"Yellowship Health={yellowship.health}'",True,"white")
    screen.blit(fonttext1,(50,40))
    screen.blit(fonttext2,(500,40))

    if gameover:
        fonttext3=font.render(f"GAMEOVER!! {winner}",True,"white")
        screen.blit(fonttext3,(300,210))

    pygame.display.update()
