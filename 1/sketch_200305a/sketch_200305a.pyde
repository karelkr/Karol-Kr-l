def setup():
    size(600, 600)
    background(255,165,0)
def draw():
     line(height, width, mouseX, mouseY)
     rect(200,200,200,200)
     print(height, width, mouseX, mouseY,mousePressed)
     if mousePressed:
         rect(mouseX, mouseY, mouseX, mouseY)
         clear()