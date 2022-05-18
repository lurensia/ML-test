import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

bream_length = pd.read_csv('bream_length.csv', sep=",", header=None)
bream_weight = pd.read_csv('bream_weight.csv', sep=",", header=None)
smelt_length = pd.read_csv('smelt_length.csv', sep=",", header=None)
smelt_weight = pd.read_csv('smelt_weight.csv', sep=",", header=None)

plt.scatter(bream_length, bream_weight)
plt.scatter(smelt_length, smelt_weight)
plt.xlabel("length")
plt.ylabel("weight")
plt.show()

length = pd.concat([bream_length, smelt_length])
weight = pd.concat([bream_weight, smelt_weight])

print(length)
print(weight)

fish_data = np.column_stack((length, weight))
print(fish_data)

fish_target = [1]*35 + [0]*14
print(fish_target)

train_input, test_input, train_target, test_target = train_test_split(
    fish_data, fish_target)

kn = KNeighborsClassifier()


kn.fit(train_input, train_target)
kn.score(test_input, test_target)

print(train_input.shape)
print(test_input.shape)

plt.scatter(train_input[:, 0], train_input[:, 1])
plt.scatter(test_input[:, 0], test_input[:, 1])
plt.xlabel("length")
plt.ylabel("weight")
plt.show()