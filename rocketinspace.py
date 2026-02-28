import pygame
pygame.init()

screen=pygame.display.set_mode((800,600))

pygame.display.set_caption("Rocket zooming in space...")

class rocketed(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("rocketspace.png")
        self.image=pygame.transform.scale(self.image,(70,100))
        self.rect=self.image.get_rect()
    
    def update(self,keys):
        if keys[pygame.K_UP]:
            self.rect.move_ip(0,-5)
        elif keys[pygame.K_DOWN]:
            self.rect.move_ip(0,5)
        elif keys[pygame.K_LEFT]:
            self.rect.move_ip(-5,0)
        elif keys[pygame.K_RIGHT]:
            self.rect.move_ip(5,0)
        if self.rect.left<0:
            self.rect.left=0
        

# make a group of the sprites

rocket1=rocketed()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

    keys=pygame.key.get_pressed()
    rocket1.update(keys)

    screen.blit(pygame.image.load("spacebg.png"),(0,0))
    screen.blit(rocket1.image,rocket1.rect.topleft)

    pygame.display.update()
    
