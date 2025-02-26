import math

class TinyStatistician:
	@staticmethod
	def mean(nb_list):
		if not isinstance(nb_list, list) or not nb_list: #"not nb_list" == "nb is empty"
			print("Error")
			return None
		sum = 0
		for nb in nb_list:
			sum += nb
		mean = sum / len(nb_list)
		print(f"Mean : {mean}")
		return mean
	
	@staticmethod
	def median(nb_list):
		if not isinstance(nb_list, list) or not nb_list:
			print("Error")
			return None
		sorted_list = sorted(nb_list)
		index = len(sorted_list) / 2
		# soit index = len(sorted_list) // 2 
		# qui donne direct l'index du milieu (un int). En cas de liste paire, 
		# ça donne l'index supérieur ex: liste de 6 nombres ça va donner le 
		# 4ème et non le 3ème. En cas de liste impaire ça rajoute direct les 
		# 0.5 car ça arrondit à l'int supérieur.
		if len(sorted_list) % 2 == 0:
			index = int(index)
			median = (sorted_list[index - 1] + sorted_list[index]) / 2
			print(sorted_list)
			print(index)
		else:
			index = index + 0.5
			index = int(index)
			median = sorted_list[index - 1]
		print(f"Median : {median}")
		return median
	
	@staticmethod
	def quartile(nb_list):
		if not isinstance(nb_list, list) or not nb_list:
			print("Error")
			return None
		quartile = (0, 0)
		sorted_list = sorted(nb_list)
		q1_index = len(sorted_list) // 4
		q3_index = q1_index * 3
		q1 = sorted_list[q1_index]
		q3 = sorted_list[q3_index]
		print(f"Quartiles : Q1 = {q1}, Q3 = {q3}")
		return (q1, q3) #I could not use tuples during the calculation because tuples 
		# cannot be modified after they are created. They are often used to store 
		# related pieces of data and can contain elements of different data types.
	
	@staticmethod
	def var(nb_list):
		if not isinstance(nb_list, list) or not nb_list:
			print("Error")
			return None
		mean = TinyStatistician.mean(nb_list)
		sum = 0
		for nb in nb_list:
			diff = nb - mean
			squared = diff * diff
			sum += squared
		variance = sum / len(nb_list)
		print(f"Variance : {variance}")
		return variance
	
	@staticmethod
	def std(nb_list):
		if not isinstance(nb_list, list) or not nb_list:
			print("Error")
			return None
		var = TinyStatistician.var(nb_list)
		std = math.sqrt(var)
		print(f"standard deviation : {std}")
		return std


tstat = TinyStatistician()
a = [1, 42, 300, 10, 59]

tstat.mean(a)
tstat.median(a)
b = [1, 42, 300, 400, 10, 59]
tstat.median(b)
tstat.quartile(a)
tstat.var(a)
tstat.std(a)