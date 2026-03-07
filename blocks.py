import random,pygame
pygame.init()
screen=pygame.display.set_mode((800,600))

class sacrifices(pygame.sprite.Sprite):
    def __init__(self,color):
        super().__init__()
        self.image=pygame.Surface((20,15))
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.reset()



    def reset(self):
        self.rect.x=random.randint(0,800)
        self.rect.y=random.randint(-500,-20)



    def update(self):
        self.rect.y+=1
        if self.rect.y>600:
            self.reset()



score=0



    
class mainsacrifice(sacrifices):

    def update(self):
        pos=pygame.mouse.get_pos()
        self.rect.x=pos[0]
        self.rect.y=pos[1]


blackblocklist=pygame.sprite.Group()
allspriteslist=pygame.sprite.Group()

red=mainsacrifice("red")
allspriteslist.add(red)

for i in range(50):
    black=sacrifices("black")
    blackblocklist.add(black)
    allspriteslist.add(black)

clock=pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

    screen.fill("white")

    allspriteslist.update()
   
    # check if the player block has collided with ANYTHING

    blockhitlist=pygame.sprite.spritecollide(red,blackblocklist,False)
    for i in blockhitlist:
        score+=5
        print(f"SCORE={score}")
        i.reset()

    allspriteslist.draw(screen)
    clock.tick(60)

    pygame.display.update()
    