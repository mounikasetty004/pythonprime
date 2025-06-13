#oops:
#EXAMPLE WITH CONSTRUCTOR
'''class Employee:
     def __init__(self,name,id,salary):
         self.name=name
         self.id=id
         self.salary=salary
     def output(self):
         return self.name,self.id
         #print("name:",self.name,"id:",self.id,"salaray:",self.salary)
x=Employee("mouni",982,209870)
x.output()
a=input("name:")
b=int(input("id:"))
c=float(input("salary:"))
y=Employee(a,b,c)
#y.output()
print("details:",y.output())
#EXAMPLE WITHOUT CONSTRUCTOR
class Employee:
     def Details(self,name,id,salary):
         self.name=name
         self.id=id
         self.salary=salary
     def output(self):
         return self.name,self.id
         #print("name:",self.name,"id:",self.id,"salaray:",self.salary)
x=Employee()
x.Details("mouni",982,209870)
print("details:",x.output())
#
class Employee:
     pass
x=Employee()
x.a=10
print(x.a)
y=Employee()
y.b=200
print(y.b)
#types of inheritence
#1single inheritence
class parent:
    def fun1(self):
        print("hoi")
    def fun2(self):
        print("hello")
class child(parent):
    def fun3(self):
        print("mounika")
x=child()
x.fun1()
x.fun2()
x.fun3()
#2multiple inheritence
class ParentA:
    def fun1(self):
        print("hoi")
    def fun2(self):
        print("hello")
class ParentB:
    def fun(self):
        print("good morning")
class child(ParentA,ParentB):
    def fun3(self):
        print("mounika")
x=child()
x.fun2()
x.fun2()
x.fun3()
x.fun()
#3multilevel inheritence
class ParentA:
    def fun3(self):
        print("hoi")
    def fun1(self):
        print("hello")
class ParentB(ParentA):
    def fun3(self):
        print("good morning")
class child(ParentB):
    def fun3(self):
        print("mounika")
x=child()
x.fun3()#if method override will return the stmts in child only
x.fun1()
#heirarchical inheritence
class ParentA:
    def fun1(self):
        print("hoi")
    def fun2(self):
        print("hello")
class child1(ParentA):
    def fun3(self):
        print("good morning")
class child2(ParentA):
    def fun3(self):
        print("mounika")
x=child1()
x.fun3()
x.fun1()
x.fun2()
y=child2()
y.fun3()
y.fun1()
x.fun2()'''


class math:
    def __init__(self):
        print("area of the shapes")
class circle(math):
    def __init__(self,r):
        self.r=r
        area=3.14*self.r*self.r
        print("area of circle:",area)
class square(math):
    def __init__(self,r):
        self.r=r
        area=4*self.r
        print("area of square:",area)
class rectangle(math):
    def __init__(self,l,b):
        self.l=l
        self.b=b
        area=l*b
        print("area of rectangle:",area)
x=[math(),circle(4),square(5),rectangle(4,9)]
for i in x:
    i.__init__



















    
