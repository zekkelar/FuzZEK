result_compare = dict()

def compares(value,rules):
	for y,x in zip(value,rules):
		result_compare[y] = x
	return result_compare
