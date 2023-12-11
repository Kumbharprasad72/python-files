'''
break keyword:
need of break keyword
======================

Idealy loop stop working when condition become fls.
If there is need to stop loop even if condition is true, then there is need of break
keyword.

break keyword [It has reserved meaning]
============================

break is keyword which is used to stop or terminate loop even if loop condition is true.
break is alwsys associated with if statement in loop i.e breakkeyword does its work
to terminate the loop based on certain condition.

'''

for i in range(1,11,1):

    if i==5:

        break
    print(i)
print("Out of loop")
