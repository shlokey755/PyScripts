import random

class Car:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self):
        self.position += random.randint(1, 5)

def print_race(cars):
    for car in cars:
        print(f"{car.name}: {' ' * car.position}|{car.name}'s position")

def race():
    car1 = Car("Car A")
    car2 = Car("Car B")
    car3 = Car("Car C")

    cars = [car1, car2, car3]

    while True:
        print_race(cars)
        input("Press Enter to race...")

        for car in cars:
            car.move()

        if any(car.position >= 20 for car in cars):
            winner = max(cars, key=lambda car: car.position)
            print(f"\n{winner.name} wins the race!")
            break

if __name__ == "__main__":
    race()
