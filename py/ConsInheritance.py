class A:
    def __init__(self,a):
        self.a=a;
    def show(self):
        print(self.a)

class B:
    def __init__(self,b):
        self.b=b;
    def show(self):
        print(self.b)

class C(A,B):
    def __init__(self):
        A.__init__(80)
        B.__init__(100)
        self.c=self.a+self.b;
    def show(self):
        print(self.c)

Z=C();
Z.show()