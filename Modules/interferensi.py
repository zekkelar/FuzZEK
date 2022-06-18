import time
import pandas as pd
import numpy as np
import itertools
from rich import print
from rich.panel import Panel
from matplotlib.pyplot import *
from fuzzylab import *
from simpful import *
from Modules.sikap_inter import *

res_inter = []
sikap_inter2 = []
def interferensi_2(value, palue_1, titik_temu_2, value_one,value_two):
	print("")
	#print(Panel.fit("interferensi"))
	

	inputan = value
	#
	# X - A / B - A
	#

	#get A value
	find_keys_1 = titik_temu_2[0]
	val_list = list(palue_1.keys())
	

	find_keys_2 = (titik_temu_2[-1])
	val_list_2 = list(palue_1.keys())

	##########################
	# Calculate Interference #
	##########################

	variable_one = (inputan - float(value_one)) / (float(value_two) - float(value_one))
	variable_two = (float(value_two) - float(inputan)) / (float(value_two) - float(value_one))
	#print()

	

	res_inter.append(variable_two)
	res_inter.append(variable_one)
	sikap_inter2.append(val_list[int(find_keys_2)])
	sikap_inter2.append(val_list[int(find_keys_1)])
	#sikap(sikap_inter2)

	return(res_inter)
