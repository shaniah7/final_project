rect_x = 800
rect_y = random(200,600)

rect2_x = 1100
rect2_y = random(200,600)

rect3_x = 1400
rect3_y = random(200,600)
x_speed = 3
y_speed = 0

bird_x = 150
bird_y = 400
gravity= 15
Death = False
def setup():
    size(700,800)
    background(0,105,148)
    
    DAY_BACKGROUND = loadImage("Screen Shot 2019-07-29 at 10.30.48 AM.png")
    image(DAY_BACKGROUND, 0,0, 700, 800)




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
    global rect2_x 
    global rect2_y
    global rect3_x 
    global rect3_y
    #tube(random(800), random(300,600))
    tube1()
    tube2()
    tube3()

    if rect_x <= -60:
        rect_x =  900
        rect_y =  random(300,600)
      
    if rect2_x <= -60:
        rect2_x =  900
        rect2_y =  random(300,600)  
    
       
    if rect3_x <= -60:
        rect3_x =  900
        rect3_y =  random(300,600) 
    
  
#when the bird will hits the pipe the rect_X's will all stop and the bird will go to 0
    bird()
    #if bird death = true:
        
    
def bird():
    global bird_x
    global bird_y
    global birdx_spd
    global birdy_spd
    global gravity
    ellipse(bird_x, bird_y,30,30)
    bird_y = bird_y + gravity
    if bird_y >= 700:
        bird_y = 700 
        print("dead")
    if keyPressed and key == 'r' or key == 'R':
        bird_y = bird_y - gravity*3.6
    # # if bird_y < rect_y and bird_x > rect_x and bird_x > 600:
    #     print("dead")
    #     x_speed = -13
    
    
    # elif bird_y < rect_y - 30 and bird_x > rect_x - 30 and bird_x > 50:
    #     print("dead")
    #     x_speed = -13
   
     
    # elif bird_y < rect_y - 250 and bird_x > rect_x - 20 and bird_x > 50:
    #     print("dead")
    
    #     x_speed = -13
    # elif bird_y < rect_y - 250 and bird_x > rect_x - 8 and bird_x > 600:
        
    #     print("dead")
    #     x_speed = -13

    
    
    
def tube1():
    global x_speed
    global y_speed
    global rect_x
    global rect_y
    #xPos = rect_x + 50
    #yPos = rect_y + 50
    x_speed = -10
    y_speed = 0

    fill(44, 176, 26)
    #bottom 
    rect(rect_x, rect_y, 50, 600)
    rect(rect_x-30, rect_y-30, 110, 50)
    rect_x = rect_x + x_speed
    rect_y = rect_y + y_speed
    #top
    rect(rect_x-20,rect_y-250,110,50)
    rect(rect_x + 8, rect_y - 250, 50, -600)
    rect_x = rect_x + x_speed
    rect_y = rect_y + y_speed
    
    
    
def tube2():
    global x_speed
    global y_speed
    global rect2_x 
    global rect2_y
    

    x_speed = -10
    y_speed = 0

    fill(44, 176, 26)
    #bottom 
    rect(rect2_x  , rect2_y, 50, 600)
    rect(rect2_x-30 , rect2_y-30, 110, 50)
    rect2_x = rect2_x + x_speed
    rect2_y = rect2_y + y_speed
    #top
    rect(rect2_x-20 ,rect2_y-250,110,50)
    rect(rect2_x + 8, rect2_y - 250, 50, -600)
    rect2_x = rect2_x + x_speed
    rect2_y = rect2_y + y_speed
    
    
def tube3():
    global x_speed
    global y_speed
    global rect3_x 
    global rect3_y
    
    #xPos = rect_x + 50
    #yPos = rect_y + 50
    x_speed = -10
    y_speed = 0

    fill(44, 176, 26)
    #bottom 
    rect(rect3_x  , rect3_y, 50, 600)
    rect(rect3_x-30 , rect3_y-30, 110, 50)
    rect3_x = rect3_x + x_speed
    rect3_y = rect3_y + y_speed
    #top
    rect(rect3_x-20 ,rect3_y-250,110,50)
    rect(rect3_x + 8, rect3_y - 250, 50, -600)
    rect3_x = rect3_x + x_speed
    rect3_y = rect3_y + y_speed
  
