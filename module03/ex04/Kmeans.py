import sys
import numpy as np
import matplotlib.pyplot as plt
from random import random

plt.switch_backend('TkAgg') # to avoid "non interactive" Error

def show_data_points(data, centroids_array=None, clusters=None):
	# plt.scatter(data[:, 0], data[:, 1], c='blue', marker='o') #':' means "select all rows", 0 and 1 refer to the columns
	plt.scatter(data[:, 0], data[:, 1], c=clusters, cmap='viridis', marker='o')
	plt.title('Solar System Census')
	plt.xlabel('Height')
	plt.ylabel('Weight')
	if centroids_array is not None and clusters is not None:
		plt.scatter(centroids_array[:, 0], centroids_array[:, 1], c='red', marker='x', s=100) 
	plt.show()

#----------------------------------------------------------------------------

def euclidian_distance(p1,p2):
	return np.sqrt(np.sum((p1-p2)**2))

class KmeansClustering:
	def __init__(self, max_iter=20, ncentroid=5):
		self.ncentroid = ncentroid # number of centroids
		self.max_iter = max_iter # number of max iterations to update the centroids
		self.centroids = [] # values of the centroids
		
	def fit(self, X):
		"""
		Run the K-means clustering algorithm.
		For the location of the initial centroids, random pick ncentroids from the dataset.
		Args:
		-----
			X: has to be an numpy.ndarray, a matrice of dimension m * n.
		Return:
		-------
			None.
		Raises:
		-------
			This function should not raise any Exception.
		"""

		if not isinstance(X, np.ndarray):
			print("Error: numpy array expected")
			return None

		#first time inside this function : randomly assign centroids inside the csv values' bounds
		x_min = X[:, 0].min()
		x_max = X[:, 0].max()
		y_min = X[:, 1].min()
		y_max = X[:, 1].max()

		for i in range(self.ncentroid):
			x = x_min + random() * (x_max - x_min) #pour s'assurer que inside boundaries
			y = y_min + random() * (y_max - y_min)
			self.centroids.append([x, y])
		
		centroids_array = np.array(self.centroids)
		# show_data_points(X, centroids_array)

		for _ in range(self.max_iter):
			clusters = self.predict(X)
			# print(clusters)
			# print()
			new_centroids_list = []
			for _ in range(ncentroid):
				current_cluster_points = X[clusters == i] #on populate cette 
				# variable de tous les points qui ont pour centre ce cluster
				# en comparant l'index de la liste clusters à l'index des points
				if len(current_cluster_points) > 0: #si le cluster n'est pas vide
					new_centroid = np.mean(current_cluster_points[:, 1:3], axis=0)
					new_centroids_list.append(new_centroid)
				else: # si un cluster est vide c'est que le centroid est bcp trop loin des poi9nts donc j'en re-assigne un au hasard
					x = x_min + random() * (x_max - x_min)
					y = y_min + random() * (y_max - y_min)
					new_centroids_list.append(np.array([x, y]))
			self.centroids = new_centroids_list
			centroids_array = np.array(new_centroids_list)
			show_data_points(X, centroids_array, clusters)
			yield self.centroids

		clusters = self.predict(X)
		show_data_points(X, centroids_array, clusters)
		return None


	def predict(self, X):
		"""
		Predict from wich cluster each datapoint belongs to.
		Args:
		-----
			X: has to be an numpy.ndarray, a matrice of dimension m * n.
		Return:
		-------
			the prediction has a numpy.ndarray, a vector of dimension m * 1.
		Raises:
		-------
			This function should not raise any Exception.
		"""

		if not isinstance(X, np.ndarray):
			print("Error: numpy array expected")
			return None

		clusters = []
		for dot in X:
			min_distance = euclidian_distance(dot[1:3], np.array(self.centroids[0])) #j'initialise avec la distance du premier centroide
			closest_centroid_index = 0
			for index, centroid in enumerate(self.centroids):
				distance = euclidian_distance(dot[1:3], centroid) #dot[1:3] --> means only use columns 1 and 2 since column 0 is index and column 4 is bone structure
				if distance < min_distance:
					min_distance = distance
					closest_centroid_index = index
			clusters.append(closest_centroid_index)
			# print(clusters)

		print(clusters)
		return np.array(clusters) # il y a un centroid pour chaque ligne, qui correspond 
		# à chaque point, ce qui me permettra de le représenter sur le graph

#------------------------------------------------------------------------------------

if len(sys.argv) != 4:
	print("Error: 3 parameters expected : filepath, max_iter and ncentroid")
	sys.exit(1)

filepath = sys.argv[1]

try:
	max_iter = int(sys.argv[2])
	ncentroid = int(sys.argv[3])
except ValueError:
	print("Error: max_iter and ncentroid must be integers")
	sys.exit(1)

# try:
# 	file = open("solar_system_census.csv")
# 	if file is not None:
# 		# print(file.read())
		
# 		data = np.loadtxt(file, delimiter=',', skiprows=1) #this line converts file into a numpy array

# 		show_data_points(data)
		
# 		kmc = KmeansClustering(max_iter, ncentroid)
# 		for _ in kmc.fit(data): # '_' : convention en python lorsqu'on utilisera pas cette variable dans la boucle for donc autant ne pas lui donner de nom
# 			pass

# except Exception as e:
# 	print(f"Error: {e}")


try:
		# create random points already in kinf of clusters to check my algorithm
		data = np.random.rand(100, 2)
		data[:30] += 2
		data[30:60] += 3
		data[60:] += 4

		show_data_points(data)
		
		kmc = KmeansClustering(max_iter, ncentroid)
		for _ in kmc.fit(data): # '_' : convention en python lorsqu'on utilisera pas cette variable dans la boucle for donc autant ne pas lui donner de nom
			pass

except Exception as e:
	print(f"Error: {e}")


