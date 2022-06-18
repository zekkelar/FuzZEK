import numpy as np
from rich import print
import pandas as pd
from rich.panel import Panel

key_1 = []
key_2 = []
untuk_panda = []

def parse_all_value_keys(palue_1, palue_2, merge_rules):
	key_1.clear()
	key_2.clear()
	untuk_panda.clear()
	val_list_value1 = list(palue_1.keys())
	val_list_value2 = list(palue_2.keys())

	for y in range(0, len(palue_1)):
		key_1.append(val_list_value1[y])

	for x in range(0, len(palue_2)):
		key_2.append(val_list_value2[x])

	panda(merge_rules, palue_1)


def panda(merge_rules, palue_1):


	"""
	untuk nyesuain rules, value1, value2 ama tabel, contoh
	3 rules, 3 value1, 3 tabel = 9 rules
	untuk memasangkan
	"""
	#print(merge_rules)
	arr = np.array(merge_rules)
	newarr = np.array_split(arr, len(palue_1))
	for y in newarr:
		untuk_panda.append(y.tolist())
	#print(untuk_panda)

	#print(Panel.fit("[green][[white]x[green]][white] Creating Rules of Fuzzy Logic - Sugeno"))
	array = np.array(untuk_panda)

	df = pd.DataFrame(data = array, 
					  index = key_2, 
					  columns = key_1)
  
	print(df)
