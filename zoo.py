class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def make_sound(self):
        print(self.sound)

    def eat(self):
        print(self.food)

class Bird(Animal):
    def __init__(self, name, age, sound, food):
        super().__init__(name, age)
        self.sound = sound
        self.food = food

    def make_sound(self):
        print(f"{self.name} издает звук {self.sound}")
    def food(self):
        print(f"{self.name} ест {self.food}")

class Mammal(Animal):
    def __init__(self, name, age, sound, fur_color, food):
        super().__init__(name, age)
        self.sound = sound
        self.fur_color = fur_color
        self.food = food

    def make_sound(self):
        print(f"{self.name} издает звук {self.sound}")

    def eat(self):
        print(f"{self.name} ест {self.food}")

    def fur_color(self):
        print(f"{self.name} имеет {self.food} окрас")

class Reptile(Animal):
    def __init__(self, name, age, sound, food, habitat):
        super().__init__(name, age)
        self.sound = sound
        self.food = food
        self.habitat = habitat

    def make_sound(self):
        print(f"{self.name} издает звук {self.sound}")

    def eat(self):
        print(f"{self.name} ест {self.food}")

    def habitat(self):
        print(f"{self.name} обитает в {self.habitat}")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

animals = [Bird("Tweety", 2, "щебет", "крошки"),
           Mammal("Doggy", 5, "гав", "рыжий", "мясо"),
           Reptile("Snakey", 3, "шипение", "моллюски", "лес")]

animal_sound(animals)


class Zoo():
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} успешно добавлен в зоопарк")

    def add_staff(self, staff):
        self.staff.append(staff)
        print(f"Сотрудник {staff.name} успешно добавлен в штат работников зоопарка")


class Employee():
    def __init__(self, name):
        self.name = name

class ZooKeeper(Employee):
    def feed_animal(self, animal):
        print(f"{self.name} кормит животное {animal.name}")

class Veterinarian(Employee):
    def hear_animal(self, animal):
        print(f"{self.name} лечит животное {animal.name}")


bird = Bird("Tweety", 2, "щебет", "крошки")
mammal = Mammal("Doggy", 5, "гав", "рыжий", "мясо")
reptile = Reptile("Snakey", 3, "шипение", "моллюски", "лес" )

# Тестирование методов
bird.make_sound()
bird.eat()
mammal.make_sound()
mammal.eat()
reptile.make_sound()
reptile.eat()

zoo = Zoo()
zoo.add_animal(Mammal("Лошадь", 4, "иго-го", "рыжий", "овес"))
zoo.add_staff(ZooKeeper("Вася"))
zoo.add_staff(Veterinarian("Петя"))

zoo.animals[0].make_sound()
zoo.staff[0].feed_animal(zoo.animals[0])
zoo.staff[1].hear_animal(zoo.animals[0])


zoo = {
    "Львы": ["Симба", "Муфаса"],
    "Тигры": ["Шерхан"],
    "Обезьяны": ["Кинг Конг", "Абу"]
}

import json

def сохранить_зоопарк(имя_файла, зоопарк):
    with open(имя_файла, 'w', encoding='utf-8') as файл:
        json.dump(зоопарк, файл, ensure_ascii=False, indent=4)

def загрузить_зоопарк(имя_файла):
    try:
        with open(имя_файла, 'r', encoding='utf-8') as файл:
            зоопарк = json.load(файл)
        return зоопарк
    except FileNotFoundError:
        print("Файл не найден. Создается новый состав зоопарка.")
        return {}

имя_файла = "зоопарк.json"

# Добавление животных в зоопарк (пример)
zoo["Пингвины"] = ["Пинг", "Понг"]

# Сохранение состояния зоопарка в файл
сохранить_зоопарк(имя_файла, zoo)

# Загрузка зоопарка из файла при следующем запуске
zoo = загрузить_зоопарк(имя_файла)
print(zoo)




















