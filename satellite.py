import random,pgzrun
from time import time 
print(time())
WIDTH=500
HEIGHT=500
satellites=[]
start=0
totaltime=0
currentsatellite=0
tot=8
lines=[]
for i in range(8):
    satellite=Actor("satellite.png")
    satellite.pos=random.randint(10,450), random.randint(10,450)
    satellites.append(satellite)
start=time()

def draw():
    screen.blit("galaxy",(0,0))
    number=1
    for i in satellites:
        i.draw()
        screen.draw.text(str(number),(i.pos[0],i.pos[1]+20))
        number+=1
    for i in lines:
        screen.draw.line(i[0],i[1],"yellow")

def on_mouse_down(pos):
    global currentsatellite,lines
    if currentsatellite < tot:
        if satellites[currentsatellite].collidepoint(pos):
            if currentsatellite:
                lines.append((satellites[currentsatellite-1].pos,satellites[currentsatellite].pos))
            currentsatellite+=1

        else:
            lines=[]
            currentsatellite=0




pgzrun.go()
