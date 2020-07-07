def setup():
    global letters_colors, is_key_pressed, swap, color_0, color_1, is_key_pressed, decor_which_color, decor_colors
    size(600,600)
    color_0 = 0
    color_1 = 0
    swap = False
    is_key_pressed = 0
    letters_colors = ["#FF6F61", "#6B5B95"]
    decor_colors = [255, 0]
    decor_which_color = 0
    textSize(100)
    textAlign(LEFT, TOP)
    strokeWeight(4)
def draw():
    global color_0, color_1, decor_which_color
    background(200)
    for i in range(0, 100, 10):
        stroke(decor_colors[decor_which_color])
        line(200 + i*1.75, 200, 200 + i*1.75 + 17.5, 200)
        line(200, 200 + i, 200, 200 + i + 10)
        line(200 + i*1.75, 300, 200 + i*1.75 + 17.5, 300)
        line(375, 200 + i, 375, 200 + i + 10)
        decor_which_color = (decor_which_color + 1) % 2
        
        stroke(decor_colors[decor_which_color])
        line(200 + i*1.75, 200 - 4, 200 + i*1.75 + 17.5, 200 + 4)
        line(200 - 4, 200 + i, 200 + 4, 200 + i + 10)
        line(200 + i*1.75, 300 - 4, 200 + i*1.75 + 17.5, 300 + 4)
        line(375 - 4, 200 + i, 375 + 4, 200 + i + 10)
        decor_which_color = (decor_which_color + 1) % 2
    color_0 = mouse_hover(200, 200)
    color_1 = is_key_pressed
    if swap:
        color_0, color_1 = color_1, color_0
    fill(letters_colors[color_0])
    text("K", 200, 200)
    fill(letters_colors[color_1])
    text("K", 300, 200)
    color_0 = 0; color_1 = 0
def keyPressed():
    global is_key_pressed, swap
    if keyCode == LEFT:
        swap = True
    if keyCode == RIGHT:
        swap = True
    if str(key).upper() == "K":
        is_key_pressed = 1
def keyReleased():
    global is_key_pressed, swap
    if keyCode == LEFT: 
        swap = False
    if keyCode == RIGHT:
        swap = False
    if str(key).upper() == "K":
        is_key_pressed = 0
def mouse_hover(x, y):
    if mouseX >= x and mouseX <= x + 100 and mouseY >= y and mouseY <= y + 100:
        return 1
    else:
        return 0
    
# 2pkt i + do aktywności za ciekawą ramkę
