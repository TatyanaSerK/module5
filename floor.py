class House:

    def __init__(self):
        self.numberOfFloors = 0


    def setNewNumberOfFloors(self, floors):
        numberOfFloors = self.numberOfFloors + floors
        print('Новый этаж равен: ', numberOfFloors)


H = House()

H.setNewNumberOfFloors(5)