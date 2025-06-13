#printing the prime number series within the range
'''import math
a=int(input("a:"))
b=int(input("b:"))
for i in range(a,b+1):
    if(i<=1):
        print("not a prime number")
    else:
        is_prime=(math.factorial(i-1)+1)%i==0
        if is_prime:
            print(i,end=" ")
import math
a=int(input("a:"))
b=int(input("b:"))
for num in range(a,b+1):
    if num>1:
        is_prime=True
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
        print(num)
str="qiscet"
print(len(str))
print(str.capitalize())
print(str.upper())
print(str.lower())
str="i am going"
print(str.title())
print(str.replace('going','went'))
print(str.startswith('i'))
print(str.count('o'))
print(str.find('g'))
print(str.index("n"))

str=" i am going"
print(str[:2])
print(str[2:])
print(str[3:7])
print(str[-1],str[::-2])
print(str[:])
print(str.strip())
print(str.lstrip())
print(str.rstrip())
str=' '
print(str.isspace())
print(str.isalpha())
str='123'
print(str.isdigit())
print(str.isalpha())
print(str.isalnum())


a=5
print(a<<2)
print(a>>2)
x=[1.23,45,6,6,7]
print(type(x))

s="10010"
c=int(s,2)
print("after converting to integer base2:",end=" ")
print(c)
d=float(s)
print(d)

print(chr(1))
print(hex(66))
print(oct(76))
print(ord('M'))'''

#python type conversion using list



















