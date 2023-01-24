import numpy as np


def estimate_coef(x, y):
	n = np.size(x)

	mean_x = np.mean(x)
	mean_y = np.mean(y)

	
	SS_xy = np.sum(y*x) - n * mean_y * mean_x
	SS_xx = np.sum(x*x) - n* mean_x * mean_x

	a_1 = SS_xy / SS_xx
	a_0 = mean_y - a_1 * mean_x

	return (a_1, a_0)

def main():
	
	x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
	y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])

	a = estimate_coef(x, y)
	print("Estimated coefficients:\na_0 = {} \
		\na_1 = {}".format(a[0], a[1]))

	# plotting regression line
	#plot_regression_line(x, y, b)

if __name__ == "__main__":
	main()




