import pgzrun, random
HEIGHT=800
WIDTH=600
levels=4
startspeed=10
normalstars=["greenstar","orangestar","yellowstar","redstar","bluestar"]
gameover=False
gamewin=False
currentlevel=1
additems=[]
animations=[]

def draw():
    screen.blit("galaxybg",(0,0))

    if gameover:
        screen.draw.text("OH NO YOU LOST!! :(",fontsize=40,center=(200,100),color="white")
    elif gamewin:
        screen.draw.text("YAY YOU WON!! :)",fontsize=40,center=(200,100),color="white")

    else:
        for i in additems:
            i.draw()
def update():
    global additems
    if len(additems)==0:
        additems=masteritemcreator(currentlevel)
def masteritemcreator(numitems):
    itemstocreate=itempicker(numitems)
    itemtoimage=imageloader(itemstocreate)
    itemlayout(itemtoimage)
    animateditems(itemtoimage)
    return itemtoimage

def itempicker(numitems):
    itemstocreate=["purplestar"]
    for i in range(numitems):
        randomoption=random.choice(normalstars)
        itemstocreate.append(randomoption)
    return itemstocreate

def imageloader(itemstocreate):
    itemtoimage=[]
    for i in itemstocreate:
        image=Actor(i)
        itemtoimage.append(image)
    
    return itemtoimage

def itemlayout(itemstolayout):
    numgaps=len(itemstolayout)+1
    gapsize=WIDTH/numgaps
    random.shuffle(itemstolayout)
    for index,item in enumerate(itemstolayout,1):
        xpos=index*gapsize
        item.x=xpos

def animateditems(itemstoanimate):
    global animations
    for i in itemstoanimate:
        duration=startspeed-currentlevel
        i.anchor=("center","bottom")
        animation=animate(i,duration=duration,y=800,on_finished=handlegameover)
        animations.append(animation)

def handlegameover():
    global gameover
    gameover=True

def on_mouse_down(pos):
    for i in additems:
        if i.collidepoint(pos):
            if "purplestar" in i.image:
                handlegamewin()
            else:
                handlegameover()

def handlegamewin():
    global gamewin,additems,animations,currentlevel
    stopanimations(animations)
    if currentlevel==levels:
        gamewin=True
    else:
        currentlevel+=1
        additems=[]
        animations=[]

def stopanimations(animationstostop):
    for i in animationstostop:
        if i.running:
            i.stop()

pgzrun.go()
