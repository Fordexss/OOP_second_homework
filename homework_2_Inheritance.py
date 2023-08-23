# Батьківський клас
class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    # Методи до нього
    def cost(self):
        print(f"Привіт, я {self.brand} та моя ціна {self.price}")

    def characteristics(self, processor, video_card, RAM):
        print(f"Ось мої характеристики:\n{self.brand}\nПроцесор: {processor}, Відеокарта: {video_card}, RAM: {RAM}")


# 2 підкласи до батькіського класу Laptop
class Apple(Laptop):
    def __init__(self, brand, price, processor, video_card, RAM):
        super().__init__(brand, price)
        self.processor = processor
        self.video_card = video_card
        self.RAM = RAM


class Dell(Laptop):
    # Виклакаємо конструктор батьківського класу (super) та даємо аргументи
    def __init__(self, brand, price, processor, video_card, RAM):
        super().__init__(brand, price)
        self.processor = processor  # Встановлюємо атрибути об'єктів
        self.video_card = video_card
        self.RAM = RAM


# Робимо екземпляри класів
dell_laptop = Dell("Dell Latitude 7430 2-in-1", 86000, "Intel Core i7-1265U", "Intel Iris Xe Graphics", "16GB")
dell_laptop.cost()  # Вивід: Привіт, я Dell та моя ціна 2000
dell_laptop.characteristics("Intel i7", "Intel Iris Xe Graphics", "16GB\n")

apple_laptop = Apple("Apple MacBook Pro 16", 150.000, "Intel Core i9", "AMD Radeon Pro 5600M", "16GB")
apple_laptop.cost()  # Вивід: Привіт, я Apple та моя ціна 2000
apple_laptop.characteristics("Intel Core i9", "AMD Radeon Pro 5600M", "16GB")
