
#maybe bash
import numpy as np
import cv2
import os


# get the path or directory
folder_dir = input("What is the folder?")
for images in os.listdir(folder_dir):
    if not images.endswith('_Edited.PNG'):
        if not images.endswith('_Edited2.PNG'):
            # img_path = input("What is the image path?")
            img_path = folder_dir + '/' + images
            cap =  cv2.imread(img_path)

            #cropping by removing the outer 20% of the boundary (10% on each side)
            #in order to get rid of any outside-of-tree areas
            top_of_img = int(cap.shape[0] * 0.1)
            bottom_of_img = int(cap.shape[0] * 0.9)
            left_of_img = int(cap.shape[1] * 0.1)
            right_of_img = int(cap.shape[1] * 0.9)
            # Cropping an image
            cap = cap[top_of_img:bottom_of_img, left_of_img:right_of_img]


            cap_HSV = cv2.cvtColor(cap, cv2.COLOR_BGR2HSV)
            cap_threshold = cv2.inRange(cap_HSV, (48, 5, 93), (89, 68,255))

            newimg = cap_threshold
            number_of_white_pix = np.sum(newimg != 0)
            number_of_total_pix = cap.shape[0] * cap.shape[1]
            # print(number_of_total_pix)
            # print("The number of pixels (shown in white) that fit this parameter is:",
            #             number_of_white_pix)
            # print(number_of_total_pix)
            desired_proportion = 100 * (number_of_white_pix / number_of_total_pix)
            # print(desired_proportion)




            # this will return a tuple of root and extension
            split_tup = os.path.splitext(images)
            
            # extract the file name and extension
            file_name = split_tup[0]
            file_extension = split_tup[1]

            png_img_name = file_name + '_Edited.PNG'

            #new filedir
            newfiledir = os.path.splitext(img_path)
            new_file_name = newfiledir[0]
            new_file_ext = newfiledir[1]
            data_img_name = new_file_name + '_Edited.PNG'
            #save selected color in file
            def write_to_file(neighborhoodname, imgName, pix_count, proportional_pix_count):
                pix_count = round(pix_count, 3)
                proportional_pix_count = round(proportional_pix_count, 5)
                f = open("Foliose_concentrations.csv", "a")
                White_color = str(neighborhoodname) + "," + str(imgName) + "," \
                    + str(pix_count) + \
                    "," + str(proportional_pix_count) + str("\r")
                f.write(White_color)
                f.close()

            write_to_file(folder_dir,png_img_name, number_of_white_pix, desired_proportion)
            cv2.imwrite(data_img_name, newimg)
