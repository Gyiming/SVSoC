from __future__ import with_statement
from __future__ import print_function
import os
import configparser
import random
import numpy as np 
import cv2

def main():
	prev = cv2.imread("",0)
	presnet = cv2.imread("",0)
	flow = cv2.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
	next = presnet + flow
	

if __name__=='__main__':

	main()
