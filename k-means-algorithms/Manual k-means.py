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
  # Nous allons stocker l'evolution de l'inertie expliquee au cours de l'algorithme.
  Energie = np.zeros(niter_max)
  for iterations in range(niter_max): 
    # pour chaque point du jeu de donnees, calcul du centroide qui lui est le plus proche le vecteur suivant contiendra en i l'indice du cluster le plus proche du i eme point.
    labels = np.zeros(n)
    # nombre de points assignes a chacun des clusters.
    clustersize = np.zeros(k)
    for i in range(n):
      min_distance = np.linalg.norm(X[:,i].astype(np.float64)-Y[:,0].astype(np.float64))
      # boucle calculant les distances de i aux centroides
      for j in range(k):
        squared_distance = np.linalg.norm(X[:,i].astype(np.float64)-Y[:,j].astype(np.float64))
        if squared_distance < min_distance: 
          min_distance = squared_distance
          labels[i]= j
        
      # increment de la somme des residus
      Energie[iterations] = Energie[iterations] + min_distance
      # decompte des points appartenant au cluster
      clustersize[int(labels[i])]=clustersize[int(labels[i])]+1
    
    # calcul de la moyenne des points
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
