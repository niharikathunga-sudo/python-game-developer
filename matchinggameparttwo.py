import pygame
import sys

pygame.init()

screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Match the Game")
screen.fill((255,255,255))

#Load images
images= {
    "Subway Surfer":pygame.image.load("subway surfers.png"),
    "Ludo":pygame.image.load("ludo.png"),
    "Temple Run":pygame.image.load("temple run.png"),
    "Candy Crush":pygame.image.load("candy crush.jpg")


    }

image_positions={
    "Subway Surfer":pygame.Rect(150,100,100,50),
    "Ludo":pygame.Rect(150,200,100,50),
    "Temple Run":pygame.Rect(150,300,100,50),
    "Candy Crush":pygame.Rect(150,400,100,50),
}

text_positions={
    "Ludo":pygame.Rect(350,100,150,50),
    "Candy Crush":pygame.Rect(350,200,150,50),
    "Subway Surfer":pygame.Rect(350,300,150,50),
    "Temple Run":pygame.Rect(350,400,150,50),
}

correct_matches= {
    "Subway Surfer":"Subway Surfer",
    "Ludo":"Ludo",
    "Temple Run":"Temple Run",
    "Candy Crush":"Candy Crush",
}

font=pygame.font.SysFont("Time New Roman",30)

for name, pos in image_positions.items():
    screen.blit(images[name],(pos.x,pos.y))

for name, pos in text_positions.items():
    text_surface=font.render(name, True,(0,0,0))
    screen.blit(text_surface,(pos.x,pos.y))

pygame.display.update()

running=True
lines=[]
score=0
matched_pairs=[]

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        elif event.type==pygame.MOUSEBUTTONDOWN:
            start_pos=pygame.mouse.get_pos()

        elif event.type==pygame.MOUSEBUTTONUP:
            end_pos=pygame.mouse.get_pos()

            start_label=None
            end_label=None

            for lable,rect in image_positions.items():
                if rect.collidepoint(start_pos):
                    start_label=lable
                    #break

            for lable,rect in text_positions.items():
                if rect.collidepoint(end_pos):
                    end_label=lable
                    #break

            if start_label and end_label:
                pygame.draw.line(screen,(0,0,25), start_pos,end_pos,4)
                pygame.display.update()

                if correct_matches.get(start_label)==end_label and (start_label, end_label) not in matched_pairs:
                    score+=1
                    matched_pairs.append((start_label, end_label))
                    print(f"Correct match! Score: {score}")

                else:
                    print(f"Wrong match... Score {score}")

pygame.quit()
sys.exit()

        

    
