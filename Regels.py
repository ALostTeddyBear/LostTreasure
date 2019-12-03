add_library("sound")
import Functies
import Main

def setup():
    global scene
    fullScreen()
    
    scene = ''
    Background = loadImage("RulesBackground.jpg")
    Background.resize(width, height)
    background(Background)

    
def draw():
    global scene
    if scene == "main":
        Main.draw()
        return
    
    Font = createFont("Rapscallion.ttf", 100)
    textFont(Font)
    text("Spel Regels!", width / 2, height / 8)
    fill(240, 223, 55)
    
    fill(255)
    stroke(204, 102, 0)
    rect(width-150, height-75, 127, 35)
    
    fill(0)
    textSize(28)
    text("Terug", width-87, height-47)
    
    def isMouseWithinSpace(x, y, breedte, hoogte):
        if (x < mouseX < x + breedte and y < mouseY < y + hoogte):
            return True
        else:
            return False
    
    if isMouseWithinSpace(width-150, height-75, 127, 35):
        if mousePressed:
            Main.setup()
            scene = 'main'
            
    if scene == "main":        
        if isMouseWithinSpace(width-300, height-75, 100, 35):
            if mousePressed:
                scene = ''
            
            
        
