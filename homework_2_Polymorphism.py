# Батькіський клас
class Animal:
    def __init__(self, food):
        self.food = food

    def speak(self):
        pass


# підкласи
class Dog(Animal):
    def speak(self):
        return f"Гав! Моя улюблена їжа {self.food}"


class Cat(Animal):
    def speak(self):
        return f"Мяу! Моя улюблена їжа {self.food}"


class Duck(Animal):
    def speak(self):
        return f"Квак! Моя улюблена їжа {self.food}"


def animal_speak(animal):
    print(animal.speak())


# Екземпляр класу до кожного класу додаємо до кожної тваринки свою їжу та команду голос
dog = Dog("м'ясо")
cat = Cat("риба")
duck = Duck("дрібна рибка")

animal_speak(dog)
animal_speak(cat)
animal_speak(duck)
