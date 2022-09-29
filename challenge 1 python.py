import turtle
import time
def challenge():
    turtle.write("You must write a script who does that. You have 5 minutes ! Let's go !")
    time.sleep(5)
    turtle.reset()
    for i in range(180):
        turtle.hideturtle()
        turtle.forward(40)
        turtle.goto(0, 0)
        turtle.right(2)
    turtle.reset()
    minutes = 4
    while minutes != 0:    
        seconds = 60
        while seconds != 0:
            time.sleep(1)
            seconds -= 1
            turtle.reset()
            turtle.hideturtle()
            turtle.write(minutes, " ")
            turtle.write(" : ", " ")
            turtle.write(seconds, " ")
        minutes -= 1
            

def reset():
    turtle.reset()
    

    
