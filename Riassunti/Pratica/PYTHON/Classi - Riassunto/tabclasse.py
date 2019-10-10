
class Classe():
    def __init__(self, attributo1, attributo2, attributo3):
        self.attributo1 = attributo1
        self.attributo2 = attributo2
        self.attributo3 = attributo3

    def funzione1(self):
        return self.attributo1 + self.attributo2

    def __str__(self):
        return self.attributo2 + self.attributo3


