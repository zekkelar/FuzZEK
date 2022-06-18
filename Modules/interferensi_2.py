import numpy as np
from rich import print
from rich.panel import Panel
result_keys = []
rules_res = []
def parse_rules(result_rules,rules):
	for res in result_rules:
		#print(rules[res])
		rules_res.append(rules[res])

def pisah(key_win):
	for key_winn in key_win:
		get_key = key_winn.split(':')
		#print(get_key[1])
		result_keys.append(get_key[1])


defuzifikasi = []
defuzifikasi2 = []
def gabung():
	for one, two in zip(result_keys,rules_res):
		defuzifikasi.append(((float(one)*float(two))))
	for tri in result_keys:
		convert = float(tri)
		defuzifikasi2.append(convert)

	array1 = np.array(defuzifikasi)
	total = np.sum(array1)
	

	array2 = np.array(defuzifikasi2)
	total2 = np.sum(array2)
	defuz_final(total, total2)

def defuz_final(total1, total2):
	print(Panel.fit("Total : "+str(total1/total2),title="Deffuzifikasi"))

