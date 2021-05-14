import generate_results
import numpy as np
import matplotlib.pyplot as plt

results = generate_results.get_data()
men = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
women = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
counter_men = 0
counter_women = 0
for subject in results:
	if results[subject][0] == "m":
		men[0] += results[subject][2]
		men[1] += results[subject][3]
		men[2] += results[subject][4]
		men[3] += results[subject][5]
		men[4] += results[subject][6]
		men[5] += results[subject][7]
		men[6] += results[subject][13]   #wrong_first_two_blocks_cong
		men[7] += results[subject][12]   #wrong_first_two_blocks_incong
		men[8] += results[subject][10]   #wrong_response_repeat_cong 
		men[9] += results[subject][8]    #wrong_response_repeat_incong
		men[10] += results[subject][11]  #wrong_response_switch_cong
		men[11] += results[subject][9]   #wrong_response_switch_incong
		counter_men += 1
	elif results[subject][0] == "f":
		women[0] += results[subject][2]
		women[1] += results[subject][3]
		women[2] += results[subject][4]
		women[3] += results[subject][5]
		women[4] += results[subject][6]
		women[5] += results[subject][7]
		women[6] += results[subject][13]   #wrong_first_two_blocks_cong
		women[7] += results[subject][12]   #wrong_first_two_blocks_incong
		women[8] += results[subject][10]   #wrong_response_repeat_cong 
		women[9] += results[subject][8]    #wrong_response_repeat_incong
		women[10] += results[subject][11]  #wrong_response_switch_cong
		women[11] += results[subject][9]   #wrong_response_switch_incong
		counter_women += 1
for subject in men:
	index = men.index(subject)
	if index < 6:
		men[index] /= 1000
	if index >= 6:
		men[index] *= 100
for subject in women:
	index = women.index(subject)
	if index < 6:
		women[index] /= 1000
	if index >= 6:
		women[index] *= 100
if counter_men != 0:
	for result in men:
		result /= counter_men
if counter_women != 0:
	for result in women:
		result /= counter_women
print(men, women)


X = ['Pure C','Pure I','Repeat C','Repeat I','Switch C','Switch I']
Y = women[0:6]
Z = men[0:6]
_X = np.arange(len(X))
plt.bar(_X - 0.2, Y, 0.4, label='Women')
plt.bar(_X + 0.2, Z, 0.4, label='Men')
plt.xticks(_X, X)
plt.title("Response times")
plt.legend()
plt.show()

X = ['Pure C','Pure I','Repeat C','Repeat I','Switch C','Switch I']
Y = women[6:]
Z = men[6:]
_X = np.arange(len(X))
plt.bar(_X - 0.2, Y, 0.4, label='Women')
plt.bar(_X + 0.2, Z, 0.4, label='Men')
plt.xticks(_X, X)
plt.title("Error percentages")
plt.legend()
plt.show()
