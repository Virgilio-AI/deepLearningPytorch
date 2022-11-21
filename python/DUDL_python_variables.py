# Date: 19/November/2022 - Saturday
# Author: Virgilio Murillo Ochoa
# personal github: Virgilio-AI
# linkedin: https://www.linkedin.com/in/virgilio-murillo-ochoa-b29b59203
# contact: virgiliomurilloochoa1@gmail.com
# web: virgiliomurillo.com

# %% [markdown]
# # Arithmetic and comments

# %%
4*5

# %%
# a comment!
# 5+4

# %% colab={"base_uri": "https://localhost:8080/"} id="5K9VO-n8W2Vj" executionInfo={"status": "ok", "timestamp": 1621440313932, "user_tz": -120, "elapsed": 473, "user": {"displayName": "Mike X Cohen", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GhjXSur8ulydyiQQEh2U6pYGIhDN22fqYYNNDg49A=s64", "userId": "13901636194183843661"}} outputId="64eb648d-70d1-4ee9-9f12-2e7bf0d635e5"
4*5
4+5

# %%
print( 4*5 )
print( 4+5 )

# %% [markdown]
# # Variables

# %% colab={"base_uri": "https://localhost:8080/"} id="_a2BD83UX-Th" executionInfo={"status": "ok", "timestamp": 1621440523437, "user_tz": -120, "elapsed": 448, "user": {"displayName": "Mike X Cohen", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GhjXSur8ulydyiQQEh2U6pYGIhDN22fqYYNNDg49A=s64", "userId": "13901636194183843661"}} outputId="7c582baa-4343-449e-f16d-a04370a0ace8"
x = 5
y = 4

x*y

# %%
aLongerVariableName = 4
another_naming_style = 5

# %% colab={"base_uri": "https://localhost:8080/", "height": 135} id="cpVVvqzGX-mJ" executionInfo={"status": "error", "timestamp": 1621440622109, "user_tz": -120, "elapsed": 683, "user": {"displayName": "Mike X Cohen", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GhjXSur8ulydyiQQEh2U6pYGIhDN22fqYYNNDg49A=s64", "userId": "13901636194183843661"}} outputId="3047cee1-29b5-4ab2-f3ff-e08a3a598a32"
not a variable = 10

# %% colab={"base_uri": "https://localhost:8080/", "height": 135} id="YN9pM2bnX-ph" executionInfo={"status": "error", "timestamp": 1621440636781, "user_tz": -120, "elapsed": 609, "user": {"displayName": "Mike X Cohen", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GhjXSur8ulydyiQQEh2U6pYGIhDN22fqYYNNDg49A=s64", "userId": "13901636194183843661"}} outputId="8933c733-983e-460f-fd3e-004a52438b59"
also?not%a&variable = 10

# %% colab={"base_uri": "https://localhost:8080/", "height": 135} id="q-TA3giPX-sz" executionInfo={"status": "error", "timestamp": 1621440667107, "user_tz": -120, "elapsed": 689, "user": {"displayName": "Mike X Cohen", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GhjXSur8ulydyiQQEh2U6pYGIhDN22fqYYNNDg49A=s64", "userId": "13901636194183843661"}} outputId="667b3ede-65fc-4b74-eb65-864e2b50ec27"
number2use = 5
4somethingElse = 10

# %% colab={"base_uri": "https://localhost:8080/", "height": 35} id="hdI9nFujX-wG" executionInfo={"status": "ok", "timestamp": 1621440976951, "user_tz": -120, "elapsed": 589, "user": {"displayName": "Mike X Cohen", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GhjXSur8ulydyiQQEh2U6pYGIhDN22fqYYNNDg49A=s64", "userId": "13901636194183843661"}} outputId="b7859835-e254-4b08-b127-f659f4889340"
stringVariable = 'Hello'
stringVariable

# %% colab={"base_uri": "https://localhost:8080/", "height": 35} id="nTKnZMU3adWd" executionInfo={"status": "ok", "timestamp": 1621440981572, "user_tz": -120, "elapsed": 479, "user": {"displayName": "Mike X Cohen", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GhjXSur8ulydyiQQEh2U6pYGIhDN22fqYYNNDg49A=s64", "userId": "13901636194183843661"}} outputId="a2d22139-f695-48e9-e6ce-ad5511f0906d"
stringVariable*2

# %% colab={"base_uri": "https://localhost:8080/", "height": 35} id="2RFf8ZFpX-zf" executionInfo={"status": "ok", "timestamp": 1621441340029, "user_tz": -120, "elapsed": 476, "user": {"displayName": "Mike X Cohen", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GhjXSur8ulydyiQQEh2U6pYGIhDN22fqYYNNDg49A=s64", "userId": "13901636194183843661"}} outputId="45551fd4-a53a-4906-91da-d16c88ae62ef"
firstName = 'mike'
lastName = 'cohen'

firstName + ' ' + lastName

# %% [markdown]
# # Printing mixed variable types

