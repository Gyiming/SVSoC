import numpy as np

def main():
	ssim = np.load('ssim.npy')
	total = 0
	for i in range(len(ssim)):
		if ssim[i] > 0.5:
			total = total + 1
	print(total)
if __name__ == '__main__':
	main()