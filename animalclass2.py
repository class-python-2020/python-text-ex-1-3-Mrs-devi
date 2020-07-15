from abc import ABCMeta,abstractmethod

class Animal(metaclass = ABCMeta):
    @abstractmethod
    def cry(self):
        pass

class Cat(Animal):
    def cry(self):
        print("にゃー"*10)

class Dog(Animal):
    def cry(self):
        print("わん"*10)

class Hors(Animal):
    def cry(self):
        print("火品"*10)

tama = Cat()
tama.cry()
inu = Dog()
inu.cry()
uma = Hors()
uma.cry()
