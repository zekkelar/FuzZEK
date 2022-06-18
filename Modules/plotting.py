import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt


palue_1 ={
		 'Kurang Ramah':'0,5,7.5',
		 'Biasa':'5,7.5,10',
		 'Sangat Ramah':'7.5,10,20',
		 }

saved_one = []
saved_two = []
def ploting(value1, value2):
	a=(value1.keys())
	for k in a:
		saved_two.append(k)


	panjang_plot = 15
	x_one = np.arange(1,15,1)
	for y in palue_1:
		#print(palue_1[y])
		saved_one.append(palue_1[y])

	pisah1 = saved_one[0].split(',')
	if '.' in str(pisah1[-1]):
		remover = pisah1[-1].split('.')
		last_pisah = remover[0]

	else:
		last_pisah = pisah1[-1]

	one = fuzz.trapmf(x_one, [1,1,int(pisah1[1]), float(last_pisah)])
	plt.plot(x_one, one, 'b', linewidth=1.5, label=f'{saved_two[0]}')



	pisah2 = saved_one[1].split(',')
	if '.' in str(pisah2[0]):
		remover2 = pisah2[0].split('.')
		last_pisah2 = remover2[0]
	else:
		last_pisah2 = pisah2[0]

	pisah2_1 = saved_one[1].split(',')
	#print(pisah2_1)
	if '.' in str(pisah2_1[1]):
		remover2_1 = pisah2_1[1].split('.')
		last_pisah2_1 = remover2_1[0]
	else:
		last_pisah2_1 = pisah2_1[1]

	pisah2_2 = saved_one[1].split(',')
	if '.' in str(pisah2_2[2]):
		remover2_2 = pisah2_2[1].split('.')
		last_pisah2_2 = remover2_2[0]
	else:
		last_pisah2_2 = pisah2_2[2]

	x_two = np.arange(1,15,1)
	two = fuzz.trimf(x_two, [float(last_pisah2), float(last_pisah2_1), float(last_pisah2_2)])
	plt.plot(x_two, two, 'g', linewidth=1.5, label=f'{saved_two[1]}')


	pisah3 = saved_one[2].split(',')
	if '.' in str(pisah3[0]):
		remover3 = str(pisah3[0]).split('.')
		last_pisah3 = remover[0]
	else:
		last_pisah3 = pisah3[0]

	if '.' in str(pisah3[1]):
		remover3_1 = str(pisah3[1]).split('.')
		last_pisah3_1 = remover3_1[0]
	else:
		last_pisah3_1 = pisah3[1]

	x_three = np.arange(float(last_pisah3),15,1)
	three = fuzz.trimf(x_three, [float(last_pisah3), float(last_pisah3_1), 1000])
	plt.plot(x_three, three, 'r', linewidth=1.5, label=f'{saved_two[2]}')
	plt.legend()
	plt.show()
