from __future__ import with_statement
import os
import configparser
import random
import numpy as np 

def main():
	data = np.load('ssim.npy')
	count = 0
	for i in range(data.shape[0]-5):
		if data[i]<0.3:
			count = count+1
	print count

if __name__ == '__main__':
	main()