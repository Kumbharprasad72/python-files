'''
prime number
=============

A number which is completely divisible by 1 and itself is calld as prime number.

7 is prime number=> 7 is completely divisible by 1 and 7

8 is also completely divisible by 1 and 8, but 8 is non prime number.

n=7
    1   23456    7
        ------
    excluding 1 and 7 check whether any number completelyt divides 7 , so none
    of in between number given by user, then that number is non prime number
     if no one completely divide that number then it is called as prime number.

conclusion:
excluding 1 qnd last number, if any one number completely divides that number given by user, then that number is
non prime number
if no one compeletely divide that number it is called as prime number.
'''

n=int(input("Enter a number:"))

for i in range(2,n,1):
    r=n%i

    if r==0:
        print(n,"is non-prime number")
        break
else:
    print("It is prime number")
    
