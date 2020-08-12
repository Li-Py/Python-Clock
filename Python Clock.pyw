import turtle
from datetime import datetime
from math import sin
from math import cos
from math import radians

TURTLE_WIDTH  = 600 #the width of the canvas
TURTLE_HEIGHT = 600 #the height of the canvas

TITLE_POS    = (0,225) #the position of the title
TITLE_FONT   = ("Consolas",30,"bold") #the font of the title
PLATE_RADIUM = 200 #the radium of the clock plate
LONG_LENGTH  = 20  #the length of the long scales in the plate
SHORT_LENGTH = 10  #the length of the short scales in the plate
SCALE_WIDTH  = 5   #the width of the scales in the plate

HOUR_LENGTH   = 100 #the length of the hour hand
HOUR_WIDTH    = 5   #the width of the hour hand
MINUTE_LENGTH = 190 #the length of the minute hand
MINUTE_WIDTH  = 5   #the width of the minute hand
SECOND_LENGTH = 180 #the length of the second hand
SECOND_WIDTH  = 3   #the width of the second hand

HOUR_STEP  = 30 #the step-angle of the hour hand
SCALE_STEP = 6  #the step-angle of scale, minute hand and hour hand

WEEK_POS  = (0,80) #the position of what we print the information of week
WEEK_FONT = ("Arial",20,"bold") #the font of the information of week
DATE_POS  = (0,-80) #the position of what we print the information of date
DATE_FONT = ("Times New Roman",20,"bold") #the font of the information of date

#Every day of a week
TPL_WEEK = ("Sunday","Monday","Tuesday","Wednesday",\
            "Thursday","Friday","Saturday")
#Every month of a year
TPL_MONTH = ("January","February","March","April","May","June","July",\
             "August","September","October","November","December") 


# get the shape of the hand
# param: the length of the hand
# return: the shape of the hand
def Hand_getShape(length):
    turtle.reset()
    turtle.seth(90)
    turtle.penup()
    turtle.forward(-length//10)
    turtle.pendown()
    turtle.begin_poly()
    turtle.forward(length//10 + length)
    return turtle.get_poly()

#Callback function for drawing hands and printing date
def Clock_drawCallBack():
    global hourHand,minHand,secHand
    timNow = datetime.today()
    second = timNow.second
    minute = timNow.minute
    hour = timNow.hour + minute/60
    hourHand.seth(90 - HOUR_STEP * hour)
    minHand.seth(90 - SCALE_STEP * minute)
    secHand.seth(90 - SCALE_STEP * second)
    turtle.goto(WEEK_POS)
    turtle.write(TPL_WEEK[timNow.weekday()],align = "Center",
                 font = WEEK_FONT)
    turtle.goto(DATE_POS)
    turtle.write("{} {} {}".format(timNow.year,\
                 TPL_MONTH[timNow.month - 1],timNow.day),
                 align = "Center",font = DATE_FONT)
    turtle.ontimer(Clock_drawCallBack,100)

#initilize the setting of the turtle
def Turtle_init():
    turtle.title("Python Clock")
    turtle.setup(width = TURTLE_WIDTH,height = TURTLE_HEIGHT)

#initlize the hand of the clock
def Hand_init():
    global hourHand,minHand,secHand
    turtle.register_shape("hourHand",Hand_getShape(HOUR_LENGTH))
    turtle.register_shape("minHand",Hand_getShape(MINUTE_LENGTH))
    turtle.register_shape("secHand",Hand_getShape(SECOND_LENGTH))
    hourHand = turtle.Turtle()
    hourHand.shape("hourHand")
    hourHand.shapesize(1,1,HOUR_WIDTH)
    minHand = turtle.Turtle()
    minHand.shape("minHand")
    minHand.shapesize(1,1,MINUTE_WIDTH)
    secHand = turtle.Turtle()
    secHand.shape("secHand")
    secHand.shapesize(1,1,SECOND_WIDTH)
    for hand in (hourHand,minHand,secHand):
        hand.speed(0)

#initlize the plate of the clock
def Plate_init():
    turtle.reset()
    turtle.pensize(SCALE_WIDTH)
    turtle.penup()
    turtle.goto(TITLE_POS)
    turtle.write("Python Clock",align = "Center",
                 font = TITLE_FONT)
    turtle.goto(0,0)
    theta = 0
    turtle.seth(90)
    while theta < 360:
        turtle.penup()
        turtle.goto(PLATE_RADIUM*sin(radians(theta)),\
                    PLATE_RADIUM*cos(radians(theta)))
        turtle.pendown()
        if theta%30:
            turtle.forward(SHORT_LENGTH)
        else:
            turtle.forward(LONG_LENGTH)
        turtle.right(SCALE_STEP)
        theta += SCALE_STEP
    turtle.penup()
    turtle.speed(0)
    turtle.penup()
    turtle.hideturtle()

turtle.showturtle()
turtle.tracer(False)
Turtle_init()
Hand_init()
Plate_init()
turtle.tracer(True)
Clock_drawCallBack()
turtle.mainloop()
