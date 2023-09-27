import pandas
import numpy

def youngest_fellah(df, year):
	'''The function returns a dictionary containing the age of the youngest woman and man
who took part in the Olympics on that year. '''

	filtered_df = df[(df.Year == year)]
	filtered_df = filtered_df.sort_values('Age')
	i = 1
	first = 0
	column = 3
	for (i, column) in enumerate(filtered_df):
		if filtered_df.iloc[i, column] == 'F' and first == 0:
			print(i, numpy.asarray(filtered_df[3]))
			first = 1
		if filtered_df.iloc[i, column] == 'M' and first == 0:
			print(i, numpy.asarray(filtered_df[3]))
			first = 1
		i+=1


	#for sex in (df.iloc[i,:] for i in range(df.shape[0])):
	#for i in filtered_df.columns[:2]:
	#for i, rows in filtered_df.columns[:3]:
	#for i, rows in filtered_df.iterrows():
	#for i in filtered_df.iloc[:, 3]: #for i in len(filtered_df)
		# if filtered_df.iloc[i, 3] == 'F' and first == 0:
		# 	print(filtered_df[i, :])
		# 	first = 1
		# if filtered_df.iloc[i, 3] == 'M' and first == 0:
		# 	print(filtered_df[i, :])
		# 	first = 1
		# i+=1

	# #to print column name
	# for name in df.columns[:2]:
	# 	print(df[name]
	# #Similarly to iterate over all the columns in reversed order, we can do:
	# for column in df.columns[::-1]:
	# 	print(df[column])
	# #pour print la premiere ligne de la colonne Name
	# print(df.iloc[1]['Name'])
	# #pour print que a colonne de noms
	# print(df['Name'])
	# #pour filtrer
	# print(df.filter(items=[year], axis=0))
	# filtered_df = df[(df.Sport == "Athletics") & (df.Sex == "M")]


	# for line in df[0]:
	# 	if df['Year'] == year:
	# 		print(df.lock[5])

	# for age in df[0]['Age']:
	# 	youngest_age = df.idxmin()
	# print(youngest_age)


	# filtered_df = df[(df.Year == year)]
	# print(filtered_df.iloc[1:15,1:4])
	# age = 0
	# i = 0
	# while filtered_df[i][4]:
	# 	if int(i) > int(i) + 1:
	# 		age = int(i) + 1
	# 	i+=1
	# print(age)



	# while filtered_df[i]['Sex']:
	# 	if filtered_df[i]['Sex'] == 'F' and first == 0:
	# 		print(filtered_df[i])
	# 		first = 1
	# 	if filtered_df[i]['Sex'] == 'M' and first == 0:
	# 		print(filtered_df[i])
	# 		first = 1
	# 	i+=1




	# for age in filtered_df.loc['Age']:
	# 	if int(age) > int(age) + 1:
	# 		age = int(age) + 1
	# print(age)


	# 	data.iloc

	# 	for year in df[year]
	# 	man --> age
	# 	woman --> age



#iloc : avec numeros, loc avec noms

df = pandas.read_csv('athlete_events.csv')
year = 2000
youngest_fellah(df, year)





#& (df.Sex == "M"

