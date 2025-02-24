""" 
	ZIP METHOD :

	list1 = [1, 2, 3]
	list2 = ['a', 'b', 'c']
	zipped = zip(list1, list2)
	print(list(zipped))
	
	Output: [(1, 'a'), (2, 'b'), (3, 'c')]

	ENUMERATE METHOD:

	enumerate(iterable, start=0)
	list1 = ['a', 'b', 'c']
	enumerated = enumerate(list1)
	print(list(enumerated))
	
	Output: [(0, 'a'), (1, 'b'), (2, 'c')]

	# With a different starting index
	enumerated = enumerate(list1, start=1)
	print(list(enumerated))
	
	Output: [(1, 'a'), (2, 'b'), (3, 'c')]
 """

import sys

class Evaluator():
	@staticmethod #static methods/functions are not used to modify the class or an instance
	def zip_evaluate(coefs, words):
		if len(coefs) != len(words):
			print(-1)
			sys.exit(1)
		iterator = zip(coefs, words)
		sum = 0
		for i in iterator:
			sum = sum + (i[0] * len(i[1]))
		print(sum)
	@staticmethod
	def enumerate_evaluate(words):
		iterator = enumerate(words) #idem que , enumerate(words, start=0)
		sum = 0
		for i, word in iterator:
			sum = sum + (coefs[i] * len(word))
		print(sum)


#------------------------------------------------------

try:
	words = ["Le", "Lorem", "Ipsum", "est", "simple"]
	coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
	Evaluator.zip_evaluate(coefs, words)
	Evaluator.enumerate_evaluate(words)

	words = ["Le", "Lorem", "Ipsum", "est", "simple"]
	coefs = [1.0, 2.0]
	Evaluator.zip_evaluate(coefs, words)
	Evaluator.enumerate_evaluate(words)
except Exception as e:
	print(f"Error: {e}")




