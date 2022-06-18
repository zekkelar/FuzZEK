
import time
import pandas as pd
import numpy as np
import itertools
from rich import print
from rich.panel import Panel
from matplotlib.pyplot import *
from fuzzylab import *
from simpful import *
from Modules.grab_keys_final import *
import time
from multiprocessing import Process


nana = dict()
titik_temu_2 = []




def drange3(palue_1,pandas_properties_2, value_2_nilai):
	titik_temu_2.clear()
	nana.clear()
	for i in range(0,len(pandas_properties_2)):
		rng = np.arange(float(pandas_properties_2[i][0]), float(pandas_properties_2[i][1]), 0.1)
		nana[i] = rng #SoLVED

	out = 0
	for y in range(0, len(nana)):
		for a in nana[out]:
			if str(value_2_nilai) in str(round(a, 2)):
				if len(str(value_2_nilai)) == len(str(round(a, 2))):
					#print(Panel.fit(' Found {} '.format(str(round(a,2)))))

					titik_temu_2.append(f"{out}")
					add_titiktemu_two = out+1
					titik_temu_2.append(add_titiktemu_two)
					get_value_last(palue_1,pandas_properties_2)
					break
				else:
					print('Not found')
		out += 1


	#return titik_temu_2


def get_value_last(palue_1,pandas_properties_2):
	#print(titik_temu_2)
	try:
		get_val=(pandas_properties_2[int(titik_temu_2[0])])
		print('[x] Titik awal  : {}' .format(get_val[0]))
		print('[x] Titik akhir : {}' .format(get_val[-1]))
		grab_keys_final(palue_1, titik_temu_2)

	except Exception as e:
		print(e)
		#check_min_v()

	return titik_temu_2

	