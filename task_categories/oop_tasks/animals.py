# TASK: Create dog, cat, bird and ant classes according to the tests written below
"""
Rules:
    - You are not allowed to create more than 5 classes.
    - Neither of the 4 classes are allowed to have "describe" method in them
"""

class Animal():
    def __init__(self, typ, legs, sound):
        self.typ = typ
        self.legs = legs
        self.sound = sound

    def get_type(self):
        return self.typ

    def get_number_of_legs(self):
        return self.legs
    
    def say(self):
        return self.sound 
    
    def describe(self):
        return f"{self.typ} with {self.legs} legs that says '{self.sound}'."


class Dog(Animal):
    def __init__(self):
        super().__init__('A mammal', 4, 'bark')

class Cat(Animal):
    def __init__(self):
        super().__init__('A mammal', 4, 'meow')
    
class Bird(Animal):
    def __init__(self):
        super().__init__('A bird', 2, 'chirp')

class Ant(Animal):
    def __init__(self):
        super().__init__('An insect', 8, 'nothing')

# Don't change the code below this line


dog = Dog()
cat = Cat()
bird = Bird()
ant = Ant()

dog_tests = 0
if dog.get_type() == 'A mammal':
    dog_tests += 1
if dog.get_number_of_legs() == 4:
    dog_tests += 1
if dog.say() == 'bark':
    dog_tests += 1
if dog_tests == 3:
    print('Dog data is correct')
else:
    print('Dog data is incorrect')

cat_tests = 0
if cat.get_type() == 'A mammal':
    cat_tests += 1
if cat.get_number_of_legs() == 4:
    cat_tests += 1
if cat.say() == 'meow':
    cat_tests += 1
if cat_tests == 3:
    print('Cat data is correct')
else:
    print('Cat data is incorrect')

bird_tests = 0
if bird.get_type() == 'A bird':
    bird_tests += 1
if bird.get_number_of_legs() == 2:
    bird_tests += 1
if bird.say() == 'chirp':
    bird_tests += 1
if bird_tests == 3:
    print('Bird data is correct')
else:
    print('Bird data is incorrect')

ant_tests = 0
if ant.get_type() == 'An insect':
    ant_tests += 1
if ant.get_number_of_legs() == 8:
    ant_tests += 1
if ant.say() == 'nothing':
    ant_tests += 1
if ant_tests == 3:
    print('Ant data is correct')
else:
    print('Ant data is incorrect')

print(dog.describe())
if dog.describe() == "A mammal with 4 legs that says 'bark'.":
    print('CORRECT')
else:
    print('INCORRECT')

print(cat.describe())
if cat.describe() == "A mammal with 4 legs that says 'meow'.":
    print('CORRECT')
else:
    print('INCORRECT')

print(bird.describe())
if bird.describe() == "A bird with 2 legs that says 'chirp'.":
    print('CORRECT')
else:
    print('INCORRECT')

print(ant.describe())
if ant.describe() == "An insect with 8 legs that says 'nothing'.":
    print('CORRECT')
else:
    print('INCORRECT')
