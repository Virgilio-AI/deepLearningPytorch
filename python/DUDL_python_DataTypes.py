# Date: 19/November/2022 - Saturday
# Author: Virgilio Murillo Ochoa
# personal github: Virgilio-AI
# linkedin: https://www.linkedin.com/in/virgilio-murillo-ochoa-b29b59203
# contact: virgiliomurilloochoa1@gmail.com
# web: virgiliomurillo.com

# %% [markdown]
# # .
# # .
# # .

# %% [markdown]
# # VIDEO: Variables

# %%
# This is a comment. Python will ignore this text.


# %%
a = 4
b = 3

# %%
a

# %%
a
b

# %%
print(a) # comments after a line
print(b)

# %%
c = 7
d = 7.0

print(c,d)

# %%
type(c)
type(d)

# %%
c = 'hello'
d = "Hey there!"


# %%
# define variables and parameters
aVariable    = 10
filterOrder  = 2048
user_name    = 'mike'
param4modelA = 42.42

not!allowed = 3
also#not = 3
^nope! = 3

# variable naming rule: no non-alphanumeric characters except _
# variables may contain numbers but not start with them


# %%
# %whos

# %%
# multiple assignment
varA,varB = 3,'test'

print(varA)
print(varB)

# %% [markdown]
# ### Exercise:

# %%
# discover whether it's possible in Python to over-write variables:
#  1) within-type (e.g., numeric to a different number)
#  2) across-type (e.g., numeric to a string)

# %% [markdown]
# # .
# # .
# # .

# %% [markdown]
# # VIDEO: Math operators

# %%
# let's start by creating some variables
x = 7
y = 4.1
z = 0

# %%
# Addition and subtraction

print( x-7 )

c = y + x - 2

# %%
# multiplication and division
print( x*y ) # note: floating-point algebra is not the same thing as "real" algebra
4/3
4\
  +3

# %%
# powers
2**3

# %%
print( 9**1/2 )

# therefore, use parentheses to overwrite order of operations
print( 9**(1/2) )

# %%
# can we "add" strings??
firstName = 'Mike'
lastName  = 'Cohen'

print( firstName + lastName )
print( firstName + ' ' + lastName )

# %%
# just curious...
firstName - lastName

# %%
firstName * 3

# %%
# printing mixed variable types
print( '7 times 4.1 equals 28.7' )

print( x ' times ' y ' equals ' x*y )
print( x + ' times ' + y + ' equals ' + x*y )

# %%
print( str(x) + ' times ' + str(y) + ' equals ' + str(x*y) )

# %%
# inputting data from the user
ans = input('Feed me a stray cat ')
print(ans)
print(type(ans))

# %%
ans*10



# %%
numans = input( 'Input a number: ' )
numans = float(numans)

type(numans)

# %% [markdown]
# ### Exercise

# %%
# The goal is to apply the Pythagorean theorem.
#  Input from the user two lengths, and you return the third length
side1 = int( input('Length of side a: ') )
side2 = int( input('Length of side b: ') )

thirdside = (side1**2 + side2**2)**(1/2)

print(' ')
print( 'The length of side c is ' + str( thirdside ) )

# %% [markdown]
# # .
# # .
# # .

# %% [markdown]
# # VIDEO: Lists

# %%
aList = [0,1,2,3,4,5]

aList

# %%
strList = [ 'hi','my','name','is','Mike' ]
strList

# %%
mixList = [ 3,'three',4,'four' ]
mixList

# %%
listList = [ 3,['3','4','5'],5,[4,5,6] ]
listList

# %%
listList = [ 
            3,              # a number
            ['3','h','5'],  # a list of strings
            5,              # another number
            [4,5,6]         # a list of numbers
           ]

listList

# %%
# test whether an item is in a list
4 in aList

# %%
print( 4 in aList )

print( 14 in aList )
print( 14 not in aList )

# %%
aList + strList

# %%
aList*3


# %%
newlist = [4,3,4,5,6,7,7,7,7]

set(newlist)

# %%
## some list methods 

# show the original
print(aList)

# add a new element
aList.append(-100)
print(aList)

# sort
aList.sort()
print(aList)

# %% [markdown]
# ### Exercise

# %%
# Use a list method to find the number of 7's in newlist
newlist.count(7)

# %% [markdown]
# # .
# # .
# # .

# %% [markdown]
# # VIDEO: Lists part 2

# %%
# append, insert, remove, del, sort

lst = [1,2,3,4,5]

print(lst)
lst.append(7)
print(lst)


# %%
lst.insert(2,20)
print(lst)

# %%
lst.append(3)
print(lst)
lst.remove(3)
print(lst)

# %%
print(lst)

lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)

# %%
lst.append('hi')
lst.sort()

# %% [markdown]
# # VIDEO: Tuples

# %%
atuple = ( 3,'4',3 )

atuple*3

# %%
atuple.count(3)

# %%
alist = list(atuple)

print(atuple)
print(alist)

# %%
# tuples are immutable
atuple[0] = 5

# %%
# lists are mutable
alist[0] = 5
alist

# %% [markdown]
# # .
# # .
# # .

# %% [markdown]
# # VIDEO: Booleans

# %%
boolTrue = True
booltrue = 'true'

# %whos

# %%
# comparisons
4 == 4

# %%
4>5

# %%
4>4

# %%
4>=4

# %%
4 != 5

# %%
a = 8
b = 4

outcome = a == b*2
print(outcome)

# %%
# conjunctive comparisons
14>5 and 7<10


# %%
14>5 or 7>10

# %%
# converting to boolean
print( bool(0) )
print( bool(10) )

print(' ')

print( bool('asdf') )
print( bool(' ') )
print( bool('') )

# %% [markdown]
# ### Exercise

# %%
# Ask users to input Pythagorean triplet, check whether it's real


# %%
print("Let's test your knowledge of Pythagorean triples!")

sidea = float(input('Input length of side a: '))
sideb = float(input('Input length of side b: '))
sidec = float(input('Input length of side c: '))

# check
isPythTriplet = sidea**2 + sideb**2 == sidec**2

print('Your answer is ' + str(isPythTriplet) '!!')


# %% [markdown]
# # .
# # .
# # .

# %% [markdown]
# # VIDEO: Dictionaries

# %%
D = dict()
D

# %%
D['name'] = 'Mike' # key/value pairs
D['AgeRange'] = [20,50]

D

# %%
D = {'name':'Mike' , 'AgeRange':[20,50]}

D

# %%
# retrieve one item
D['name']

# %%
# list all properties
D.keys()

# %%
# test whether a key is in the dictionary
'name' in D

# %%
'Mike' in D

# %%
'Mike' not in D

# %%
D.values()

# %%
D.items()

# %% [markdown]
# ### Exercise

# %%
# Input two numbers from the user. 
# Create a dictionary with keys 'firstNum', 'secondNum', and 'product'

# %%
del D
D = dict()

num1 = float(input('Give me a number '))
D['FirstNum'] = num1

num2 = float(input('Give me another number '))
D['SecondNum'] = num2

D['Product'] = num1*num2

D.items()

# %%
