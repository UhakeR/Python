# creare una classe:

class Car():

    def __init__(self, make, model, year):
        """ Inizializziamo gli attributi della macchina. """
        self.make = make
        self.model = model
        self.year = year

        # Stabilisco la capacità e il livello di benzina in galloni.
        self.fuel_capacity = 15
        self.fuel_level = 0

    def fill_tank(self):
        """ Riempi di benzina fino al pieno. """
        self.fuel_level = self.fuel_capacity
        print("Fuel tank is full.")

    def drive(self):
        """Simula la guida."""
        print("The car is moving.")


# Creare un oggetto da una classe:

from car import Car

my_car = Car('audi', 'a4', 2017)
print(my_car.make)
print(my_car.model)
print(my_car.year)

# my_car è un oggetto della classe Car. I suoi attributi sono audi (corrisponde al make), a4 (corrisp. al modello) e 2017 (corrisponde all'anno)
# vanno messi nell'ordine preciso in cui sono stati esplicitati nell'inizializzazione.