'''
Greatest of Three using Logical Operator
'''

a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))

'''
if a>b and a>c:
    print(a,"is Greater")

if b>c and b>a:
    print(b,"is Greater")
if c>a and c>b:
    print(c,"is Greater")
'''

'''
if a>b and a.c:
    print(a,"is greater")
else:
    if b>a and b>c:
        print(b,"is greater")
    else:
        if c>a and c>b:
            print(c,"is greater")
'''

#elif-> elseif

if a>b and a>c:
    print(a,"is greater")
elif b>a and b>c:
    print(b,"is Greater")
elif c>a and c>b:
    print(c,"is Greater")
