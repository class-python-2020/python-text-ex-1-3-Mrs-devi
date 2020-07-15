class A:
    def print(self):
        print("A")
class B:
    def print(self):
        print("B")
class C:
    def print(self):
        print("C")
class Hoge(C,A,B):
    pass

h = Hoge()
h.print()