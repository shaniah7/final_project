def setup():
    size(700, 800)
    background(79, 80, 150)

    
    DAY_BACKGROUND = loadImage("Screen Shot 2019-07-29 at 10.30.48 AM.png")
    image(DAY_BACKGROUND, 0,0, 700, 800)
    
    
    
    
    bird_x = 0
    bird_y = 350
    """
    Bird = loadImage("Screen Shot 2019-07-29 at 11.19.16 AM.png")

    image(Bird, 350,0, 100, 100)
    
    """

def draw():

   # bird 1 movement

    fill(65, 182, 230)
    DAY_BACKGROUND = loadImage("Screen Shot 2019-07-29 at 10.30.48 AM.png")
    image(DAY_BACKGROUND, 0,0, 700, 800)
    ellipse(250, mouseY, 30, 30)
