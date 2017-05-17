def mediana():

	'''Calcula a mediana de uma lista de números'''

	# lista com número par de itens
	x = [6, 4, 8, 2, 5, 1, 3, 2, 9, 7, 5.5, 4, 7, 9, 1, 7, 4, 7, 1, 7]
	x.sort() #ordena a lista
	
	if len(x) % 2 == 0: # caso que a quantidade de itens na lista seja par
		# pega os dois valores centrais (xr, xr+1) e calcula a média deles
		xr = x[(((len(x) + 1) // 2) - 1)]
		xrplusone = x[((len(x) + 1) // 2)]

		return (xr + xrplusone) / 2

	else:	# resolução para o caso ímpar
		return x[(((len(x) + 1) // 2) - 1)]
