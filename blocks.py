import random,pygame
pygame.init()
screen=pygame.display.set_mode((800,600))

class sacrifices(pygame.sprite.Sprite):
    def __init__(self,color):
        super().__init__()
        self.image=pygame.Surface((20,15))
        self.image.fill(color)
        self.rect=self.image.get_rect()

    def reset(self):
        self.rect.x=random.randint(0,800)
        self.rect.y=random.randint(-300,-20)


    def update(self):
        self.rect.y+=1
        if self.rect.y>600:
            self.reset()

    
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
    black=sacrifice("red")