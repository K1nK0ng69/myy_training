class House:
    def __init__(self, name, numFloors):
        self.Name = name
        self.Floors = numFloors
    
    def GoTo(self, floor):
        if(floor < 1 or floor > self.Floors):
            print("Такого этажа не существует")
            return None
        for i in range(floor):
            print(i+1)
            
    def __len__(self):
        return self.Floors
        
    def __str__(self):
        return f"Название: {self.Name}, кол-во этажей {self.Floors}"
        
    def __eq__(self, obj):
        if(not isinstance(obj, House)): return False
        return self.Floors == obj.Floors
        
    def __ne__(self, obj):
        if(not isinstance(obj, House)): return False
        return not self == obj
        
    def __lt__(self, obj):
        if(not isinstance(obj, House)): return False
        return self.Floors < obj.Floors
        
    def __le__(self, obj):
        if(not isinstance(obj, House)): return False
        return (self < obj) or (self == obj)
        
    def __gt__(self, obj):
        if(not isinstance(obj, House)): return False
        return not self <= obj
        
    def __ge__(self, obj):
        if(not isinstance(obj, House)): return False
        return not self < obj
        
    def __add__(self, num):
        if(not isinstance(num, int)): return False
        return House(self.Name, self.Floors + num)
        
    def __radd__(self, num):
        if(not isinstance(num, int)): return False
        return self + num
        
    def __iadd__(self, num):
        if(not isinstance(num, int)): return False
        return self + num

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__