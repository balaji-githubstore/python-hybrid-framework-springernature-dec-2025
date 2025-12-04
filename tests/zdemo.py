class Parent:
    def __init__(self):
        self.a = 10
        print("father c")

    def father(self):
        print("father")


class Son(Parent):
    def __init__(self):
        super().__init__()
        self.b = 20
        print("son c")

    def son(self):
        print("son")


s = Son()
s.father()
s.son()

print(s.a)
print(s.b)
