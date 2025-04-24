class Superhero:
    def __init__(self, name, power, strength):
        self.name = name
        self.power = power
        self.strength = strength

    def introduce(self):
        return f"I am {self.name}, and my power is {self.power}!"

    def use_power(self):
        return f"{self.name} uses {self.power} with strength level {self.strength}."


class FlyingSuperhero(Superhero):
    def __init__(self, name, power, strength, fly_speed):
        super().__init__(name, power, strength)
        self.fly_speed = fly_speed

    def use_power(self):
        return f"{self.name} flies at {self.fly_speed} km/h and uses {self.power}!"


class TechSuperhero(Superhero):
    def __init__(self, name, power, strength, gadget):
        super().__init__(name, power, strength)
        self.gadget = gadget

    def use_power(self):
        return f"{self.name} uses their {self.gadget} to boost {self.power}!"


print("=== Superheroes ===")
hero1 = FlyingSuperhero("Falcon", "Wind Control", 85, 300)
hero2 = TechSuperhero("IronTech", "Laser Blast", 90, "Arm Cannon")

print(hero1.introduce())
print(hero1.use_power())

print(hero2.introduce())
print(hero2.use_power())


class Vehicle:
    def move(self):
        print("Vehicle is moving...")


class Car(Vehicle):
    def move(self):
        print("Driving")


class Plane(Vehicle):
    def move(self):
        print("Flying")


class Boat(Vehicle):
    def move(self):
        print("Sailing")


print("\n=== Vehicles in Motion ===")
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()

