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
# # VIDEO: Indexing

# %%
arange = range(5)

arange

# %%
alist = list(arange)
alist

# %%
alist[1]

# %%
alist = [5,4,1,-67,343,34]

alist[1]

# %%
print( alist[5] )

print( alist[-1] )
print( alist[-2] )

# %%
# can also use variables
idx = 3
alist[idx]

# %%
idxs = [4,2]
alist[idxs]


# %%
alist = [ 4,3,[4,3,5] ]

alist[2][1]

# %% [markdown]
# ### Exercise

# %%
# Get the attribute of Penguin in the following list
listlist = [ 4,'hi',[5,4,3],'yo',{'Squirrel':'cute','Penguin':'Yummy'} ]

# %%

listlist[4]['Penguin']

# %% [markdown]
# # .
# # .
# # .

# %% [markdown]
# # VIDEO: Slicing, part 1

# %%
alist = list( range(5,11) )
alist

# %%
print( alist[0:2] )
print( alist[0:1] )

# %%
alist[2:5]

# %%
alist[2:]

# %%
alist[:4]

# %%
alist[::2]

# %%
# using variables
start = 1
stop  = 4
skip  = 2

alist[start:stop:skip]

# %%
# to reverse a list
alist[::-1]

# %% [markdown]
# ### Exercise

# %%
# use slicing to write "Mike is a nice guy" from this text
text = '345dfyug ecin a si ekiM 93845d'

text[-8:4:-1]

# %% [markdown]
# # .
# # .
# # .

# %%
# Broadcasting
