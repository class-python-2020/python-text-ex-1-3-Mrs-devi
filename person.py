class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Player(Person):
    def __init__(self,name,age,number,position):
        super().__init__(name,age)
        self.number = number
        self.position = position

 def toString(self):
    print(f"私の名前は{self.name},年齢は{self.age}です。")
    print(f"背番号は{self.number},ポジションは{self.porition}です。")

obj = Player("高橋洋平",29,10,"MF")
obj.toString()