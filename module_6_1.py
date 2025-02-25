class Animal:        #Растение
    alive = True         #(живой)
    fed = False          #(накормленный)

    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

    def eat(self, food):    #еда
        if food.edible:
            self.fed = True
            print(f'{self.name} съел {food.name}')

        else:
            self.alive = False
            print(f"{self.name} не стал есть {food.name}")


class Plant:                 #Животное
    edible = False                    #(съедобность)

    def __init__(self, name):
        self.name = name
        self.edible = False

class Mammal(Animal):             #млекопитающее

    def __init__(self, name):
        self.name = name


class Predator(Animal):               #Хищник

    def __init__(self, name):
        self.name = name


class Flower(Plant):  #Цветок
    edible = False                                  # (съедобность)
    def __init__(self, name):
        self.name = name

class Fruit (Plant): #Фрукты
    edible = True
    def __init__(self, name):
        self.name = name
        self.edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)