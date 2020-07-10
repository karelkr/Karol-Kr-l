add_library('pdf')
def setup():
    global img0, img1, img2
    size(500, 500) #1 ustawiamy wielkość okna
    img0 = loadImage("zdjecie.jpg") #1 wczytujemy obraz (uwaga: nie wszystkie formaty wczytuje, można podać nazwę pliku znajdującego się lokalnie w folderze projektu w folderze data lub adres na serwerze - internetowy)
    img1 = loadImage("maska.png") #2 w przypadku plików wektorowych korzystamy z analogicznej funkcji, rónież mogą być zlokalizowane lokalnie lub na serwerze
    img2 = loadImage("okulary.png")
    
    

def draw():
    beginRecord(PDF, "nagranie.pdf")
    image(img0, 0,0, height, width)
    if keyCode == LEFT:
        image(img1, 110, 150, 275, 175)
        
    elif keyCode == RIGHT:
        image(img2, 100, 150, 300, 150)

def mousePressed():
    endRecord()
    exit()
