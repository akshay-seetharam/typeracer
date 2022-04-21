import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

def polynomial(x, a, b, c, d, e, f, g):
	a = float(a)
	b = float(b)
	c = float(c)
	d = float(d)
	e = float(e)
	f = float(f)
	g = float(g)
	return a + b*x**2 + c*x**3 + d*x**4 + e*x**5 + g*x**6

if __name__ == '__main__':
	data = pd.read_csv('~/typing.csv')
	
	wpm = data['wpm']
	wpm = wpm.tolist()
	wpm.reverse()
	print(type(wpm),len(wpm))
	#popt, pcov = curve_fit(polynomial, range(len(wpm)), wpm, bounds=[0, [[[-100.,1000.].,[-100.,1000.],[-100.,1000.],[-100.,1000.],[-100.,1000.],[-100.,1000.],[-100.,1000.]]])
	plt.hist(wpm)
	plt.figure()
	plt.scatter(list(range(len(wpm))),wpm)
	#plt.plot(xdata, func(xdata, *popt), 'r-',
        # label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
	
	plt.show()
