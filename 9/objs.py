class MyVector: 

    def __init__(self):
        self.x = 1
        self.y = 1
        self.z = 1

    def asTupple(self):
        return self.x, self.y, self.z


class My4dVector(MyVector):
    def __init__(self):  
        self.w = 1 
        super().__init__()

    def asTupple(self):
        return self.x, self.y, self.z, self.w

t = MyVector()

t.x = 20

print(t)
print(t.asTupple())

l = My4dVector()
l
print(l.asTupple())