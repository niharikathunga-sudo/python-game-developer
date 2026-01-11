import random
import pgzrun
WIDTH=500
HEIGHT=500

def draw():
    screen.fill("navy blue")
    screen.draw.filled_circle((100,210),50,"pink")
    screen.draw.line((0,0),(500,500),"white")
    screen.draw.text("niha",(50,60),fontsize=70,color="yellow",gcolor="light blue",owidth=1.5,ocolor="pink")

    """w=400
    h=200
    for i in range(20):
        corrdinates=Rect((0,0),(w,h))
        corrdinates.center=250,250
        screen.draw.rect(corrdinates,"white")
        w-=15
        h+=20"""



pgzrun.go()
    