rect_x = 800
rect_y = random(300,800)
x_speed = 3
y_speed = 0

def setup():
    size(700,800)
    background(0,105,148)
    
    DAY_BACKGROUND = loadImage("Screen Shot 2019-07-29 at 10.30.48 AM.png")
    image(DAY_BACKGROUND, 0,0, 700, 800)
    
    
    
# def tube():
#     # x_speed = 3
#     # y_speed = 3


#     bird_x = 0
#     bird_y = 350
    
#     # rect_x = 50
#     # rect_y = 500
   
#     fill(44, 176, 26)
#     #bottom 
#     rect(rect_x, rect_y, 50, 900)
#     rect(rect_x-30, rect_y-40, 110, 50)
#     rect_x = rect_x + x_speed
#     rect_y = rect_y + y_speed
#     #top
#     rect(rect_x-30,rect_y-200,110,50)
#     rect(rect_x, rect_y - 200, 50, -900)
#     rect_x = rect_x + x_speed
#     rect_y = rect_y + y_speed



"""
    Bird = loadImage("Screen Shot 2019-07-29 at 11.19.16 AM.png")

    image(Bird, 350,0, 100, 100)
    
    """
def draw():
    DAY_BACKGROUND = loadImage("Screen Shot 2019-07-29 at 10.30.48 AM.png")
    image(DAY_BACKGROUND, 0,0, 700, 800)
    
    global rect_x
    global rect_y
    global x_speed
    global y_speed
    global tube
    #tube(random(800), random(300,600))
    tube()

    if rect_x <= -80:
        rect_x =  800
        rect_y =  random(300,600)

    

    
    
def tube():
    global x_speed
    global y_speed
    global rect_x
    global rect_y
    #xPos = rect_x + 50
    #yPos = rect_y + 50
    x_speed = -5
    y_speed = 0

    fill(44, 176, 26)
    #bottom 
    rect(rect_x, rect_y, 50, 900)
    rect(rect_x-30, rect_y-40, 110, 50)
    rect_x = rect_x + x_speed
    rect_y = rect_y + y_speed
    #top
    rect(rect_x-30,rect_y-200,110,50)
    rect(rect_x, rect_y - 200, 50, -900)
    rect_x = rect_x + x_speed
    rect_y = rect_y + y_speed
  
