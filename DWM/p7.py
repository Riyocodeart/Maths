import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.datasets import load_iris

X = load_iris().data
Z = linkage(X, method='ward')
plt.figure(figsize=(10,5))
dendrogram(Z,truncate_mode='level',p=3)
plt.title('Hierarchical clustering denfrogram')
plt.xlabel('Sample index or cluster size')
plt.ylabel('Distance')
plt.show()