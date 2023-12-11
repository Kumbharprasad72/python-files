'''
for loop
=========

sytax: for variable in range(start,stop,step)

              body of loop

variable is counter variable.
'''
n=int(input("Enter a last number:")) #n=15

for i in range(1,10,1):

    print(i)

'''
i  i in [1,2,...,9]  print(i)  step1
i  1 in [1,2,...,9]T  1          2
2  2 in [1,2,...,9]T  2          3
3  3 in [1,2,...,9]T  3          4
.
.
.
10 10 in [1,2,...,9]F
'''
