import pgzrun
HEIGHT=600
WIDTH=800
TITLE="WELCOME TO QUIZ MASTER..."
questions=[]
scrollerbox=Rect(0,0,800,80)
questionbox=Rect(0,0,600,150)
answerbox1=Rect(0,0,300,150)
answerbox2=Rect(0,0,300,150)
answerbox3=Rect(0,0,300,150)
answerbox4=Rect(0,0,300,150)
timerbox=Rect(0,0,200,150)
skipbox=Rect(0,0,200,320)
score=0
totaltime=25
gameover=False
currentq=0
totalq=0
scrollerbox.move_ip(0,0)
questionbox.move_ip(20,100)
answerbox1.move_ip(20,270)
answerbox2.move_ip(20,440)
answerbox3.move_ip(340,270)
answerbox4.move_ip(340,440)
timerbox.move_ip(620,100)
skipbox.move_ip(650,270)
answers=[answerbox1,answerbox2,answerbox3,answerbox4]

def draw():
    screen.fill(color="black")
    screen.draw.filled_rect(scrollerbox,"black")
    screen.draw.filled_rect(questionbox,"beige")
    for i in answers:
        screen.draw.filled_rect(i,"light pink")
    screen.draw.filled_rect(timerbox,"white")
    screen.draw.filled_rect(skipbox,"white")
    scrollerboxmessage=f"WELCOME TO QUIZ MASTER... Q:{currentq}/{totalq}"
    screen.draw.textbox(scrollerboxmessage,scrollerbox,color="white")
    screen.draw.textbox("SKIP", skipbox ,color="black",angle=-90)
    screen.draw.textbox(str(totaltime),timerbox,color="black")
    screen.draw.textbox(q[0].strip(),questionbox,color="black")
    index=1
    for i in answers:
        screen.draw.textbox(q[index].strip(),i,color="black")
        index+=1
        
def on_mouse_down(pos):
    index=1
    for i in answers:
        if i.collidepoint(pos):
            if index is int(q[5]):
                correctanswer()
            else:
                game_over()
        index+=1
    if skipbox.collidepoint(pos):
        skipquestion()

def correctanswer():
    global totaltime,q,score
    score+=1
    if questions:
        q=readnextq()
        totaltime=25
    else:
        game_over()

def game_over():
    global totaltime,gameover,q
    message=f"GAME OVER..YOU GOT {score} QUESTIONS CORRECT"
    q=[message,"-","-","-","-",0]
    totaltime=0
    gameover=True


def update():
    scrollerbox.x-=2
    if scrollerbox.right<0:
        scrollerbox.left=800

def readfile():
    global totalq
    with open("questions.txt","r") as file:
        for i in file:
            questions.append(i)
            totalq+=1

def readnextq():
    global currentq
    currentq+=1
    return questions.pop(0).split("|")

def timer():
    global totaltime
    if totaltime:
        totaltime-=1
    else:
        game_over()

def skipquestion():
    global totaltime,q
    if questions:
        q=readnextq()
        totaltime=25
    else:
        game_over()



readfile()
q=readnextq()
clock.schedule_interval(timer,1)
pgzrun.go()