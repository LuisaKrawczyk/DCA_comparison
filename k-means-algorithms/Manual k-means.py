# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 14:35:33 2019

@author: Luisa
"""
''' Input: X is expected to be a numpy matrix with observations as columns and
variables as rows
'''
### k-means function as an alternative to the one available in sklearn  
import numpy as np
from numpy import *
from numpy import linalg

def my_kmeans(X, Y, niter_max):
  d = len(X[:,0]) # d dimensions (number of rows)
  n = len(X[0,:]) # n observations (number of columns)
  k = len(Y[0,:]) # k clusters/ centroids
  # We will save the error (sum of squares) over the course of the algorithm
  Energie = np.zeros(niter_max)
  for iterations in range(niter_max): 
    # the following labels vector contains for each data point i the cluster that i is closest to
    labels = np.zeros(n)
    # number of data points assigned to each cluster
    clustersize = np.zeros(k)
    for i in range(n):
      min_distance = np.linalg.norm(X[:,i].astype(np.float64)-Y[:,0].astype(np.float64))
      # computing the distance of i to each centroid:
      for j in range(k):
        squared_distance = np.linalg.norm(X[:,i].astype(np.float64)-Y[:,j].astype(np.float64))
        if squared_distance < min_distance: 
          min_distance = squared_distance
          labels[i]= j
        
      # increase of the sum of squares
      Energie[iterations] = Energie[iterations] + min_distance
      
      clustersize[int(labels[i])]=clustersize[int(labels[i])]+1
    
    # computing the new centroids as means/ barycentres
    Y= np.zeros((d,k))
    for i in range(n):
      Y[:,int(labels[i])]= Y[:,int(labels[i])] + X[:,i].astype(np.float64)/ clustersize[int(labels[i])]
    
  return (labels,Energie,clustersize)
'''labels is a vector of length n; for each observation i it indicates 
which centroid it belongs to
Energie is a vector of length niter_max 
Y[:,0] is the centroid for the first cluster, it's a vector of length d
  '''
# I generate a random centroid matrix for initialization
k=20
Y = np.random.random((d, k))
niter_max = 15

# run the algorithm
my_kmeans(X, Y, niter_max)
