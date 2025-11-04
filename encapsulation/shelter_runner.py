from shelter_animals import *

a1 = ShelterAnimal("A")   # generic animal
a2 = ShelterAnimal("B")    # generic animal
s1 = Dog('Fido',"D")
s2 = Dog('Spot','D')
s3 = Cat('Whiskers', 'C')
s4 = Cat("Mittens",'C')
s5 = HermitCrab("Crabby","A")
s6 = Rabbit("Sniffles", "B")
s7 = Kitten("Bitsy", s4._bldg, True)


petlist = [a1, a2, s1, s2, s3, s4, s5, s6, s7]
for pet in petlist:
    print(f"{pet}")
    pet.speak()
    try: # test for cat before calling push_off_table
        pet.push_off_table("soda can")
        pet.push_off_table()
    except AttributeError:
        print("This ShelterAnimal does not have the attribute 'push_off_table()'")
    try:
        pet.eat(5, "lettuce")
        pet.eat()
    except AttributeError:
        print("This ShelterAnimal does not have the attribute 'eat()'")
    print()

