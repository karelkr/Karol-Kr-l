def setup():
    size(600, 600)
    background(0)
    global obrazeczek
    obrazeczek = loadImage("kozak.jpg")
    strokeWeight(10)
    noFill()
 
def draw():
    try:
        image(obrazeczek, width/30, height/30, 400, 400)
    except:
        stroke("#FF0000")
        text("blad: brak obrazka", width - 100, height - 50)
    else:
        stroke("#0000FF")
    finally:
        rect(width/30, height/30, 400, 400)
