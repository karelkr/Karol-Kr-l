class Kwadrat():
    def __init__(self, bok): # konstruktor jak się dowiedzieliśmy jest metodą prywatną, nie można go wywołać na obiekcie klasy po kropce, ani po za klasą
        self.bok = bok
    def sketch(self, x, y):
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)
        
class PasiastyKwadrat(Kwadrat): # dziedziczymy po klasie Kwadrat aby móć skorzystać z jej funkcjonalności
    def sketchPasiasty(self, x, y, paski): # dodajemy ilość pasków, w które ma być kwadrat
        Kwadrat.sketch(self, x, y) # korzystamy z metody klasy bazowej
        space = self.bok/paski # wyliczamy przerwęmiędzy paskami
        _xLinii_ = 0 # to jest pole chronione, nie powinno się go używać w kodzie po za klaą i klasami po niej dziedziczącymi 
        for pasek in range(0, paski): # dorysowujemy paski
            line(x+_xLinii_, y, x+_xLinii_, y+self.bok)
            _xLinii_ +=space

class KwadratDoKwadratu(Kwadrat):
    def sketchKwadraciasty(self, x, y):
        rectMode(CENTER)
        Kwadrat.sketch(self, x, y)
        temp_bok = self.bok / 5
        while self.bok >= temp_bok:
            self.bok *= 0.8
            Kwadrat.sketch(self, x, y)
        rectMode(CORNER)
def setup():
    size(500, 500)
    malyKwadrat = Kwadrat(50.0) # obiekt typu kwardrat o wielkości 50
    malyKwadrat.sketch(200, 300) # rysujemy go w podanych wsółrzędnych
    malyKwadraciastyKwadrat = KwadratDoKwadratu(100)
    malyKwadraciastyKwadrat.sketchKwadraciasty(400, 400)
    duzyKwadraciastyKwadrat = KwadratDoKwadratu(250)
    duzyKwadraciastyKwadrat.sketchKwadraciasty(150, 150)
