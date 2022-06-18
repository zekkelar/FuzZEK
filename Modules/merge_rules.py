merge_rules=[]

def two(key_rules, value):
	merge_rules.clear()
	count = 0

	#kalau value nya 2 , count2 nya 1
	#kalau value nya 3 , count2 nya 2
	calculate_val = len(value) - 1
	count2 = calculate_val


	#kalau value nya 2 , range nya 2
	#kalau value nya 3 , range nya 3
	for i in range(0,len(value)):
		try:
			for i in range(count, len(key_rules)-count2):
				merge_rules.append(key_rules[i])
			count+=1
			count2 -=1
		except:
			break

	#print(merge_rules)
	return merge_rules
