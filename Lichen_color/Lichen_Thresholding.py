from __future__ import print_function
import cv2 as cv
import argparse
import numpy as np

max_value = 255
max_value_H = 360//2
low_H = 0
low_S = 0
low_V = 0
high_H = max_value_H
high_S = max_value
high_V = max_value
window_capture_name = 'Original Img'
window_detection_name = 'After Editing'
low_H_name = 'Low H'
low_S_name = 'Low S'
low_V_name = 'Low V'
high_H_name = 'High H'
high_S_name = 'High S'
high_V_name = 'High V'


# Making the adjustable bars
def on_low_H_thresh_trackbar(val):
    global low_H
    global high_H
    low_H = val
    low_H = min(high_H-1, low_H)
    cv.setTrackbarPos(low_H_name, window_detection_name, low_H)
def on_high_H_thresh_trackbar(val):
    global low_H
    global high_H
    high_H = val
    high_H = max(high_H, low_H+1)
    cv.setTrackbarPos(high_H_name, window_detection_name, high_H)
def on_low_S_thresh_trackbar(val):
    global low_S
    global high_S
    low_S = val
    low_S = min(high_S-1, low_S)
    cv.setTrackbarPos(low_S_name, window_detection_name, low_S)
def on_high_S_thresh_trackbar(val):
    global low_S
    global high_S
    high_S = val
    high_S = max(high_S, low_S+1)
    cv.setTrackbarPos(high_S_name, window_detection_name, high_S)
def on_low_V_thresh_trackbar(val):
    global low_V
    global high_V
    low_V = val
    low_V = min(high_V-1, low_V)
    cv.setTrackbarPos(low_V_name, window_detection_name, low_V)
def on_high_V_thresh_trackbar(val):
    global low_V
    global high_V
    high_V = val
    high_V = max(high_V, low_V+1)
    cv.setTrackbarPos(high_V_name, window_detection_name, high_V)

# parser = argparse.ArgumentParser(description='Code for Thresholding Operations using inRange tutorial.')
# parser.add_argument('--camera', help='Camera divide number.', default=0, type=int)
# args = parser.parse_args()
img_path = input("Image path?")
cap =  cv.imread(img_path)

cv.namedWindow(window_capture_name, cv.WINDOW_KEEPRATIO)
cv.resizeWindow(window_capture_name, 400, 400)
cv.namedWindow(window_detection_name, cv.WINDOW_KEEPRATIO)
cv.resizeWindow(window_detection_name, 300, 300)

cv.createTrackbar(low_H_name, window_detection_name , 0, max_value_H, on_low_H_thresh_trackbar)
cv.createTrackbar(high_H_name, window_detection_name , 70, max_value_H, on_high_H_thresh_trackbar)
cv.createTrackbar(low_S_name, window_detection_name , 0, max_value, on_low_S_thresh_trackbar)
cv.createTrackbar(high_S_name, window_detection_name , 87, max_value, on_high_S_thresh_trackbar)
cv.createTrackbar(low_V_name, window_detection_name , 0, max_value, on_low_V_thresh_trackbar)
cv.createTrackbar(high_V_name, window_detection_name , 102, max_value, on_high_V_thresh_trackbar)
while True:
    
    cap
    if cap is None:
        break
    cap_HSV = cv.cvtColor(cap, cv.COLOR_BGR2HSV)
    cap_threshold = cv.inRange(cap_HSV, (low_H, low_S, low_V), (high_H, high_S, high_V))
    
    
    cv.imshow(window_capture_name, cap)
    cv.imshow(window_detection_name, cap_threshold)

    key = cv.waitKey(30)
    if key == ord('s'):
        newimg = cap_threshold
        number_of_white_pix = np.sum(newimg != 0)
        number_of_total_pix = cap.shape[0] * cap.shape[1]
        print(number_of_total_pix)
        # print("The number of pixels (shown in white) that fit this parameter is:",
                    # number_of_white_pix)
        print(number_of_total_pix)
        desired_proportion = 100 * (number_of_white_pix / number_of_total_pix)
        print(desired_proportion)



        print("The parameters are:")
        print("(Low H, high H) = (", low_H, ",", high_H, ")" )
        print("(Low S, high S) = (", low_S, ",", high_S, ")" )
        print("(Low V, high V) = (", low_V, ",", high_V, ")" )
        print("The number of pixels (shown in white) that fit this parameter is:",
            number_of_white_pix)
    if key == ord('q') or key == 27:
        break