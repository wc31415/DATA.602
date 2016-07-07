#OpenCV
#http://opencv.org/downloads.html
#http://mathalope.co.uk/2015/05/07/opencv-python-how-to-install-opencv-python-package-to-anaconda-windows/


import cv2
import numpy as np
from matplotlib import pyplot as plt


#images read in directly from C:/


#takes contours and prints center points (centroids) of objects found in image
def findCenterPoints(input_contours):
    print "Center Points of Objects Found in Image:"
    for i in range(len(input_contours)):        
        input_cnt = input_contours[i]
        input_M = cv2.moments(input_cnt)
        centroid_x = int(input_M['m10']/input_M['m00'])
        centroid_y = int(input_M['m01']/input_M['m00'])
        print (centroid_x, centroid_y)
        
        
#takes thresholded image
#prints number of objects found in image
#calls function findCenterPoints with contours found in image        
def countObjects(input_binary_thresh):
    input_contours, input_hierarchy = cv2.findContours(input_binary_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    input_newimg = np.zeros_like(input_binary_thresh)
    cv2.drawContours(input_newimg, input_contours, -1, 255)
    cv2.imshow('Found', input_newimg)
    cv2.waitKey()
    print "Number of Objects Found in Image: " + str(len(input_contours))
    findCenterPoints(input_contours)
    
    
if __name__ == "__main__":
    circles_img = cv2.imread('C:/circles.png', 0)
    objects_img = cv2.imread('C:/objects.png', 0)
    peppers_img = cv2.imread('C:/peppers.png', 0)
    
    ret, circles_binary_thresh = cv2.threshold(circles_img, 127, 255, cv2.THRESH_BINARY)
    
    objects_remove_noise = cv2.blur(objects_img, (5, 5))
    ret, objects_binary_thresh = cv2.threshold(objects_remove_noise, 119, 255, cv2.THRESH_BINARY)
    
    peppers_remove_noise = cv2.blur(peppers_img, (9, 9))
    ret, peppers_binary_thresh = cv2.threshold(peppers_remove_noise, 129, 255, cv2.THRESH_BINARY)
        
    plt.subplot(2, 3, 1), plt.imshow(circles_img, 'gray')
    plt.title('circles.png')
    plt.subplot(2, 3, 4), plt.imshow(circles_binary_thresh, 'gray')
    plt.title('Binary Thresholding')
    plt.subplot(2, 3, 2), plt.imshow(objects_img, 'gray')
    plt.title('objects.png')
    plt.subplot(2, 3, 5), plt.imshow(objects_binary_thresh, 'gray')
    plt.title('Binary Thresholding')
    plt.subplot(2, 3, 3), plt.imshow(peppers_img, 'gray')
    plt.title('peppers.png')
    plt.subplot(2, 3, 6), plt.imshow(peppers_binary_thresh, 'gray')
    plt.title('Binary Thresholding')
    plt.show()
    
    print "circles.png"    
    countObjects(circles_binary_thresh)
    
    print "\nobjects.png"
    countObjects(objects_binary_thresh)
    
    print "\npeppers.png"
    countObjects(peppers_binary_thresh)
    