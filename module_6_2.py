class Vehicle:
    def __init__(self, owner, model, clr, engpwr):
        self.Owner = owner
        self._Model = model
        self._EnginePower = engpwr
        self._Color = clr
        self._COLORS = [
            "white",
            "gray",
            "black"
        ]

    def GetModel(self):
        return f"Модель: {self._Model}"

    def GetHorsePower(self):
        return f"Мощность двигателя: {self._EnginePower}"

    def GetColor(self):
        return f"Цвет: {self._Color}"

    def GetOwner(self):
        return f"Владелец: {self.Owner}"

    def PrintInfo(self):
        print(self.GetModel())
        print(self.GetHorsePower())
        print(self.GetColor())
        print(self.GetOwner())

    def SetColor(self, clr):
        clr = clr.lower()
        if (clr in self._COLORS):
            self._Color = clr
        else:
            print(f"Нельзя сменить цвет на {clr}")


class Sedan(Vehicle):
    _PASSENGER_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)


vehicle1.PrintInfo()


vehicle1.SetColor('Pink')
vehicle1.SetColor('BLACK')
vehicle1.Owner = 'Vasyok'

vehicle1.PrintInfo()



