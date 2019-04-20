# This file generates a hierarchical clustering as well as a dendrogram and a
# plot indicating cluster sizes

# Importing the data set 
quantlet <- read.table("C:/Users/Luisa/Desktop/Clustering/quantlet_data.txt", header=T, sep=",")
X <- quantlet[1:2064,2:1287] # removing the first column which contains the file names 
matrix <- as.matrix(X)

# dist generates a distance matrix, by default complete linkage is used
clusters <- hclust(dist(matrix)) 
plot(clusters) # plots the dendrogram
# You can plot a truncated dendrogram like this: 
dend <- as.dendrogram(clusters)
plot(cut(dend, h=6)$upper) # h is the distance you want to trucate at

# print the whole dendrogram as PDF
dend <- as.dendrogram(clusters)
pdf("whole_dendrogram.pdf", width = 40, height = 15)
plot(dend)
dev.off()

# print only truncated dendrogram :
dend <- as.dendrogram(clusters)
pdf("dendrogram_truncated", width = 40, height = 15)
plot(cut(dend, h = 5)$upper)
dev.off()

# creating 10 clusters
clusterCut <- cutree(clusters, k=40)
table(clusterCut)

# Export a plot indicating cluster sizes as PDF 
pdf("40_clusters_hierarchical_obs.pdf", width = 10, height = 4)
barplot(table(clusterCut), main="Hierarchical Clustering 40 clusters ", ylab="Number of observations per cluster", xlab="Cluster")
dev.off()

# Computing average linkage clustering
clusters_average <- hclust(dist(matrix), method = 'average')
dend_average <- as.dendrogram(clusters_average)
# plot(cut(dend,h=6)$upper)
clusterCut_average <- cutree(clusters_average, 40)
table(clusterCut_average)
