from animal import Animal
from dog import Dog

ani = Animal("Fido", "Blue", 2)
ani2 = Animal(colour="pink")

# ani.name = "Fido"
# ani.colour = "Blue"
# ani.limbcount = 2

ani2.name = "Fifi"
ani2.limbcount = -1
#ani2.set_limbcount(-1)
print(ani2.limbcount)

print(f"{ani2.name} has {ani2.limbcount} limbs!")


print(ani.move("East"))
print(ani2.move("West"))
print(ani.eat("Crisps"))
print(ani2.eat("Banana"))

print(ani)

a = ani.__add__(ani2)
print(ani)

dog = Dog("Rover", "Purple", 4, 30)


print(dog.__str__() + " " + str(dog.taillength))

