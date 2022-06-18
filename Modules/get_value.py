
import time
import pandas as pd
import numpy as np
import itertools
from rich import print
from rich.panel import Panel
from matplotlib.pyplot import *
from fuzzylab import *
from simpful import *

total_range_2 = []
pandas_properties_2 = []
total=[]



def get_value(value):
	total_range_2.clear()
	pandas_properties_2.clear()
	total.clear()
	for key_2 in value:
		ronal = (value[key_2]).split(',')
		total.append(ronal)

	output = 0
	for i in range(0, len(total)):
		total_range_2.append(total[i][1])
	rng = 0
	penanda = 0
	totalnih = []
	while(True):
		try:
			a=(total_range_2[0], total_range_2[1])
			totalnih.append(a)
			total_range_2.pop(0)
		
		except:
			break

	aru = np.array(totalnih)
	fla_arr = aru.flatten()
	arr = np.array(fla_arr)
	newarr = np.array_split(arr, len(totalnih))
	for y in newarr:
		pandas_properties_2.append(y.tolist())  
	#print(pandas_properties_2)
	return pandas_properties_2

