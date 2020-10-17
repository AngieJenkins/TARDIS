import random

class SpaceObject:
    
    def __init__(self, name=None):
        self.name = name
    def __repr__(self):
        return self.name

class Planet(SpaceObject):
    def __init__(self, name, population=None):
        super().__init__(name)
        self.population = population or []

class Animal:
    def __init__(self, name=None, hobby=None):
        self.name = name
        self.hobby = hobby
    def __repr__(self):
        return self.name
        
class Panda(Animal):
    def __init__(self, name, hobby, food=None):
        super().__init__(name)
        self.food = food
    def yam_yam(self):
        number = random.randint(1,20)
        print(self.name + ' the panda eats ' + str(number), self.food)

class Tiger(Animal):
    def __init__(self, name, hobby, age=None, birthplace=None):
        super().__init__(name)
        self.age = age
        self.birthplace = birthplace
    def attack(self):
        print(self.name + ' attacks with a tiger-style kung-fu strike!')

class Fox(Animal):
    def __init__(self, name, hobby, colour=None):
        super().__init__(name)
        self.colour = colour
    def sing(self):
        message = input('What does the fox say?')
        print(self.name + ' the fox sings: ' + message + '!')
        
      
Earth = Planet('Earth')

Po = Panda('Po', 'kung-fu', 'dumplings')
Earth.population.append(Po)

Tigress = Tiger('Tigress', 'kung-fu', 5, 'China')
Earth.population.append(Tigress)

Alice = Fox('Alice', 'singing', 'red')
Earth.population.append(Alice)

Li = Panda('Li', 'eating', 'burgers')
Earth.population.append(Li)

print(Earth.population)
Tigress.attack()




    
