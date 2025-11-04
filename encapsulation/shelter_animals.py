''' Class ShelterAnimals
shows use of parent class with child classes (Dog, Cat, Hermit Crab
K Riley 10/31/25

Parent Class is ShelterAnimal
Note use of class variable (shelterID)

Child class: Dog class
overrides speak, utilizes constructor and __str__ methods from parent

Child class: Cat class
Overrides speak, utilizes constructor and __str__ methods from parent
Has an additional method push_off_table that is not shared by parent class

Child class: HermitCrab class
Utilizes constructor and __str__ methods from parent
Does not override speak, so it uses the ShelterAnimal speak method

'''

# parent params: building, ID
# parent methods: toString, speak
class ShelterAnimal:    #Parent class
    shelterID = 1

    def __init__(self, bldg):
        self._bldg = bldg
        self._ID = ShelterAnimal.shelterID
        ShelterAnimal.shelterID = ShelterAnimal.shelterID + 1


    def __str__(self):
        return "Shelter animal " + str(self._ID)+ " in bldg " + self._bldg

# default speak method just returns "silence"
    def speak(self):
        print("...silence")

# child dog params: name (gets ID and building from parent)
# child dog methods: overrides toString and speak() from parent
class Dog(ShelterAnimal):
    def __init__(self, name, bldg):
        self._name = name
        super().__init__(bldg)

    def __str__(self):
        return super().__str__() + " is a dog named " + self._name

    def speak(self):
        print("Woof!")

# child cat params: name (gets ID and building from parent)
# child cat methods: push_off_table, overrides speak and toString
class Cat(ShelterAnimal):
    def __init__(self, name, bldg):
        self._name = name
        super().__init__(bldg)

    def __str__(self):
        return super().__str__() + " is a cat named " + self._name

    def speak(self):
        print("Meow!")

    def push_off_table(self, item = "water glass"):
        print(f"Pushing {item} off the table... crash!")

class Kitten(Cat):
    def __init__(self, name, bldg, vaccinated = False):
        self.vax = vaccinated
        super().__init__(name, bldg)

    def __str__(self):
        if self.vax:
            vax_str = " who is vaccinated"
        else:
            vax_str = " who is not vaccinated"
        return super().__str__() + vax_str

# child crab params: name (gets ID and building from parent)
# child crab methods: overrides toString and gets speak from parent
class HermitCrab(ShelterAnimal):
    def __init__(self, name, bldg):
        self._name = name
        super().__init__(bldg)

    def __str__(self):
        return super().__str__() + " is a hermit crab named " + self._name

# child rabbit params: name (gets ID and building from parent)
# child rabbit methods: eat, overrides toString, and gets speak from parent
class Rabbit(ShelterAnimal):
    def __init__(self, name, bldg):
        self._name = name
        super().__init__(bldg)

    def __str__(self):
        return super().__str__() + " is a rabbit named " + self._name

    def eat(self, quantity = 0, item = "carrots"):
        print(f"{self._ID} has eaten {quantity} {item}")
