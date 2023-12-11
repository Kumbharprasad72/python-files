'''
range(): This function generates lisst of numbers in a sequene
 syntax:
       range(start,stop,step)

       start: Initialization
       stop:  condition
       step: increement/ decrement
'''
'''
x=list(range(1,15,1))  #start=1,stop=10, and step=1
print(x)
'''
'''
x=list(range(2,20)) #default step is
print(x)
'''

#No step and start

'''
x=list(range(20)) #default start is 0
print(x)
'''
'''
x=list(range()) #Error as range() require atleast one argument
print(x)
'''
x=list(range(15,5,-2))
print(x)
