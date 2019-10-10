
# Restituisce la rappresentazione in stringa dell'oggetto.

class Person:
    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return {'name' : self.name, 'age' : self.age}

    def __str__(self):
        return 'nome: ' + self.name + ', età: ' + str(self.age)

p = Person('Peta Jensen', 28)

print(p.__str__())