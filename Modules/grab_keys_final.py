import time
import pandas as pd
import numpy as np
import itertools
from rich import print
from rich.panel import Panel
from matplotlib.pyplot import *
from fuzzylab import *
from simpful import *

sikap = []

def grab_keys_final(palue_1, titik_temu_2):
	#SOLVED
	#print(titik_temu_2)
	find_keys_1 = titik_temu_2[0]
	find_keys_2 = (titik_temu_2[-1])
	val_list = list(palue_1.keys())

	print(Panel.fit("""
Got Parameter One: {}
Got Parameter Two: {}
		""".format(val_list[int(find_keys_1)],val_list[find_keys_2]), title="[ Keys ]"))

	sikap.append(val_list[int(find_keys_1)])
	sikap.append(val_list[int(find_keys_2)])
	return sikap	