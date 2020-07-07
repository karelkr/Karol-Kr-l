class Spinner():
    colors = ["#6b5b95", "#feb236", "#d64161", "#ff7b25"]
    color = 0
    spinnage = 1

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
    
    def spin(self):
        stroke(self.colors[self.color])

        pushMatrix()
        translate(self.x, self.y)

        rotate(self.spinnage * 0.01 * TWO_PI)
        line(0, 0, self.size, self.size)

        popMatrix()
        if self.spinnage % 10 == 0:
            self.color = (self.color + 1) % len(self.colors)
        self.spinnage += 1

def setup():
    size(700, 700)
    strokeWeight(3)
    
    global spinnerList
    spinnerList = []

def draw():
    background(0)
    for i in spinnerList:
        i.spin()

def mousePressed():
    global spinnerList
    spinnerList.append(Spinner(mouseX, mouseY, mouseY/5))
    
# 2 pkt +
