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
# create some random matrices
A = np.random.randn(3,4)
B = np.random.randn(4,5)
C = np.random.randn(3,7)

# try some multiplications...
print(np.round( A@B   ,2)), print(' ')
# print(np.round( A@C   ,2)), print(' ')
# print(np.round( B@C   ,2)), print(' ')
print(np.round( C.T@A ,2))

# %% [markdown]
# # Using pytorch

# %%
# create some random matrices
A  = torch.randn(3,4)
B  = torch.randn(4,5)
C1 = np.random.randn(4,7)
C2 = torch.tensor( C1,dtype=torch.float )

# try some multiplications...
# print(np.round( A@B   ,2)), print(' ')
# print(np.round( A@B.T ,2)), print(' ')
print(np.round( A@C1  ,2)), print(' ')
print(np.round( A@C2  ,2))
