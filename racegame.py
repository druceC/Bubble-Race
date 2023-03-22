import os, random

path = os.getcwd()

class Creature:
    def __init__(self, x, y, r, g,img, img_w, img_h):
        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.vy = 1
        self.vx = 0
        self.img = loadImage(path + "/images/" + img )
        self.img_w = img_w
        self.img_h = img_h
    def gravity(self):
        if self.y + self.r >= self.g: 
            self.vy = 0
        else:
            self.vy = self.vy + 0.4
            if self.y + self.r + self.vy > self.g:
                self.vy = self.g - (self.y + self.r)
    
    def update(self):
        self.gravity()
        self.y = self.y + self.vy
        self.x = self.x + self.vx
        
    def display(self):
        self.update()
        strokeWeight(0)
        fill(255, 0, 0)
        image(self.img,self.x,self.y/2)
        
class Bubblecar(Creature):
    def __init__(self, x, y, r, g):
        Creature.__init__(self, x, y, r, g,"bubblecar.png", 100, 70) 
        self.key_handler = {LEFT:False, RIGHT:False, UP:False}
        
    def update(self):
        self.gravity()
        
        if self.key_handler[LEFT] == True:
            print("uu")
            self.vx = -20
            # self.dir = LEFT
        elif self.key_handler[RIGHT] == True:
            print("uu")
            self.vx =20
            # self.dir = RIGHT
        else:
            self.vx = 0
        
        if self.key_handler[UP] == True :#and self.y + self.r == self.g:
            self.vy = -10
            
        self.y = self.y + self.vy
        self.x = self.x + self.vx
        
        if self.x< 0:
            self.x =0
        
        if self.x>game.w-self.r:
            self.x=game.w-self.r
        
class Game:
    def __init__(self, w, h, g):
        # global path
        self.w = w
        self.h = h
        self.g = g
        self.bubblecar = Bubblecar(470, 700, 280, self.g)
        self.bg_imgs = []
                                                             
        self.bg_imgs.append(loadImage(path + "/images/layer1.png"))
        self.bg_imgs.append(loadImage(path + "/images/layer2.png"))
          
    def display(self):
       
        image(self.bg_imgs[0],0,0)
        image(self.bg_imgs[1],0,0)
        
        self.bubblecar.display()
            
            
game = Game(1280, 720,1000)

def setup():
    size(game.w, game.h)
    background(255,255,255)

def draw():
    background(255,255,255)
    game.display()

def keyPressed():
    if keyCode == LEFT:
        game.bubblecar.key_handler[LEFT] = True
        
    elif keyCode == RIGHT:
        game.bubblecar.key_handler[RIGHT] = True
    elif keyCode == UP:
        game.bubblecar.key_handler[UP] = True

def keyReleased():
    if keyCode == LEFT:
        game.bubblecar.key_handler[LEFT] = False
    elif keyCode == RIGHT:
        game.bubblecar.key_handler[RIGHT] = False
    elif keyCode == UP:
        game.bubblecar.key_handler[UP] = False

def mouseClicked():
    global game
    if game.bubblecar.alive == False:
        # game.bg_sound.close()
        game = Game(1280, 720, 585)