# %% colab={"base_uri": "https://localhost:8080/"} id="wLdF2k-Hb0rj" executionInfo={"status": "ok", "timestamp": 1621442065038, "user_tz": -120, "elapsed": 484, "user": {"displayName": "Mike X Cohen", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GhjXSur8ulydyiQQEh2U6pYGIhDN22fqYYNNDg49A=s64", "userId": "13901636194183843661"}} outputId="222ac180-2005-46e1-c950-435613e00800"
age = 26

print(firstName + ' is ' + str(age) + ' years old.')

# %% colab={"base_uri": "https://localhost:8080/"} id="A85VVZDsb0v2" executionInfo={"status": "ok", "timestamp": 1621442100129, "user_tz": -120, "elapsed": 448, "user": {"displayName": "Mike X Cohen", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GhjXSur8ulydyiQQEh2U6pYGIhDN22fqYYNNDg49A=s64", "userId": "13901636194183843661"}} outputId="752a944a-43c0-4c01-bf40-6171b3761aca"
# using string interpolation
print('%s is %g years old.' %(firstName,age))

# %% colab={"base_uri": "https://localhost:8080/"} id="L4h5pI9PX-2K" executionInfo={"status": "ok", "timestamp": 1621442131599, "user_tz": -120, "elapsed": 502, "user": {"displayName": "Mike X Cohen", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GhjXSur8ulydyiQQEh2U6pYGIhDN22fqYYNNDg49A=s64", "userId": "13901636194183843661"}} outputId="a236f631-d78c-48ea-a0c0-f2c8eca47894"
# using f-strings
print(f'{firstName} is {age} years old.')

# %% [markdown]
# # Lists and indexing

# %% colab={"base_uri": "https://localhost:8080/"} id="PIDmqQqgcIYB" executionInfo={"status": "ok", "timestamp": 1621441488491, "user_tz": -120, "elapsed": 438, "user": {"displayName": "Mike X Cohen", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GhjXSur8ulydyiQQEh2U6pYGIhDN22fqYYNNDg49A=s64", "userId": "13901636194183843661"}} outputId="3aa12a18-139e-4d55-ae8e-dbac58365c22"
alist = [ 5,4,6,10 ]
alist

# %% colab={"base_uri": "https://localhost:8080/"} id="Tdi0c-DYcIa5" executionInfo={"status": "ok", "timestamp": 1621441494740, "user_tz": -120, "elapsed": 463, "user": {"displayName": "Mike X Cohen", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GhjXSur8ulydyiQQEh2U6pYGIhDN22fqYYNNDg49A=s64", "userId": "13901636194183843661"}} outputId="cb717ecd-213f-4b50-9255-ee5304ea9c70"
alist[1]

# %% colab={"base_uri": "https://localhost:8080/"} id="9MjSgw2icIeB" executionInfo={"status": "ok", "timestamp": 1621441498714, "user_tz": -120, "elapsed": 824, "user": {"displayName": "Mike X Cohen", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GhjXSur8ulydyiQQEh2U6pYGIhDN22fqYYNNDg49A=s64", "userId": "13901636194183843661"}} outputId="5f07e9b4-f7a2-4d8d-8d2e-4dd73ba18e3d"
alist[0]

# %% colab={"base_uri": "https://localhost:8080/"} id="i6h0o52jcIg-" executionInfo={"status": "ok", "timestamp": 1621441884331, "user_tz": -120, "elapsed": 452, "user": {"displayName": "Mike X Cohen", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GhjXSur8ulydyiQQEh2U6pYGIhDN22fqYYNNDg49A=s64", "userId": "13901636194183843661"}} outputId="e9d5c1f3-d1bd-41b8-95fb-1729af0344df"
alist[-1]

# %% colab={"base_uri": "https://localhost:8080/"} id="QzQzpdOZd662" executionInfo={"status": "ok", "timestamp": 1621441905172, "user_tz": -120, "elapsed": 467, "user": {"displayName": "Mike X Cohen", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GhjXSur8ulydyiQQEh2U6pYGIhDN22fqYYNNDg49A=s64", "userId": "13901636194183843661"}} outputId="41544a4b-77dc-401c-cd1e-8d39da36e987"
print(alist[2])
alist[:2]

# %% colab={"base_uri": "https://localhost:8080/"} id="MOvSbVHnd8z-" executionInfo={"status": "ok", "timestamp": 1621441986237, "user_tz": -120, "elapsed": 467, "user": {"displayName": "Mike X Cohen", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GhjXSur8ulydyiQQEh2U6pYGIhDN22fqYYNNDg49A=s64", "userId": "13901636194183843661"}} outputId="e2bf0505-aaaf-4061-d0df-e2a3b4d11063"
alist[2:6]

# %%

# %% colab={"base_uri": "https://localhost:8080/"} id="ao3BMKnEX-8E" executionInfo={"status": "ok", "timestamp": 1621444262104, "user_tz": -120, "elapsed": 709, "user": {"displayName": "Mike X Cohen", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GhjXSur8ulydyiQQEh2U6pYGIhDN22fqYYNNDg49A=s64", "userId": "13901636194183843661"}} outputId="ddf19b4f-8f4d-4232-ac5a-15e493058aec"
500/60

