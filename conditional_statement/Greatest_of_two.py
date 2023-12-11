'''
CONDITIONAL STATEMENT-----

NEED OF CONDITIONAL STATMENT:

In a program, Thre is need to take decision based on certain condition, then there
is need of onditional statment.

WHAT IS CONDITIONAL STATEMENT---

The Statement or instruction which help to give decision based on certain condition
in a program are called as conditional statement.

TYPES OF CONDITIONAL STATEMENT:

1) IF STATEMENT
2) IF ELSE STATEMENT
3) NESTED IF ELSE
4)LOGICAL OPEARATOR
5) elif

'''
#Two numbers entered by user. WAP to greatest of two numbers.

print("Enter a number:")
a=int(input())

print("Enter a number:")
b=int(input())

if a>b:
    print("In if block")
    print("Greatest is:",a)
else:
    print("In else block")
    print("Grestest is :",b)
