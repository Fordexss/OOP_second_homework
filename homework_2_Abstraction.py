# Створіємо клас
class AreaCalculation():
    def area(self):
        pass


# Підкласи
class Circle(AreaCalculation):
    def __init__(self, radius):
        self.radius = radius  # Публічний атрибут

    def area(self):
        return round(3.1415 * self.radius ** 2, 3)


# Створюємо та заповнюємо об'єкт "Круг"
circle = Circle(3)
print("Площа круга:", circle.area())
print("Радіус круга:", circle.radius)



