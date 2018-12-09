import matplotlib.pyplot as plt
import numpy as np #better work with arrays

from matplotlib.ticker import NullFormatter  # useful for `logit` scale

#matplot is limited to work with lists
#tutoral: https://matplotlib.org/users/pyplot_tutorial.html

def basic_plot_1():
	plt.plot([1,2,3,4])
	plt.ylabel('some numbers')
	plt.show()
	return


def basic_plot_2():
	plt.plot([1, 2, 3, 4], [1, 4, 9, 50])
	plt.ylabel('some numbers')
	plt.show()
	return


def basic_plot_3():
	plt.plot([1,2,3,4], [1,4,9,16], 'ro')
	plt.axis([0, 6, 0, 20])
	plt.show()

def basic_plot_4():
	# uma amostra a cada 200ms de intervalo
	t = np.arange(0., 5., 0.2)
	# red dashes, blue squares and green triangles
	plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
	plt.show()

def basic_plot_5(t):
	return np.exp(-t) * np.cos(2*np.pi*t)

def basic_plot_6():
	t1 = np.arange(0.0, 5.0, 0.1)
	t2 = np.arange(0.0, 5.0, 0.02)

	plt.figure(1) # figura 1
	plt.subplot(212) # subplot(nrows, ncols, index, **kwargs)
	plt.plot(t1, basic_plot_5(t1), 'bo', t2, basic_plot_5(t2), 'k')

	plt.subplot(212)
	plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
	plt.show()

def basic_plot_7():
	# Fixing random state for reproducibility
	np.random.seed(19680801)

	mu, sigma = 100, 18
	x = mu + sigma * np.random.randn(10000)

	# the histogram of the data
	n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)

	plt.xlabel('Eixo x')
	plt.ylabel('Eixo y')
	plt.title('Título do grafico')
	plt.text(60, .025, r'$\mu=100,\ \sigma=18$') #matplot libs accept TeX expressions
	plt.axis([40, 160, 0, 0.03])
	plt.grid(True)
	plt.show()

def basic_plot_8():
	ax = plt.subplot(111)

	t = np.arange(0.0, 5.0, 0.01)
	s = np.cos(2*np.pi*t)
	line, = plt.plot(t, s, lw=2)

	plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

	plt.ylim(-2,2)
	plt.show()

def basic_plot_9():
	# Fixing random state for reproducibility
	np.random.seed(19680801)

	# make up some data in the interval ]0, 1[
	y = np.random.normal(loc=0.5, scale=0.4, size=1000)
	y = y[(y > 0) & (y < 1)]
	y.sort()
	x = np.arange(len(y))

	# plot with various axes scales
	plt.figure(1)

	# linear
	plt.subplot(221)
	plt.plot(x, y)
	plt.yscale('linear')
	plt.title('linear')
	plt.grid(True)


	# log
	plt.subplot(222)
	plt.plot(x, y)
	plt.yscale('log')
	plt.title('log')
	plt.grid(True)

	# symmetric log
	plt.subplot(223)
	plt.plot(x, y - y.mean())
	plt.yscale('symlog', linthreshy=0.01)
	plt.title('symlog')
	plt.grid(True)

	# logit
	plt.subplot(224)
	plt.plot(x, y)
	plt.yscale('logit')
	plt.title('logit')
	plt.grid(True)
	
	# Format the minor tick labels of the y-axis into empty strings with
	# `NullFormatter`, to avoid cumbering the axis with too many labels.
	plt.gca().yaxis.set_minor_formatter(NullFormatter())

	# Adjust the subplot layout, because the logit one may take more space
	# than usual, due to y-tick labels like "1 - 10^{-3}"
	plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)

	plt.show()

if __name__ == "__main__":
	#basic_plot_1()
	#basic_plot_2()
	#basic_plot_3()
	#basic_plot_4()
	#basic_plot_6()
	#basic_plot_7()
	#basic_plot_8()
	basic_plot_9()

