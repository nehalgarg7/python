class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.cluth = False

    def start(self):
        self.cluth = True
        self.acc = True
        print("car started...")

car1=Car()
car1.start()