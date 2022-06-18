merge = []
def merge_values(dict1,dict2):
	val_key_1 = list(dict1.keys())
	val_key_2 = list(dict2.keys())
	for val1 in val_key_1:
		for val2 in val_key_2:
			#print("{} | {}" .format(val1, val2))
			merge.append("{}|{}" .format(val1,val2))
	return(merge)