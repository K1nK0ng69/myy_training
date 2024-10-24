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
            
h1 = House("ЖК Горский", 18)
h2 = House("Домик в деревне", 2)
h1.GoTo(5)
h2.GoTo(10)