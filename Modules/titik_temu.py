
import time
import pandas as pd
import numpy as np
import itertools
from rich import print
from rich.panel import Panel
from matplotlib.pyplot import *
from fuzzylab import *
from simpful import *

nana = dict()
titik_temu_2 = []


def drange4(palue_1,pandas_properties_2, value_2_nilai):
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
					#print(' Found {} '.format(str(round(a,2))))

					titik_temu_2.append(f"{out}")
					add_titiktemu_two = out+1
					titik_temu_2.append(add_titiktemu_two)
					break
				else:
					print('Not found')
			else:
				#print('jancok {}'.format( str(round(a, 2))))
				pass
		out += 1
	#print(titik_temu_2)
	return titik_temu_2
