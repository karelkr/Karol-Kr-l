import random # przypominam, tak importuje się moduły w pythonie
# Processing sam jest modułem, ale też możemy go rozszerzać o dodatkowe podmoduły
# Aby dodać podmoduł processingu wybieramy z menu Sketch pozycję Import library, interesować mogą nas np. PDF export
add_library('pdf') # te linie, jeżeli ich jeszcze nie ma doda nam automatycznie powyższa akcja; możemy je też wpisać ręcznie jeżeli już znamy nazwy interesujących nas modułów
add_library('sound')

# UWAGA program należy odpalić dwa razy i przeanalizować jego dwa warianty. W pierwszym odkomentowane są linijki zaczynające się od '1' w komentarzu, a zakomentowane z komentarzami zaczynającymi się od '2', przy drugim odpaleniu odwrotnie.
# jeżeli plik się nie otwiera, prawdopodobnie któryś krok został pominięty lub błędnie wykonany za tym lub POPRZEDNIM razem, do uszkodzonego pliku już nie zapisze ani go nie nadpisze, należy najpierw go usunąć, a potem próbować uruchomić program ponownie
# jeżeli plik się nie usuwa, należy najpierw zamknąć program Processing, aby zwolnić połączenie do pliku

def setup():
    global img # tworzymy globalną zmienną
    size(400, 400) #1 ustawiamy wielkość okna
    #size(400, 400, PDF, "banany.pdf") #2 w tym wariancie tworzymy program zamiast w oknie - na pustym pliku PDF o podanym rozmiarze i nazwie.
    img = loadImage("Lenna.png") #1 wczytujemy obraz (uwaga: nie wszystkie formaty wczytuje, można podać nazwę pliku znajdującego się lokalnie w folderze projektu w folderze data lub adres na serwerze - internetowy)
    #img = loadShape("https://upload.wikimedia.org/wikipedia/commons/f/f7/Bananas.svg") #2 w przypadku plików wektorowych korzystamy z analogicznej funkcji, rónież mogą być zlokalizowane lokalnie lub na serwerze
    beginRecord(PDF, "outLenna.pdf") #1 tworzy plik PDF do którego od tego momentu będzie zapisywać zawartość naszego okna
    
    print(random.random()) # sprawdzamy działanie zaimportowanego modułu random
    print(type(img)) # sprawdzamy jakim typem obiektu stała się zmienna po wczytaniu do niej obrazu
    fill(20,255,200) # ustawiamy wypełnienie dla kształtów


def draw():
    global img
    image(img, 0,0, height, width) #1 wyświetlamy wczytany obraz we wskazanych wpółrzędnych (czyli w rogu 0,0) skalując do wymiaru wysokości i szerokości naszego okna
    #shape(img, 0,0, height/2, width/2) #2 wyświetlamy wczytany kształt we wskazanych współrzędnych  skalując do wysokości i szerokości pliku
    rect(20,50,100,200) # dorysowujemy prostokąt
    endRecord() #1 kończymy zapisywanie do pliku PDF, by nie zapisać tylu obrazów na sobie co odpalonych klatek. Można zapis zrobić dopiero po wykonaniu kilku operacji draw, np. jeżeli chcielibyśmy narsować jakiś obraz kilkukrotnie w paru miejscach przesuwając go co klatkę
    #exit() #2 plik zapisze się dopiero przy jego zamknięciu będącym jednocześnie zamknięciem zapisywania


def mousePressed():
    exit()
