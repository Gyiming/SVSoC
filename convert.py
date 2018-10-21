from __future__ import with_statement
from __future__ import print_function
import os
import configparser
import random
import numpy as np 
import schedule
import bestE

def convert_yolo_coordinates_to_voc(x_c_n, y_c_n, width_n, height_n, img_width, img_height):

  x_c = float(x_c_n) * img_width
  y_c = float(y_c_n) * img_height
  width = float(width_n) * img_width
  height = float(height_n) * img_height
  ## compute half width and half height
  half_width = width / 2
  half_height = height / 2
  ## compute left, top, right, bottom
  ## in the official VOC challenge the top-left pixel in the image has coordinates (1;1)
  left = int(x_c - half_width) + 1
  top = int(y_c - half_height) + 1
  right = int(x_c + half_width) + 1
  bottom = int(y_c + half_height) + 1
  print (left,top,right,bottom)

def main():

  convert_yolo_coordinates_to_voc(0.628181,0.531076,0.103540,0.130316,160,128)


if __name__ == '__main__':
  main()