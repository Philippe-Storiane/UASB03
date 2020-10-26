# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 05:45:35 2020

@author: a179415
"""

import numpy as np
import pandas as pd

from sklearn.cluster import MiniBatchKMeans
#from sklearn.metrics import pairwise_distances_argmin_min

CLUSTER_SIZE = 10
REPRESENTATIVE=10

data1 = pd.read_csv( "embedding00.txt", header=None)
data2 = pd.read_csv( "embedding01.txt", header=None)
data3 = pd.read_csv( "embedding02.txt", header=None)
data4 = pd.read_csv( "embedding03.txt", header=None)

labels1 = data1[ 0 ]
labels2 = data2[ 0 ]
labels3 = data3[ 0 ]
labels4 = data4[ 0 ]

labels = labels1.append( [ labels2, labels3, labels4], ignore_index= True)

embeddings1 = data1.iloc[:, 1:]
embeddings2 = data2.iloc[:, 1:]
embeddings3 = data3.iloc[:, 1:]
embeddings4 = data4.iloc[:, 1:]

np_embeddings1 = embeddings1.to_numpy()
np_embeddings2 = embeddings2.to_numpy()
np_embeddings3 = embeddings3.to_numpy()
np_embeddings4 = embeddings4.to_numpy()

np_embeddings = np.concatenate( (np_embeddings1, np_embeddings2, np_embeddings3, np_embeddings4), axis=0) #, np_embeddings2, np_embeddings3, np_embeddings4))

# use cosine distance by normalizing embeddings
length = np.sqrt( np_embeddings ** 2).sum(axis = 1)[:,None]
np_embeddings = np_embeddings / length

kmeans = MiniBatchKMeans( CLUSTER_SIZE ).fit( np_embeddings )

distances = kmeans.transform( np_embeddings )
for cluster in range(CLUSTER_SIZE):
    distance = distances[:, cluster]
    closest_indices = np.argsort( distance)[: REPRESENTATIVE]
    print( "cluster " + str( cluster))
    for indice in closest_indices:
        print( '%s (%f)' % (labels[ indice] ,distance[ indice]))
    
    
