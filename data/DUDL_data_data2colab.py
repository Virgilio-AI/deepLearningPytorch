# Date: 19/November/2022 - Saturday
# Author: Virgilio Murillo Ochoa
# personal github: Virgilio-AI
# linkedin: https://www.linkedin.com/in/virgilio-murillo-ochoa-b29b59203
# contact: virgiliomurilloochoa1@gmail.com
# web: virgiliomurillo.com

# %%

# %% [markdown]
# # Import from torchvision

# %%
import torchvision

# download the CIFAR10 dataset
cdata = torchvision.datasets.CIFAR10(root='cifar10', download=True)

print(cdata)

# %%
# Datasets that come with torchvision: https://pytorch.org/vision/stable/index.html

# %% [markdown]
# # Download from the web

# %%
import pandas as pd

# url
marriage_url = 'https://www.cdc.gov/nchs/data/dvs/state-marriage-rates-90-95-99-19.xlsx'

# import directly into pandas
data = pd.read_excel(marriage_url,header=5)
data

# %%

# %% [markdown]
# # Upload from hard drive

# %%
from google.colab import files
uploaded = files.upload()

# %%

# %% [markdown]
# # Map your google-drive

# %%
from google.colab import drive
drive.mount('/content/gdrive')

# %%
