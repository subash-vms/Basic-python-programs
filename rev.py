rev=0
a=int(input("enter a value: "))
while(a!=0):
    b=a%10;
    rev=rev*10+b
    a=a//10;
print("reverse is: ",rev)
