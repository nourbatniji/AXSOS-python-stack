class Animal:
    def __init__(self,animal_type, animal_name, animal_age, health_level, happiness_level):
        self.type = animal_type
        self.name = animal_name
        self.age = animal_age
        self.health = health_level
        self.happiness = happiness_level
    
    def feed(self):
        self.health += 10
        self.happiness += 10
        print(f"{self.name}'s health level: {self.health} and happiness level: {self.happiness} after feeding.")
    
    def display_info(self):
        print(f"Animal: {self.type}, Name: {self.name}, Age: {self.age}, Health: {self.health}, Happiness: {self.happiness}")


class Dog(Animal):
    def __init__(self,type, name, age, health, happiness, sound):
        super().__init__(type, name, age, health, happiness)
        self.sound = sound

    def display_info(self):
        super().display_info()
        print(f"Sound: {self.sound}")

class Cat(Animal):
    def __init__(self, type, name, age, health, happiness, color):
        super().__init__(type, name, age, health, happiness)
        self.color = color

    def display_info(self):
        super().display_info()
        print(f"Color: {self.color}")


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self, animal):
        self.animals.append(animal)
   
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

zoo1 = Zoo("John's Zoo")

dog1 = Dog("Dog", "Nala", 2, 10, 5, "bark")
cat1 = Cat("Cat","Rajah", 4, 2, 4, "brown")
cat2 = Cat("Cat","Shera", 3, 7, 9, "white")

zoo1.add_animal(dog1)
zoo1.add_animal(cat1)
zoo1.add_animal(cat2)
zoo1.print_all_info()

print("-"*30)

dog1.feed()
cat1.feed()