import numpy as np
from sklearn.cluster import KMeans

data_input = input("enter numbers seperated by space or comma:").replace(","," ").split()
data = np.array(list(map(float,data_input))).reshape(-1,1)

k = int(input("Enter number of cluster: "))

model = KMeans(n_clusters=k, random_state=0, n_init=10).fit(data)

clusters = [[] for _ in range(k)]
for num, label in zip(data.flatten(), model.labels_):
    clusters[label].append(float(num))
    
print("clusters:", clusters)
print("Centroids:", [float(c) for c in model.cluster_centers_.flatten()])
