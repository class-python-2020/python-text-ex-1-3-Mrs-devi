class Animal:
    def __init__(self,name):
        self.name = name
    def cry(self):
        print(f"{self.name}は「むー」と鳴いた")

class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)
def cry(self):
    print(f"{self.name}は「ニャー」と鳴いた")

tama = Cat("タマ")
tama.cry()
animal = Animal("動物")
animal.cry()
