add_library("sound")
import Functies
import Regels
import Regels3

def setup():
    global scene
    
    fullScreen()
    scene = ''
    Background = loadImage("RulesBackground.jpg")
    Background.resize(width, height)
    background(Background)
    
def isMouseWithinSpace(x, y, breedte, hoogte):
    if (x < mouseX < x + breedte and y < mouseY < y + hoogte):
        return True
    else:
        return False
    
def draw():
    global scene
    if scene == "regels":
        Regels.draw()
        return
    
    if scene == "regels3":
        Regels3.draw()
        return
    
    img = loadImage("Speluitleg.png")
    imageMode(CENTER)
    image(img, width / 2, height / 2)
    
    Font = createFont("Rapscallion.ttf", 100)
    textFont(Font)
    text("Spel Regels!", width / 2, height / 8)
    fill(240, 223, 55)
    
    fill(255)
    stroke(204, 102, 0)
    rect(width - 300, height - 75, 127, 35)
    
    fill(0)
    textSize(28)
    text("Terug", width - 240, height - 47)
    
    fill(255)
    stroke(204, 102, 0)
    rect(width - 150, height - 75, 127, 35)
    
    fill(0)
    textSize(28)
    text("Volgende", width - 87, height - 47)
    
    if isMouseWithinSpace(width - 300, height - 75, 127, 35):
        if mousePressed:
            Regels.setup()
            scene = 'main'
            
    if scene == "regels":        
        if isMouseWithinSpace(width - 350, height - 75, 100, 35):
            if mousePressed:
                scene = ''
    
    if isMouseWithinSpace(width - 150, height - 75, 127, 35):
        if mousePressed:
            Regels3.setup()
            scene = 'regels3'
            
    if scene == "regels3":        
        if isMouseWithinSpace(width - 350, height - 75, 100, 35):
            if mousePressed:
                scene = ''
        
