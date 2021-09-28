import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets

iris = datasets.load_iris()

samples = iris.data

x = samples[:,0]
y = samples[:,1]

# Number of clusters
k = 3
# Create x coordinates of k random centroids
centroid_x = np.random.uniform(min(x), max(x), k)
# Create y coordinates of k random centroids
centroid_y = np.random.uniform(min(y), max(y), k)

# Create centroids array
centroids = np.array(list(zip(centroid_x, centroid_y)))
# Make a scatter plot of x, y
plt.scatter(x, y)
# Make a scatter plot of the centroids
plt.scatter(centroid_x, centroid_y)

# Display plot
plt.show()