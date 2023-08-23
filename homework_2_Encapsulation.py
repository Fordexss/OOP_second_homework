# Тип: public
# Створює клас
class Person:
    def __init__(self, name, age, number):  # public age and name
        self.name = name
        self.age = age
        self.number = number


# Створюємо об'єкт класу Person
person = Person("Іван", 25, "+38665342865")

# Виводимо інформацію про об'єкт
print("Ім'я:", person.name)
print("Вік:", person.age)
print("Номер Телефону:", person.number)

# Змінюємо дані об'єкта напряму
person.name = "Владислав"
person.age = 13
person.age = "+380952836751"

# Виводимо оновлену інформацію
print("\nОновлене ім'я:", person.name)
print("Оновлений вік:", person.age),
print("Оновлений номер телефону:", person.number)


# Тип: private
# Створює клас
class My_Bank:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Приватне поле
        self.__balance = balance  # Приватне поле

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Гроші успішно внесено.")
        else:
            print("Некоректна сума для внесення.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print("Гроші успішно знято.")
        else:
            print("Недостатньо коштів на рахунку або некоректна сума для зняття.")


# Створюємо об'єкт класу My_Bank
account = My_Bank(account_number="123456789", balance=1000)

# Отримуємо баланс рахунку
print("Поточний баланс:", account.get_balance())

# Вносимо гроші на рахунок
account.deposit(500)
print("Новий баланс після внесення:", account.get_balance())

# Знімаємо гроші з рахунку
account.withdraw(200)
print("Новий баланс після зняття:", account.get_balance())


# Тип protect
# Створюємо клас
class Human:
    def __init__(self, name, age):
        self._name = name  # protect поле
        self._age = age  # protect поле

    def display_info(self):
        print("Ім'я:", self._name)
        print("Вік:", self._age)


# Підклас
class Student(Human):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self._student_id = student_id  # Тип protect

    def display_info(self):
        super().display_info()
        print("Студентський ID:", self._student_id)


# Заповнюємо екземпляри
student = Student(name="Артем", age=20, student_id="GD2516")

# Виводимо інформацію про студента
student.display_info()
