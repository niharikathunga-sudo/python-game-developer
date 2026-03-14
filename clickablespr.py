import pygame, random
pygame.init()
screen=pygame.display.set_mode((300,300))

class click(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((200,100))
        self.image.fill("Blue")
        self.rect=self.image.get_rect(center=(150,150))
        

    def mouse(self,pos):
        if self.rect.collidepoint(pos):
            one=random.randint(0,255)
            two=random.randint(0,255)
            three=random.randint(0,255)

            self.image.fill((one,two,three))


experiment=click()
color=pygame.sprite.GroupSingle(experiment)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

        elif event.type==pygame.MOUSEBUTTONUP:
            experiment.mouse(event.pos)

    screen.fill("white")
    color.draw(screen)

    pygame.display.update()
