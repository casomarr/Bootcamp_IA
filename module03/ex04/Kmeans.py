import sys
import numpy as np
import matplotlib.pyplot as plt
from random import random

plt.switch_backend('TkAgg') # to avoid "non interactive" Error

def show_data_points(data, centroids_array):
	plt.scatter(data[:, 0], data[:, 1], c='blue', marker='o') #':' means "select all rows", 0 and 1 refer to the columns
	plt.title('Solar System Census')
	plt.xlabel('Height')
	plt.ylabel('Weight')
	if centroids_array is not None:
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
		# print(f"centroids: {self.centroids}")
		
		centroids_array = np.array(self.centroids)
		# show_data_points(X, centroids_array)


		# iter = 0
		# while iter < self.max_iter:
		for _ in range(self.max_iter):
			# i = 0
			# self.centroids.clear()
			clusters = self.predict(X)
			new_centroids_list = []
			# while i < self.ncentroid:
			for _ in range(ncentroid):
				current_cluster_points = X[clusters == i] #on populate cette 
				# variable de tous les points qui ont pour centre ce cluster
				# en comparant l'index de la liste clusters à l'index des points
				print(f"Current cluster points: {current_cluster_points}")
				if len(current_cluster_points) > 0: #si le cluster n'est pas vide
					print("cluster non vide")
					new_centroid = np.mean(current_cluster_points, axis=0)
					new_centroids_list.append(new_centroid)
				else: # si un cluster est vide c'est que le centroid est bcp trop loin des poi9nts donc j'en re-assigne un au hasard
					x = x_min + random() * (x_max - x_min)
					y = y_min + random() * (y_max - y_min)
					new_centroids_list.append(np.array([x, y]))
					print("cluster vide")
					# self.centroids.append(self.centroids[i]) #dans ce cas ne pas .clear() avant
				# i += 1
			self.centroids = new_centroids_list
			centroids_array = np.array(new_centroids_list)
			# show_data_points(X, centroids_array)
			yield self.centroids
			# iter += 1

		show_data_points(X, centroids_array)
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
			# min_distance = float('inf') #on initialise à une valeur très grande
			print(f"dot: {dot.shape}")
			print(f"centroid: {np.array(self.centroids).shape}")
			min_distance = euclidian_distance(dot[1:3], np.array(self.centroids[0])) #j'initialise avec la distance du premier centroide
			print(f"min_distance: {min_distance}")
			closest_centroid_index = -1
			for index, centroid in enumerate(self.centroids):
				distance = euclidian_distance(dot[1:3], centroid) #dot[1:3] --> means only use columns 1 and 2 since column 0 is index and column 4 is bone structure
				print(f"distance: {distance}")
				if distance < min_distance:
					min_distance = distance
					closest_centroid_index = index
			clusters.append(closest_centroid_index)
		print(f"clusters: {clusters}")
		
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

try:
	file = open("solar_system_census.csv")
	if file is not None:
		# print(file.read())

	#To visualize the file's data points
		data = np.loadtxt(file, delimiter=',', skiprows=1) #this line converts file into a numpy array
		# print(type(data))
		
		# show_data_points(data, None)


		kmc = KmeansClustering(max_iter, ncentroid)
		for _ in kmc.fit(data): # '_' : convention en python lorsqu'on utilisera pas cette variable dans la boucle for donc autant ne pas lui donner de nom
			pass

except Exception as e:
	print(f"Error: {e}")


