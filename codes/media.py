def avg():

	'''Calcula a média de uma lista de números'''
	x = [1, 2, 3, 4]
	sum = 0
	for i in range(0, len(x)):
		sum = sum + x[i]
	return sum/len(x)
