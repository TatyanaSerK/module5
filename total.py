class Building:                #новый класс Buiding
    total = 0                  #зададим атрибут total

    def __init__(self):        #инициализатор для класса Buiding
        Building.total += 1    #увеличим атрибут total класса Building

while Building.total < 40:          #цикл создает 40 объектов класса Building
    house = Building()              #вызываем класс
    print('это дом под номером', Building.total)      #выведим на экран
