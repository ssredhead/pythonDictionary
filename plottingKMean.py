import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.cluster import KMeans

iris = datasets.load_iris()

samples = iris.data

# Code Start here:
num_clusters = [1,2,3,4,5,6,7,8]
inertias = []

for num in num_clusters:
  model = KMeans(n_clusters = num)
  model.fit(samples)
  inertias.append(model.inertia_)

plt.plot(num_clusters, inertias, '-o')
plt.xlabel('Number of Clusters(k)')
plt.ylabel('Inertia')

plt.show()