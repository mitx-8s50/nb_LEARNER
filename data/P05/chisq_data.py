import numpy as np
import matplotlib.pyplot as plt
import random

def model():
	x = np.arange(-1,1.1,step=0.1)
	y = 200 - (x+1)*50
	with open('chisq_model.txt','w') as f:
		for n in range(len(x)):
			f.write(str(x[n])+','+str(y[n]))
			f.write('\n')

def data1():
	x = np.arange(-1,1.1,step=0.1)
	y = 200 - (x+1)*50 + (np.random.exponential(size=len(x))*15-15)
	with open('chisq_data1.txt','w') as f:
		for n in range(len(y)):
			f.write(str(y[n]))
			f.write('\n')

def data2():
	x = np.arange(-1,1.1,step=0.1)
	y = 200 - (x+1)*50 + (np.random.poisson(size=len(x))*10-5)
	with open('chisq_data2.txt','w') as f:
		for n in range(len(y)):
			f.write(str(y[n]))
			f.write('\n')

def data3():
	x = np.arange(-1,1.1,step=0.1)
	y = 200 - (x+1)*50 + (np.random.weibull(1.5,size=len(x))*10-10)
	with open('chisq_data3.txt','w') as f:
		for n in range(len(y)):
			f.write(str(y[n]))
			f.write('\n')