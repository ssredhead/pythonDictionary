import codecademylib3_seaborn
from sklearn.linear_model import Perceptron
import matplotlib.pyplot as plt
import numpy as np
from itertools import product

#inputs to AND gate
data = [[0, 0], [0, 1], [1, 0], [1, 1]]
#labels (data anded together)
labels = [0, 0, 0, 1]

#plot x values, y values, and labels
plt.scatter([point[0] for point in data], [point[1] for point in data], c = labels)
# plt.show()

#build Perceptron to learn AND
classifier = Perceptron(max_iter = 40)

#train model
classifier.fit(data, labels)
print(classifier.score(data, labels))

#Visualize decision boundary
#decision bondary is the line determining whether the output should be 1 or 0 depending on what side of the line it lands on
x_values = np.linspace(0, 1, 100)
y_values = np.linspace(0, 1, 100)
#find each combination of x and y values
point_grid = list(product(x_values, y_values))

distances = classifier.decision_function(point_grid)

abs_distance = [abs(pt) for pt in distances]

#turn list into a 100 x 100 grid
distances_matrix = np.reshape(abs_distance, (100, 100))

#draw heat map
heatmap = plt.pcolormesh(x_values, y_values, distances_matrix)

plt.colorbar(heatmap)
plt.show()
