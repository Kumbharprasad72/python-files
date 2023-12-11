print("Enter a number")
n=int(input())

a=n%10
b=n//10
c=b%10
d=b//10

sum=a**3+c**3+d**3

if sum==n:
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")
