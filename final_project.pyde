rect_x = 800
rect_y = random(300,800)
x_speed = 3
y_speed = 0

bird_x = 150
bird_y = 400
gravity= 10
bird_death = False
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
    #tube(random(800), random(300,600))
    tube()

    if rect_x <= -80:
        rect_x =  1000
        rect_y =  random(300,600)

  

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
    if keyPressed and key == 'r' or key == 'R':
        bird_y = bird_y - gravity*5
    if bird_y >= 700:
        bird_y = 700
        bird_death = True
        
    
    
    
    
    
    
def tube():
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
    rect(rect_x, rect_y, 50, 900)
    rect(rect_x-30, rect_y-30, 110, 50)
    rect_x = rect_x + x_speed
    rect_y = rect_y + y_speed
    #top
    rect(rect_x-28,rect_y-200,110,50)
    rect(rect_x, rect_y - 200, 50, -900)
    rect_x = rect_x + x_speed
    rect_y = rect_y + y_speed
  
