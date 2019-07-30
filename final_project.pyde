


def setup():
    import random

    size(700, 800)
    background(79, 80, 150)

    DAY_BACKGROUND = loadImage("Screen Shot 2019-07-29 at 10.30.48 AM.png")
    image(DAY_BACKGROUND, 0, 0, 700, 800)

    Bird_Y = 200
    y_speed = 5

def tube():
    
    x = 100
    x = ra(x)
    
    
    y = 200
    Y1 = 50
    fill(44, 176, 26)
    #bottom 
    rect(x, y, 50, 900)
    rect(x-30, y-40, 110, 50)
    #top
    rect(x,50,50,-900)
    rect(x-30,Y1,110,50)
def bird():
    bird_X = 250
    bird_Y = height/2
    ellipse(bird_X, bird_Y, 50, 50)
    
def bird_fall():
    

    
    
    """
    #Bird = loadImage("Screen Shot 2019-07-29 at 11.19.16 AM.png")

    image(Bird, 350,0, 100, 100)
    
    """
"""
def bird_Movement():
    y_speed = 5
    Bird_Y = 200
    ellipse(250, Bird_Y, 30, 30)
    if Bird_Y > 850:
        Bird_Y = bird_Y + y_speed
    if Bird_Y < 650:
        Bird_Y + y_speed

    if Bird_Y < 0:
        y_speed = - y_speed
"""
"""
if mousePressed:  # if key 'A' is pressed 
        Bird_Y = Bird_Y - 50
else:
    Bird_Y = Bird_Y + 50
"""

def draw():
    global y_speed
    global bird
    global tube
   # bird 1 movement

    fill(65, 182, 230)
    DAY_BACKGROUND = loadImage("Screen Shot 2019-07-29 at 10.30.48 AM.png")
    image(DAY_BACKGROUND, 0, 0, 700, 800)
    # bird_Movement()
    x = 5

    
    bird()



    tube()
    
    

"""            
def bird_Movement():
    y_speed = 5
    Bird_Y = 200
    ellipse(250, Bird_Y, 30, 30)
    if Bird_Y > 850:
        Bird_Y = bird_Y + y_speed
    if Bird_Y < 650:
        Bird_Y + y_speed

    if Bird_Y < 0:
        y_speed = - y_speed
"""
