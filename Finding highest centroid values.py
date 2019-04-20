# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 14:43:12 2019

@author: Luisa
"""
import numpy as np
from numpy import *
from numpy import linalg
'''
Getting the 5 highest centroids values for each cluster
Input: X is expected to be a numpy matrix 
data is expected to be the term-document data frame as list '''

d = len(X[:,0]) # d dimensions (number of rows)
n = len(X[0,:]) # n observations (number of columns)
  
k=20 # specify the number of clusters
Y = np.random.random((d, k)) # specify the centroid initialization
niter_max = 15 # specify the number of iterations


Energie = np.zeros(niter_max)
for iterations in range(niter_max): 
  labels = np.zeros(n)
  clustersize = np.zeros(k)
  for i in range(n):
    min_distance = np.linalg.norm(X[:,i].astype(np.float64)-Y[:,0].astype(np.float64))
    # boucle calculant les distances de i aux centroides
    for j in range(k):
      squared_distance = np.linalg.norm(X[:,i].astype(np.float64)-Y[:,j].astype(np.float64))
      if squared_distance < min_distance: 
        min_distance = squared_distance
        labels[i]= j
    
    Energie[iterations] = Energie[iterations] + min_distance
    clustersize[int(labels[i])]=clustersize[int(labels[i])]+1
    
  Y = np.zeros((d,k))
  for i in range(n):
    Y[:,int(labels[i])]= Y[:,int(labels[i])] + X[:,i].astype(np.float64)/ clustersize[int(labels[i])]
    
print(labels,Energie,clustersize)



def max(L): # function returning the the higher element of a list and its index
    m=0
    k=0
    for i in range(len(L)):
        if L[i]>m:
            m=L[i]
            k=i
    return(m,k)
    
def top(L): # function returning a list's the elements and its indexes in descending order
    T=[]     
    T2=[]
    L2=copy(L)
    for i in range(5):
        T.append(max(L2)[0])
        T2.append(max(L2)[1])
        L2[max(L2)[1]]=0
    return(T,T2)

# returning the 5 highest centroid values and the corresponding terms
for i in range(k):
    print("Cluster",i,"is represented by:")
    L=top(Y[:,i])[1]
    for s in range(len(L)):
        print(data[0][L[s]+1],"with",top(Y[:,i])[0][s])      