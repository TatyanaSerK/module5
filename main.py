class home:
    numberOfFloors = 10

    def lift(self):
        Floor = self
        while home.numberOfFloors != Floor:
            Floor += 1
            print('Текущий этаж равен: ', Floor)


home.lift( 0 )