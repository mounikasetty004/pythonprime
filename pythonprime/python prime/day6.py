#strong number
'''num=int(input("Enter a number:"))
s=0
temp=num
while num>0:
    rem=num%10
    fact=1
    for i in range(1,rem+1):
        fact=fact*i
    s+=fact
    num=num//10
if (s==temp):
    print(temp,"is strong number")
else:
    print(temp,"is strong number")'''
#armstrong
'''num=int(input("Enter a number:"))
s=0
l=len(str(num))
temp=num
while num>0:
    rem=num%10
    fact=pow(rem,l)
    s+=fact
    num=num//10
if (s==temp):
    print(temp,"is armstrong number")
else:
    print(temp,"is not armstrong number")'''
#
'''num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")'''
