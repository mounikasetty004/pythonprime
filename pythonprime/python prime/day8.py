#tuples:
#input forms
#basic input:
'''list1=input("enter:").split()
t1=tuple(list1)
print(t1)
#direct input:
t1=(1,"abs",76.098,1,675,[1,2,3,4],(1,2))
print(t1)
print(t1[5][1])
t1[1][2]="d"#'str' object does not support item assignment
print(t1)
#basic operations:
#index
#slicing
#concat
#repetition
#membership
#camparison
#problems:
list1=input("List:" ).split(",")
mytuple=tuple(list1)
print(list1)
print(mytuple)
#2
a=input("data:").split(",")
t=tuple(a)
print(a)
print(t)
index=int(input("index:"))
s=len(t)
if index<=s and index>=-s:
    print("element:",t[index])
else:
    print("invalid index")
#dictionary
#input form1:
d={1:10,2:20,3:30}
print(d.keys())
d1={"a":100,"b":200}
print(d1.values())
d2={"a":100,500:300,"b":200}
print(d2)
#dict sorting
d={1:10,2:20,3:30}
print(d.keys())
print(sorted(d.items()))
for i,j in sorted(d.items()):
    print(i,"->",j)
#updation :works only for values
d={1:10,2:20,3:30}
print(d)
d[2]="hello"#2 is the key
print(d)
#updaton using get()
d={1:189,2:56,3:76}
print(d.get(3))
#deletion
d={1:189,2:56,3:76}
d.pop(2)
print(d)
#dict from two lists
k=input("keys: ").split(",")
v=input("values: ").split(",")
d=dict(zip(k,v))
print(d)
print(sorted(d.items()))
for i,j in sorted(d.items()):
    print(i,"->",j)
#
k=input("keys: ").split(",")
v=input("values: ").split(",")
d={}
for i in range(len(v)):
    d[k[i]]=v[i]
print(d)
print(sorted(d.items()))
#sets:
l1=input("set:").split(",")
s=set(l1)
print(s)
print(sorted(s))
k="a"
s.add(k)
print(sorted(s))
p="7"
s.update(p)
print(sorted(s))
#remove or 
s={1,2,3,4,5}
k=12
s.discard(k)
s.remove(k)
print(sorted(s))
#mathematical operations
#recurssion
#factorial using recursion
def f(n):
    if n==0 or n==1:
        return 1
    else:
        return n*f(n-1)
n=5
print(f(n))
#palindrome:string
def p(s):
    k=len(s)
    if k<=1:
        return 1
    else:
        if s[0]==s[-1]:
            return p(s[1:-1])
        else:
            return 0
s="malayalam"
r=p(s)
if r==0:
    print("not palindrome")
else:
    print("palindrome")
#checking integer number is palindrome or not
def rev(n,r):
    if n==0:
        return r
    else:
        #return int(str(n%10)+str(rev(n//10)))
        return rev(n//10,r*10+n%10)
n=int(input("enter:"))
r=0
r=rev(n,r)
print(r)
if r==n:
    print("palindrome")
else:
    print("not palindrome")'''




























