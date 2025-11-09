import random, pgzrun
TITLE="GREEN ALIEN BLOB GAME!! :)"
WIDTH=500
HEIGHT=500
alien=Actor("greenblobthatsanalien")
alien.pos=(50,40)
def draw():
    screen.fill("pink")
    alien.draw()

pgzrun.go()
