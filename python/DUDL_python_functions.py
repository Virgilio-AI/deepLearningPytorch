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
# # VIDEO: Inputs and outputs

# %%
sum([10,20,30])

# %%
alist = [2,3,4]

sum(alist)

# %%
# alist(0)
sum[alist]

# %%
len(alist)

# %%
# give outputs
listsum = sum(alist)
print('The sum is ' + str(listsum))

# %% [markdown]
# ### Exercise

# %%
# compute the average
sum(alist) / len(alist)


# %% [markdown]
# # .
# # .
# # .

# %% [markdown]
# # VIDEO: Python modules (numpy, pandas)
#

# %%
numbers = [1,2,3,4,5]
mean(numbers)
average(numbers)

# %%
import numpy as np

np.mean(numbers)

# %%
np.linspace(1,5,7)

# %%
# clear the workspace

# %%
# new type: numpy array
numbernp = np.array([1,2,3,4,5])

print(numbernp)
print(numbers)

# %%
print(type(numbernp))
print(type(numbers))

# %%
numberz.min()


# %%
n = [4,3,5,2,6,1,7]
print(n)
n.sort()
print(n)

# %%
n = [4,3,5,2,6,1,7]
print(n)
np.sort(n)
print(n)
n = np.sort(n) # notice different variable type; could set back
print(n)

# %%

# %%
import pandas as pd

# create some random data
var1 = np.random.randn(100)*5 + 20
var2 = np.random.randn(100)>0

# variable labels
labels = ['Temp. (C)','Ice cream']

# create as a dictionary
D = {labels[0]:var1, labels[1]:var2}

# import to pandas dataframe
df = pd.DataFrame(data=D)


# %%
df.head()

# %%
df.count()

# %%
df.mean()

# %% [markdown]
# ### Exercise

# %%
# create a pandas dataframe with variables: 
# integers from 0 to 10, their square, and their log

nums = np.array(range(11))

D = {'v1':nums , 'v2':nums**2 , 'v3':np.log(nums)}

df = pd.DataFrame(D)
df

# %%

# %% [markdown]
# # VIDEO: Getting help on functions

# %%
alist = [1,2,3]

sum(alist,10)

# %%
# sum??

# %%
help(sum)

# %%
# advanced method

import inspect
import numpy as np
inspect.getsourcelines(np.linspace)

# %%
sum('test')


# %% [markdown]
# # . 
# # . 
# # . 

# %% [markdown]
# # VIDEO: Creating functions

# %%
def awesomeFunction():
  print(1+1)


# %%
awesomeFunction
awesomeFunction()


# %%
def SuperAwesomeFunction(input1,input2):
  return input1 + input2


# %%
SuperAwesomeFunction(5,8)

# %%
answer = SuperAwesomeFunction(5,8)


# %%
print(answer)


# %%
# with multiple outputs
def awesomeFunction(in1,in2):
  sumres = in1+in2
  prodres = in1*in2
  print('Their sum is ' + str(sumres))
  print('Their product is ' + str(prodres))
  return sumres,prodres


# %%
out1,out2 = awesomeFunction(4,5)

print(out1,out2)

# %%
# lambda functions

littlefun = lambda x : x**2 - 1

littlefun(4)


# %% [markdown]
# ### Exercise

# %%
# create a function that computes a factorial, 
# then compare against the numpy factorial function
# hint: import math

def myfactorial(val):
  return np.prod(np.arange(1,val+1))



# %%
import math

x = 20 # inaccurate for >~21
print(np.arange(1,x+1))

print(myfactorial(x),math.factorial(x))
# math.factorial??


# %%

# %% [markdown]
# # .
# # .
# # .

# %% [markdown]
# # VIDEO: Global and local variable scopes
#
#
#

# %%
# clear the workspace

# %%
def funfun():
  x = 7
  y = 10
  print(x)



# %%
funfun()

# %%
x

# %%
x = 3
print( funfun() )
print( x )
print( y )


# %%
def funfun():
  print(z)



# %%
funfun()

# %%
z = 3
funfun()

# %%
# rules: 
#  1) variables created inside a function are local (accessible only inside the function)
#  2) variables created outside a function are global (accessible in or out of the function)

# %% [markdown]
# ### Exercise

# %%
# write a function that flips a coin N times and reports the average

import numpy as np

def coinflip(N):
  propCoinFlips = np.mean( np.random.randn(N)>0 )
  print( str(N) + ' coin flips had ' + str(propCoinFlips*100) + '% heads.' )


