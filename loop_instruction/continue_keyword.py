'''
NEED
if there is need to skip execution of the code for a particular iteration in a loop then we can use continue
statement to achieve it.e.g
print Hello world for all iteration in loop except forth iteration
'''

'''
continue:
It is keyword
it is also associated with if condition.
when continue keyword is executed or encountered, loop control goes to
increment/decrement step skipping code for execution after continue keyword
'''

for i in range(1,11,1):
    
    if i==4:
        
        continue
    print(i,"-Hello World")
