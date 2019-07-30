def setup():
    size(700, 800)
    background(79, 80, 150)

    
    DAY_BACKGROUND = loadImage("Screen Shot 2019-07-29 at 10.30.48 AM.png")
    image(DAY_BACKGROUND, 0,0, 700, 800)
    
    Bird_Y = 200
    y_speed = 5





    """
    Bird = loadImage("Screen Shot 2019-07-29 at 11.19.16 AM.png")

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
   # bird 1 movement

    fill(65, 182, 230)
    DAY_BACKGROUND = loadImage("Screen Shot 2019-07-29 at 10.30.48 AM.png")
    image(DAY_BACKGROUND,0,0, 700, 800)
    bird_Movement() 

    
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
