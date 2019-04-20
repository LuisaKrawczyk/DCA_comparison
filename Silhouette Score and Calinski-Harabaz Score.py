# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 13:36:27 2019

@author: Luisa
"""
'''
Computing Silhouette Scores and Calinski Harabaz Scores for k-means, k-means++, 
Hierchical Ward, Hierarchical Average and Complete Clustering
'''
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.metrics import calinski_harabaz_score
import matplotlib.pyplot as plt
import pandas as pd        
from scipy.cluster.hierarchy import linkage, dendrogram, ClusterNode
from scipy.cluster.hierarchy import fcluster, cophenet
from scipy.spatial.distance import pdist
from pylab import rcParams
import seaborn as sb
import sklearn
from sklearn.cluster import AgglomerativeClustering
import sklearn.metrics as sm
# Input: matrix is supposed to be a term-document matrix
# SILHOUETTE SCORE
score=[]
K= range(3,30)
for k in K:
    clusterer = KMeans (n_clusters=k) #using k-means++ here by default
    preds = clusterer.fit_predict(matrix)
    centers = clusterer.cluster_centers_
    score.append(silhouette_score(matrix, preds, metric='euclidean'))
Z = linkage(matrix, method='complete')
scoreH = []
for k in K:
    Hclustering = AgglomerativeClustering(n_clusters =k, affinity='euclidean',linkage='ward')
    Hclustering.fit(matrix)
    labels = Hclustering.labels_
    scoreH.append(silhouette_score(matrix, labels))
scoreH_complete = []
for k in K: 
    H_complete_clustering = AgglomerativeClustering(n_clusters =k, affinity='euclidean',linkage='complete')
    H_complete_clustering.fit(matrix)
    labels_complete = H_complete_clustering.labels_
    scoreH_complete.append(silhouette_score(matrix, labels_complete))
scoreH_average = []
for k in K: 
    H_average_clustering = AgglomerativeClustering(n_clusters =k, affinity='euclidean',linkage='average')
    H_average_clustering.fit(matrix)
    labels_average = H_average_clustering.labels_
    scoreH_average.append(silhouette_score(matrix, labels_average))
# inluding classical k-means
score_kmeans=[]
for k in K:
    clus_kmeans = KMeans(n_clusters=k, init='random')
    preds_kmeans = clus_kmeans.fit_predict(matrix)
    centers_kmeans = clus_kmeans.cluster_centers_
    score_kmeans.append(silhouette_score(matrix, preds_kmeans, metric='euclidean'))
score_cos=[]
for k in K:
    clus_cos = KMeans(n_clusters=k, distance=nltk.cluster.util.cosine_distance, repeats=25)
    preds_cos = clus_cos.fit_predict(matrix)
    centers_cos = clus_cos.cluster_centers_
    score_cos.append(silhouette_score(matrix, preds_cos, metric='euclidean'))
    
plt.plot(K,scoreH, color='blue', label="Hierarchical Ward")
plt.plot(K,score, color='red', linestyle='dotted', label="k-means++")
plt.plot(K,scoreH_complete, color='blue', label="Hierarchical Complete", linestyle='dashed')
plt.plot(K, scoreH_average, color='blue', linestyle='dotted', label="Hierarchical Average")
plt.plot(K, score_kmeans, color='red', label='classical k-means')
plt.xlabel('Number of Clusters')
plt.ylabel('Silhouette Score')
plt.legend()
plt.savefig('SilhouetteScore.png', format='png', dpi=800)


# CALINSKI HARABAZ SCORE 

score_CH = []
for k in K:
    clusterer = KMeans (n_clusters=k) # k-means++
    preds = clusterer.fit_predict(matrix)
    centers = clusterer.cluster_centers_
    score_CH.append(calinski_harabaz_score(matrix, preds))
score_kmeans_CH=[]
for k in K:
    clus_kmeans = KMeans(n_clusters=k, init='random') #classical k-means
    preds_kmeans = clus_kmeans.fit_predict(matrix)
    centers_kmeans = clus_kmeans.cluster_centers_
    score_kmeans_CH.append(calinski_harabaz_score(matrix, preds_kmeans)) 
scoreH_CH = []
for k in K:
    Hclustering = AgglomerativeClustering(n_clusters =k, affinity='euclidean',linkage='ward')
    Hclustering.fit(matrix)
    labels = Hclustering.labels_
    scoreH_CH.append(calinski_harabaz_score(matrix, labels))
scoreH_complete_CH = []
for k in K: 
    H_complete_clustering = AgglomerativeClustering(n_clusters =k, affinity='euclidean',linkage='complete')
    H_complete_clustering.fit(matrix)
    labels_complete = H_complete_clustering.labels_
    scoreH_complete_CH.append(calinski_harabaz_score(matrix, labels_complete))
scoreH_average_CH = []
for k in K: 
    H_average_clustering = AgglomerativeClustering(n_clusters =k, affinity='euclidean',linkage='average')
    H_average_clustering.fit(matrix)
    labels_average = H_average_clustering.labels_
    scoreH_average_CH.append(calinski_harabaz_score(matrix, labels_average))

plt.plot(K,scoreH_CH, color='blue', label="Hierarchical Ward")
plt.plot(K,score_CH, color='red', label="k-Means++", linestyle='dotted')
plt.plot(K,scoreH_complete_CH, color='blue', label="Hierarchical Complete", linestyle='dashed')
plt.plot(K, scoreH_average_CH, color='blue', linestyle='dotted', label="Hierarchical Average")
plt.plot(K, score_kmeans_CH, color='red', label="k-means")
plt.xlabel('Number of Clusters')
plt.ylabel('Calinski Harabaz Score')
plt.legend()
plt.savefig('CalinskiHarabazScore.png', format='png', dpi=800)
