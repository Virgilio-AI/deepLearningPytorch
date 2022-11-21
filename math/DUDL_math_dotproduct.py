# Date: 19/November/2022 - Saturday
# Author: Virgilio Murillo Ochoa
# personal github: Virgilio-AI
# linkedin: https://www.linkedin.com/in/virgilio-murillo-ochoa-b29b59203
# contact: virgiliomurilloochoa1@gmail.com
# web: virgiliomurillo.com

# %%
# import libraries
import numpy as np
import torch

# %% [markdown]
# # Using numpy

# %%
# create a vector
nv1 = np.array([1,2,3,4])
nv2 = np.array([0,1,0,-1])

# dot product via function
print(np.dot(nv1,nv2))

# dot product via computation
print(np.sum( nv1*nv2 ))

# %% [markdown]
# # Using pytorch

# %%
# create a vector
tv1 = torch.tensor([1,2,3,4])
tv2 = torch.tensor([0,1,0,-1])

# dot product via function
print(torch.dot(tv1,tv2))

# dot product via computation
print(torch.sum( tv1*tv2 ))
