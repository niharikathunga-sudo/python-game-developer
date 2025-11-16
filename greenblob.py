import random, pgzrun
TITLE="GREEN ALIEN BLOB GAME!! :)"
WIDTH=500
HEIGHT=500
alien=Actor("greenblobthatsanalien")
alien.pos=(50,40)
message=""
def draw():
    screen.fill("pink")
    alien.draw()
    screen.draw.text(message,(10,30),fontsize=35)
def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        alien.x=random.randint(50,450)
        alien.y=random.randint(50,450)
        message="GNARLY!!"
    else:
        message="OH NO YOU MISSED!"

pgzrun.go()
