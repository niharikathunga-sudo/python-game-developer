import random,pgzrun
WIDTH=500
HEIGHT=500
bee=Actor("beeeeeee.png")
bee.pos=30,30
flower=Actor("flowerr.png")
flower.pos=50,50
score=0
gameover=False

def draw():
    screen.blit("background (grass)",(0,0))
    bee.draw()
    flower.draw()
    if gameover:
        screen.fill("pink")
        screen.draw.text(f"Your final score is.... {score}!!",(10,30),fontsize=45)

def update():
    global score
    if keyboard.left:
        bee.x-=2
    if keyboard.right:
        bee.x+=2
    if keyboard.up:
        bee.y-=2
    if keyboard.down:
        bee.y+=2

    if bee.colliderect(flower):
        flower.x=random.randint(0,500)
        flower.y=random.randint(0,500)
        score+=10
def timeout():
    global gameover
    gameover=True
clock.schedule(timeout,28)

pgzrun.go()
