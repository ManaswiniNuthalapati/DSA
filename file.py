# Check for Leap Year
year=2025
if year%400==0 or (year%4==0 and year%100!=0):
    print("Leap Year")
else:
    print("NOt")
    
# Fibonacci Sequence
n=5
a,b=0,1
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c

# Prime Number Check
n=11
if n<=1:
    print("Not a Prime Number")
else:
    for i in range(2,n):
        if n%i==0:
            print("Not Prime Number")
            break
    else:
        print("Prime Number")

# Find Maximum and Minimum in an Array
arr=[]

