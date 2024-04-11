class home:                # зададим класс дом
    numberOfFloors = 10    # количество этажей в доме

    def lift(self):                                  # создадим функцию лифт(для перебора этажей)
        Floor = self                                 # создадим переменную этаж
        while Floor != home.numberOfFloors:          # пока этаж не равен макс значению
            Floor += 1                               # прибавим 1 этаж
            print('Текущий этаж равен: ', Floor)     # выводим текущее значение этажа


home.lift(0)
