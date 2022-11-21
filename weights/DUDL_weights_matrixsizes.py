# Date: 19/November/2022 - Saturday
# Author: Virgilio Murillo Ochoa
# personal github: Virgilio-AI
# linkedin: https://www.linkedin.com/in/virgilio-murillo-ochoa-b29b59203
# contact: virgiliomurilloochoa1@gmail.com
# web: virgiliomurillo.com

# %%
# import libraries
import torch
import torch.nn as nn

# %% [markdown]
# # Create a model and inspect its weight matrices sizes

# %%
# build a model
aModel = nn.Sequential(
    nn.Linear(10,14),  # input layer
    nn.Linear(14,19),  # hidden layer
    nn.Linear(19,8),   # output layer
      )

aModel

# %%
# print the sizes of the weights matrices in each layer
for i in range(len(aModel)):
  print( aModel[i].weight.shape )

# %% [markdown]
# # Build a model with inconsistent layer shapes

# %%
M2 = nn.Sequential(
    nn.Linear(10,14),  # input layer
    nn.Linear(14,9),   # hidden layer
    nn.Linear(19,8),   # output layer
      )

for i in range(len(M2)):
  print( M2[i].weight.shape )

# %% [markdown]
# # Test both models with fake data

# %%
# generate the data
nsamples = 5
nfeatures = 10

fakedata = torch.randn(nsamples,nfeatures)

# %%
# test the first model

# does the size of the output make sense?
aModel(fakedata).shape

# %%
# test the second model

# does the size of the output make sense?
M2(fakedata).shape

# %%
