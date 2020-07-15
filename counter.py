class Counter:
    def __init__(self):
        self.value = 0
    def count_up(self):
        self.value += 1

class DispleyValue:
    def displey(self):
        print(f"value is {self.value}")

class DisplayCounter(Counter,DisplayValue):
    pass

if __name__ == '__main__':
    c = DisplayCounter()
    for i in range(10):
        c.count_up()
    c.display()