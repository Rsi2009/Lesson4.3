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
        print(f"{self.name} says hiss")

    def eat(self):
        print(f"{self.name} ест {self.food}")

    def habitat(self):
        print(f"{self.name} обитает в {self.habitat}")














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

