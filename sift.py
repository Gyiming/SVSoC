import os
import cv2
import numpy as np

def SIFT_match(img1,img2):

	#print(type(img1))
	#print(type(img2))
	gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
	gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
	#sift = cv2.SIFT()
	sift = cv2.xfeatures2d.SIFT_create()

	kp1, des1 = sift.detectAndCompute(gray1,None)
	kp2, des2 = sift.detectAndCompute(gray2,None)

	#print(des1.shape)
	#print(des2.shape)
	if not kp2:
	    return (len(kp1),0)
	bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
	matches = bf.match(des1,des2)
	#print(len(matches))
	return(len(kp1),len(matches))

def cal_IOU(cx1,cx2,cy1,cy2,gx1,gx2,gy1,gy2):

    cx1 = int(cx1)
    cx2 = int(cx2)
    cy1 = int(cy1)
    cy2 = int(cy2)
    gx1 = int(gx1)
    gx2 = int(gx2)
    gy1 = int(gy1)
    gy2 = int(gy2)
    carea = float((cx2 - cx1) * (cy2 - cy1))
    garea = float((gx2 - gx1) * (gy2 - gy1)) 
 
    x1 = max(cx1, gx1)
    y1 = max(cy1, gy1)
    x2 = min(cx2, gx2)
    y2 = min(cy2, gy2)
    w = max(0, x2 - x1)
    h = max(0, y2 - y1)
    area = float(w * h) 
 
    iou = float(area / (carea + garea - area))
 
    return iou

def positive_check(a):
    output = int(a)
    if output<0:
        output = 0
    return output

def check(img_key,img_spec,bbox_key,bbox_spec):
	match_bbox = 0
	if len(bbox_key) != len(bbox_spec):
		return 0
	else:
		for line_spec in bbox_spec:
			spec_info = line_spec.split()
			max_iou = 0
			count = 0
			matching_url = 0
			#finding the bounding box in key frame that has the most IOU, matching_url
			for line_key in bbox_key:
				count = count + 1
				key_info = line_key.split()
				if cal_IOU(spec_info[2],spec_info[4],spec_info[3],spec_info[5],key_info[2],key_info[4],key_info[3],key_info[5]) > max_iou:
					matching_url = count
			count = 0
			#calculating the matching points with matching_url
			for line_key in bbox_key:
				count = count + 1
				if count == matching_url:
					
					key_points, matches = SIFT_match(img_key[positive_check(key_info[3]):positive_check(key_info[5]),positive_check(key_info[2]):positive_check(key_info[4])],img_spec[positive_check(spec_info[3]):positive_check(spec_info[5]),positive_check(spec_info[2]):positive_check(spec_info[4])])
					if key_points == 0:
						match_bbox += 1				
					elif (float(matches)/float(key_points)) > 0.7:
						match_bbox += 1
	#print(match_bbox,len(bbox_spec)/2)
	if (match_bbox>float(len(bbox_spec)/2)):
		return 1
	else:
		return 0


def main():
	key_frame = 0
	match_number = 0
	for i in range(832):
		if (i==key_frame):
			cmd = 'cp ./convert_yolo/' + 'image' + str(i) + '.txt' + ' ./check/'
			os.system(cmd)
		else:
			bbox_dir_key = './convert_yolo/' + 'image' + str(key_frame) + '.txt'
			bbox_dir_spec = './convert_yolo/' + 'image' + str(i) + '.txt'
			img_dir_key = './data_kitti/' + 'image' + str(key_frame) + '.png'
			img_dir_spec = './data_kitti/' + 'image' + str(i) + '.png'
			img_key = cv2.imread(img_dir_key)
			img_spec = cv2.imread(img_dir_spec)
			fp_bbox_key = open(bbox_dir_key,'r')
			bbox_key = fp_bbox_key.readlines()
			fp_bbox_spec = open(bbox_dir_spec,'r')
			bbox_spec = fp_bbox_spec.readlines()		
			if check(img_key,img_spec,bbox_key,bbox_spec) == 1:
				cmd = 'cp ./convert_tiny/' + 'image' + str(i) + '.txt' + ' ./check/'
				os.system(cmd)
				match_number += 1
			else:
				cmd = 'cp ./convert_yolo/' + 'image' + str(i) + '.txt' + ' ./check/'
				os.system(cmd)
				key_frame = i
        print(match_number)


if __name__ == '__main__':
	main()