# %%
coinflip(2000)

# %% [markdown]
# # .
# # .
# # .

# %%

# %%

# %% colab={"base_uri": "https://localhost:8080/"} id="sKxUPiYAYwFt" executionInfo={"status": "ok", "timestamp": 1621927521203, "user_tz": -120, "elapsed": 191, "user": {"displayName": "Mike X Cohen", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GhjXSur8ulydyiQQEh2U6pYGIhDN22fqYYNNDg49A=s64", "userId": "13901636194183843661"}} outputId="477bbee3-a671-448d-feac-f49e10603350"
# tangent on copy

a = [4,3]
b = a#[:]
b[0] = 5

print(a)
print(b)

# %% colab={"base_uri": "https://localhost:8080/"} id="VAKNE1LRYwJM" executionInfo={"status": "ok", "timestamp": 1621927528471, "user_tz": -120, "elapsed": 181, "user": {"displayName": "Mike X Cohen", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GhjXSur8ulydyiQQEh2U6pYGIhDN22fqYYNNDg49A=s64", "userId": "13901636194183843661"}} outputId="9153bcb5-4f9c-48e3-e736-ed550e99d805"
print(id(a))
print(id(b))

# %% colab={"base_uri": "https://localhost:8080/"} id="ksnrXeq-ZZmk" executionInfo={"status": "ok", "timestamp": 1621927544212, "user_tz": -120, "elapsed": 180, "user": {"displayName": "Mike X Cohen", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GhjXSur8ulydyiQQEh2U6pYGIhDN22fqYYNNDg49A=s64", "userId": "13901636194183843661"}} outputId="dd957b77-46fe-4a63-8cd6-2a569c975d6d"
import copy

a = {'q':1, 'w':2}
b = copy.deepcopy(a)

print(id(a))
print(id(b))


# %%

# %%

# %%

# %%

# %% [markdown]
# # VIDEO: Classes and object-oriented programming

# %%
# class is like a blueprint for a set of attributes and methods
# instance is an example
# class is a cookie cutter, instance is an individual cookie

class model(object):

  # constructor method
  def __init__(self,numlayers,numunits,name):
    self.layers  = numlayers
    self.units   = numunits # these are attributes
    self.name    = name
    self.weights = 10
  
  # other methods
  def howManyUnits(self):
    totalUnits = self.layers * self.units
    print(f'There are {totalUnits} units in the model.')

  def trainTheModel(self,x):
    self.weights += x
    return self.weights

  def __str__(self):
    return f'This is a {self.name} architecture.'



# %% colab={"base_uri": "https://localhost:8080/", "height": 35} id="5RXhwn5R6HwD" executionInfo={"status": "ok", "timestamp": 1622019930854, "user_tz": -120, "elapsed": 183, "user": {"displayName": "Mike X Cohen", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GhjXSur8ulydyiQQEh2U6pYGIhDN22fqYYNNDg49A=s64", "userId": "13901636194183843661"}} outputId="dae7d41d-f463-4016-fd38-1590e42ec1ca"
# create an instance and check it
ex = model(2,3,'cnn')
# ex.howManyUnits()
str(ex)

# %% colab={"base_uri": "https://localhost:8080/"} id="8zpSRXZL6_kD" executionInfo={"status": "ok", "timestamp": 1622019948704, "user_tz": -120, "elapsed": 180, "user": {"displayName": "Mike X Cohen", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GhjXSur8ulydyiQQEh2U6pYGIhDN22fqYYNNDg49A=s64", "userId": "13901636194183843661"}} outputId="24921e71-a523-42c2-e573-c20247e3e46b"
ex.trainTheModel(3)

# %%
# Exercise: 
# create a new class so that 
# 1) the weights is a layers-by-units matrix, 
# 2) the weights are changed by multiplying by input x and summing input y

# %%
import numpy as np
class model2(object):

  # constructor method
  def __init__(self,numlayers,numunits,name):
    self.layers  = numlayers
    self.units   = numunits # these are attributes
    self.name    = name
    self.weights = np.random.randn(numlayers,self.units)
  
  # other methods
  def howManyUnits(self):
    totalUnits = self.layers * self.units
    print(f'There are {totalUnits} units in the model.')

  def trainTheModel(self,x,y):
    self.weights = self.weights*x + y

  def __str__(self):
    return f'This is a {self.name} architecture.'



# %%
ex1 = model2(2,3,'cnn')
print(ex1.weights)

# %%
ex1.trainTheModel(2,3)

# %%
ex1.weights
