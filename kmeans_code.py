# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 05:45:35 2020

@author: a179415
"""

import numpy as np
import pandas as pd

from sklearn.cluster import MiniBatchKMeans
from sklearn.metrics import pairwise_distances_argmin_min


data1 = pd.read_csv( "embedding00.txt", header=None)
data2 = pd.read_csv( "embedding01.txt", header=None)
data3 = pd.read_csv( "embedding02.txt", header=None)
data4 = pd.read_csv( "embedding03.txt", header=None)

labels1 = data1[ 0 ]
labels2 = data2[ 0 ]
labels3 = data3[ 0 ]
labels4 = data4[ 0 ]

embeddings1 = data1.iloc[:, 1:]
embeddings2 = data2.iloc[:, 1:]
embeddings3 = data3.iloc[:, 1:]
embeddings4 = data4.iloc[:, 1:]

np_embeddings1 = embeddings1.to_numpy()
np_embeddings2 = embeddings2.to_numpy()
np_embeddings3 = embeddings3.to_numpy()
np_embeddings4 = embeddings4.to_numpy()

np_embeddings = np.concatenate( (np_embeddings1)) #, np_embeddings2, np_embeddings3, np_embeddings4))

kmeans = MiniBatchKMeans( 10 ).fit( np_embeddings )

close = pairwise_distances_argmin_min(kmeans.cluster_centers_, x, metric='euclidean')
index_closest_points = close[0]
distance_closest_points = close[1]

for i in range(0, K):
    print("The closest word to the centroid of class {0} is {1}, the distance is {2}".format(i, labels[index_closest_points[i]], distance_closest_points[i]))






