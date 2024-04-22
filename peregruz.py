class Buiding:                            #создадим новый класс Buiding

    def __init__(self, _floor, _type):    #создадим инициализатор для класса Buiding
        self.numberOfFloors = int(_floor) #зададим целочисленный атрибут этажности self.numberOfFloors
        self.buildingType = str(_type)    #зададим строковый атрибут self.buildingType

    def __eq__(self, other):              #перегрузим __eq__
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


B1 = Buiding(_floor=5, _type='жилой')   #вызовим класс
B2 = Buiding(_floor=1, _type='магазин')  #вызовим класс с другими параметрами

print(B1 == B2)     # используйте атрибут numberOfFloors и buildingType для сравнения


