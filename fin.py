
import time
import pandas as pd
import numpy as np
import itertools
from rich import print
from rich.panel import Panel
import os
from matplotlib.pyplot import *
from fuzzylab import *
from simpful import *
from Modules.get_value import *
from Modules.find_axie import *
from Modules.merge_rules import *
from Modules.parse_value_keys import *
from Modules.titik_temu import *
from Modules.interferensi import *
import threading
from Modules.sikap_inter import *
from Modules.merge_value import *
from Modules.compare_value_rules import *
from Modules.interferensi_2 import *
from Modules.plotting import ploting
import xlrd

"""
palue_1 ={
		 'Kurang Ramah':'0,5,7.5',
		 'Biasa':'5,7.5,10',
		 'Sangat Ramah':'7.5,10,20',
		 }


palue_2 ={
		 'Lambat':'-1000,4,7',
		 'Standar':'4,7,10',
		 'cepat':'7,10,20',
		 }


#value nya 2, rules nya 3
#value nya 3 , rules nya 5
#value nya 4 , rulesnya 7
#check_validate_rules = 
key_rules = ['Sangat sedikit', 'Sedikit', 'Normal', 'Banyak', 'Sangat banyak']


rules = {
		'Sangat sedikit':'300',
		'Sedikit':'450',
		'Normal':'600',
		'Banyak':'800',
		'Sangat Banyak':'1000',
}
"""
palue_1 = dict()
palue_2 = dict()
rules = dict()
key_rules = []

def open_file():
	get_user= (os.environ.get('USERNAME'))

	df = pd.read_excel('C:/Users/{}/Documents/parameter.xls' .format(get_user), sheet_name='Sheet1')
	a=(df.to_dict())
	for var,key in zip(a['variable'],a['keys']):
		palue_1[a['variable'][var]] = a['keys'][key]
	#print(palue_1)
	

	df = pd.read_excel('C:/Users/{}/Documents/parameter2.xls' .format(get_user), sheet_name='Sheet1')
	a=(df.to_dict())
	for var,key in zip(a['variable'],a['keys']):
		palue_2[a['variable'][var]] = a['keys'][key]
	#print(palue_2)

	df = pd.read_excel('C:/Users/{}/Documents/rules.xls' .format(get_user), sheet_name='Sheet1')
	a=(df.to_dict())
	for var,key in zip(a['rulez'],a['keys']):
		rules[a['rulez'][var]] = a['keys'][key]
	#print(rules)

	for rul in range(0, len(a['rulez'])):
		key_rules.append((a['rulez'][rul]))
	#print(key_rules)

def membuat_plot():
	ploting(palue_1, palue_2)
one_interferensi = []
two_interferensi = []
sikap_interferensi_one = []
sikap_interferensi_two = []

def parameter_one():
	value = float(7.0)

	pandas_properties = (get_value(palue_1))
	(drange3(palue_1,pandas_properties,value)) #solved
	merge_rulez = ((two(key_rules, palue_1)))
	parse_all_value_keys(palue_1,palue_2,merge_rulez)

	get_titik_temu = drange4(palue_1,pandas_properties,value)

	get_val=(pandas_properties[int(get_titik_temu[0])])

	interferensi_2(value,palue_1, get_titik_temu,get_val[0], get_val[1])
	#get_titik_temu.clear()

def parameter_two():
	value = float(8.5)
	pandas_properties = (get_value(palue_2))

	(drange3(palue_2,pandas_properties,value)) #solved
	
	merge_rulez = ((two(key_rules, palue_2)))
	parse_all_value_keys(palue_1,palue_2,merge_rulez)

	get_titik_temu = drange4(palue_2,pandas_properties,value)

	get_val=(pandas_properties[int(get_titik_temu[0])])

	interferensi_2(value,palue_2, get_titik_temu,get_val[0], get_val[1])
	res =(interferensi_2(value,palue_2, get_titik_temu,get_val[0], get_val[1]))

	one_interferensi.append(res[0])
	one_interferensi.append(res[1])
	two_interferensi.append(res[3])
	two_interferensi.append(res[4])
	sikap_all = (grab_keys_final(palue_2, get_titik_temu))
	sikap_interferensi_one.append(sikap_all[0])
	sikap_interferensi_one.append(sikap_all[1])
	sikap_interferensi_two.append(sikap_all[2])
	sikap_interferensi_two.append(sikap_all[3])


