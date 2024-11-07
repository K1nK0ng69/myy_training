class Animal:
    def __init__(self, name):
        self.Alive = True
        self.Fed = False
        self.Name = name
        
class Plant:
    def __init__(self, name):
        self.Edible = False
        self.Name = name
        
class Mammal(Animal):
    
    def Eat(self, food):
        if(not isinstance(food, Plant)):
            self.Alive = False
            print(f"{self.Name} погибает от голода")
        if(food.Edible):
            self.Fed = True
            print(f"{self.Name} съел {food.Name}")
        else:
            self.Alive = False
            print(f"{self.Name} не стал есть {food.Name}")
        
class Predator(Animal):
    def Eat(self, food):
        if(not isinstance(food, Plant)):
            self.Alive = False
            print(f"{self.Name} погибает от голода")
        if(food.Edible):
            self.Fed = True
            print(f"{self.Name} съел {food.Name}")
        else:
            self.Alive = False
            print(f"{self.Name} не стал есть {food.Name}")
            
class Flower(Plant):
    pass
        
class Fruit(Plant):
    def __init__(self, name):
        self.Name = name
        self.Edible = True
        
        
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.Name)
print(p1.Name)

print(a1.Alive)
print(a2.Fed)
a1.Eat(p1)
a2.Eat(p2)
print(a1.Alive)
print(a2.Fed)




