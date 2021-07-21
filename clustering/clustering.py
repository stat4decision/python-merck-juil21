# SOURCE: http://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html#sphx-glr-auto-examples-cluster-plot-cluster-comparison-py
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from sklearn import cluster, datasets
from sklearn.preprocessing import StandardScaler

import seaborn as sns

seed = 8
n_samples = 1500
circles = datasets.make_circles(n_samples=n_samples, factor=.5, noise=.05)
moons = datasets.make_moons(n_samples=n_samples, noise=.05)
blobs = datasets.make_blobs(n_samples=n_samples, random_state=seed)
np.random.seed(seed)
no_structure = np.random.rand(n_samples, 2), None
datasets = [circles, moons, blobs, no_structure]

clustering_names = ["KMeans", "DBSCAN"]






#K means, discussion on K-medoids

#Affinity propagation : avantage, pas besoin de spécifier K, mais large complexité algorithmique O(n^2)