total_1 = dict()
total_2 = dict()

def get_value_form():
	
	for sikap,value in zip(sikap_interferensi_one,one_interferensi):
		com = ("{} = {}" .format(sikap, value))
		total_1[sikap]=value

	for sikap,value in zip(sikap_interferensi_two,two_interferensi):
		com = ("{} = {}" .format(sikap, value))
		total_2[sikap] = value


def compare():
	for s in (total_1):
		for y in (total_2):
			print("{} | {}" .format(s,y))


key_win = []
key_win_compare = []

def compare2():
	val_list_1 = list(total_1.values())
	val_key_1 = list(total_1.keys())
	val_list_2 = list(total_2.values())
	val_key_2 = list(total_2.keys())

	for val1,key1 in zip(val_list_1,val_key_1):
		for val2,key2 in zip(val_list_2,val_key_2):
			if val1 <= val2:
				key_win_compare.append('{}|{}' .format(key1,key2))
				key_win.append('{}:{}' .format(key1,val1))
			
			else:
				key_win_compare.append('{}|{}' .format(key1,key2))
				key_win.append('{}:{}' .format(key2,val2))
			#print("α {} Ո α {} : {} Ո {}" .format(key1,key2, val1,val2))

result_rules=[]
def valuexrules():
	a = (merge_values(palue_1,palue_2))
	b = two(key_rules, palue_2)
	result = (compares(a,b))
	
	for de in key_win_compare:
		result_rules.append(result[de])

def gabung_final():
	get_value_form()
	compare2()
	valuexrules()
	parse_rules(result_rules, rules)
	#print('[x] COKKKK {}' .format(result_rules))
	pisah(key_win)

def inits():

	print(Panel.fit(""" 
{} 
{}
{}
{}
		""" .format(key_win[0], key_win[1], key_win[2], key_win[3]), title="Inferensi"))
	gabung()

result_parse_rules = []


def banner():
	print("""
 _______                       
(_______)                      
 _____ _   _ _____ _____ _   _ 
|  ___) | | (___  |___  ) | | |
| |   | |_| |/ __/ / __/| |_| |
|_|   |____/(_____|_____)\__  |
						(____/ 
[x] Fuzzy Method Takagi Sugeno 
		with two parameter
[x] __Author : ZekkelAR
""")


def validating_program():
	if len(palue_1) != len(palue_2):
		print('length value 1 must same with value 2')

	elif len(palue_1) == 2:
		if len(key_rules) != 3:
			if len(key_rules) <= 3:
				print('[x] Closing programs, please add your rules to three to matched a process')
			else:
				print('[x] Closing programs, please remove your rules to three to matched a process')
		else:
			print('[x] Starting FuzzyLogic')
			#time.sleep(3)
			main_process()

	elif len(palue_1) == 3:
		if len(key_rules) != 5:
			if len(key_rules) <= 5:
				print('[x] Closing programs, please add your rules to five to matched a process')
			else:
				print('[x] Closing programs, please remove your rules to five to matched a process')
		else:
			#time.sleep(3)
			main_process()

	elif len(palue_1) == 4:
		if len(key_rules) != 7:
			if len(key_rules) <= 7:
				print('[x] Closing programs, please add your rules to seven to matched a process')
			else:
				print('[x] Closing programs, please remove your rules to seven to matched a process')
		else:
			#time.sleep(3)
			main_process()
	else:
		exit()

def main_process():
	parameter_one()
	print("================")
	parameter_two()

	gabung_final()
	inits()	

if __name__ == "__main__":
	os.system('cls')
	banner()
	open_file()

	t = threading.Thread(target=membuat_plot)
	t.start()

	q = threading.Thread(target=validating_program)
	q.start()
	

