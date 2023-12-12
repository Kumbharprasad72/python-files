'''
String
========
1) String is a collection of characters.
2)They are enclosed in a single qote or double quote or triple quoted.

'''

#x='It vedant'
#x="It vedant=Eclass"
x='''This is a string
multiline string
itvedant eclass learning
string'''

x= "Itvedant-Eclass"

print(x)
#print(type(x))

#n=len(x)
#print("Total number of characters:",n)

#Indexing
'''
Need: To process string character by character,there is need to acess string.
Indexing helps you to access characer in the string

positive Indexing start from 0
negtive Indexing start from -1

there are two types of Indexing:
1) Positive Indexing
2) Negative Indexing

syntax:
     string_Variable[index_number]
'''

'''
print(x[7])
print(x[12])
#print(x[16])# Error=>index out of range
print(x[-11]) 
print(x[-14])
'''

#Slicing:
'''need of Slicing: if there is need to extract partial part of straing from enmtire
straing, then use slicing.
1) to reverse string

syntax:
 string_variable[start:stop:step]
'''

#x1=x[2:8:1]
#x1=x[2:12:2]
#x1=x[2:8:] #default step in slicing is 1
#x1=x[:8:]#Default start is 0
#x1=x[::] # default stop=straing end

'''
slicing with negative index

if step is positive then start=left  end- right
if step is negative then start=left  end-right
'''
x1=x[:2:-1]

print(x1)







