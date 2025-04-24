Superhero and Vehicle Simulation

This project demonstrates the concepts of inheritance and polymorphism using object-oriented programming (OOP). It simulates superheroes with unique powers and vehicles with different modes of movement, where each class defines its own behavior.

Features
	1.	Superhero Class: Represents a superhero with attributes like name, power, and strength, and includes methods for introducing the hero and using their power.
	2.	Subclasses:
	•	FlyingSuperhero: Adds fly speed and overrides the power usage method.
	•	TechSuperhero: Uses a gadget to enhance the hero’s power.
	3.	Vehicle Class: Represents a vehicle with a move() method, overridden in subclasses like Car, Plane, and Boat to define their respective movements.

Example Usage:

Superheroes

hero1 = FlyingSuperhero("Falcon", "Wind Control", 85, 300)
hero2 = TechSuperhero("IronTech", "Laser Blast", 90, "Arm Cannon")

print(hero1.introduce())  # Falcon is introduced
print(hero1.use_power())  # Falcon flies and uses Wind Control

print(hero2.introduce())  # IronTech is introduced
print(hero2.use_power())  # IronTech uses Arm Cannon to boost Laser Blast

Vehicles

vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()  # Prints "Driving", "Flying", "Sailing" accordingly

Summary

This project showcases how inheritance and polymorphism can be used to create flexible and reusable structures for superheroes and vehicles in object-oriented programming.
