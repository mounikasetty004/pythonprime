#counting the string characters
'''a=input("str:")
b=a.upper()
l1=[]
for i in b:
    if i not in l1:
        print(i,b.count(i)) 
        l1.append(i)'''#we append the values to the list to stop the same char itreration
#
'''a=input("str: ")
n=int(input("num: "))
l=len(a)
if n>=0 and n<l:
    #print(a[:n]+a[n+1:])
    print(a.replace(a[n],""))
else:
    print("only positive values ane taken") '''
#probles on list
#indexing
#indirect input of list
#1.split method 
'''s=input("enter:")
print(s)
l=s.split(" ")
print(l)
print(type(l))
s=input("enter: ").split()
print(s)
#l1=[]
for i in range(len(s)):
    s[i]=int(s[i])
print(s)'''
#2.using length of list
'''n=int(input("enter:"))
l1=[]
for i in range(n):
    a=int(input("enter:"))
    l1.append(a)
print(l1)'''
#3.comprehension contains 4 steps:assigning,loop,condition(optional),expresstion
#syntax: variable=[expression loop condition (optional)]

'''l1=[int(input("enter:")) for i in range(1,4)]
print(l1)
#s="bottel"
s="12345"
l1=[int(i) for i in s]
print(l1)
s=input("enter:").split(" ")
l1=[int(i) for i in input("enter:").split('')]
print(l1)

l=["even" if int(i)%2==0 else "odd" for i in input("enter:").split(" ")]
print(l)'''
#4.using map function
#sytax:variable=datatype(map(expression,input())
#it is used for multiple values
'''l1=map(i,for i in input("enter:"))
print(l1)
l1=map(i,for i in input("enter:")) 
print(l1)
l1=list(map(int,input("enter:").split(" ")))
print(l1)


l1=set(map(str,input("enter:").split(" ")))
print(l1)
a,b,c=set(map(str,input("enter:").split(" ")))
print(a)
print(b)
print(c)


l1=[1,2,3,4,5]
l2=[6,4,3,2,1]
print(5 in l1)
print(9 not in l1)
print(l1+l2)
print(l1*7)
l3=[2,3,4,5,[9,0]]
print(l3[4][0])
print(l1==l2)
print(l1!=l2)
print(l1*len(l2)+l3)
print(l1 not in l2)
l4=["good morning",["python", "class"]]
print(l1[0])
print(l4[1][1])
print(l4[1][1][0])
#update
l1=["good morning",["python", "class"]]
print(l1)
l1[1][1]="hi"
print(l1)
l1[1][0]="java"
print(l1)'''
#methosd in list
'''l1=[1,2,3,4,5,6]
print(l1.index(3))
l1.append([12,23,24])
print(l1)
l1.extend([12,23,24])
print(l1)
l1.insert(1,23)
print(l1)
l1.remove(12)#removes values
print(l1)
l1.pop(0)
print(l1)
l1=['1','2','3','4','5','6']
l1.sort(key=None ,reverse=True)
print(l1)

l1=[int(i) for i in input("enter l1 elements: ").split()]
l2=[int(i) for i in input("enter l2 elements: ").split()]
l3=[]
if len(l1)!=len(l2):
    print("please enter the list same size")
else:
    for i in range(len(l1)):
        x=abs(l1[i]-l2[i])
        l3.append(x)
    print(l3)
'''
#functions
#block of code designed to perform specific task
#syntax: def  functionname(parameters):
#              stmts
#        fuctioncall(arguments)
#simple function
#firstdway
'''def wish():
    print("hello")
def w():
    print("good")
print("hi")
wish()'''
#secondway
'''def fun1():
    return "hi"
print(fun1())'''
#exampple
'''def hello():
    print("good morning")
    print("hello")
    print("hi")
def hii():
    return "c","python","java"
hello()
hii()
print(hii())'''
#doc string
'''def sum():
    """function is for addition of two values"""
    p,q=10,23
    print(p+q)
sum()
print(sum.__doc__)
#ARGUMENTS AND PARAMETERS
def sum(a,b):
    print(a+b)
def sub(d,c):
    print(d-c)
def mul(a,b):
    print(a*b)
a=int(input("enter a value"))
b=int(input("enter b value"))
c=int(input("enter c value"))
d=int(input("enter c value"))
#positional arguments
sum(a,b)
sub(c,d)
mul(a,b)
#keyword arguments
sub(d=a,c=b)
sub(c=b,d=a)

def sum(ba=100):
    print(a-b)
a=int(input("enter a value"))
b=int(input("enter b value"))
def fun1(m="opadma",a=10):
    print(m,a)
fun1("mounika",20)
fun1()
fun1("keerthi")
fun1(a=25)'''
#sum of natural nums
'''def addn(a,b):
    s=0
    for i in range(a,b):
        s+=i
    print("sum: ",s)
addn(1,100)
#factorial
def fact(n):
    for i in range(1,n):
        n=n*i
    return n#fruitful functions
print(fact(5))'''
#anonymous functions:nameless o lamdaa functions
#syntax:lamda arguments:expr
k=lambda a,b,c:a+b,a
a,b,c=1,2,3
print(k(a,b,c))





















