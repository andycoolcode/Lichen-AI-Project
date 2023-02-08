#open entire folder at a time rather than file?
#maybe bash
import numpy as np
import cv2

img_path = input("What is the image path?")

cap =  cv2.imread(img_path)
cap_HSV = cv2.cvtColor(cap, cv2.COLOR_BGR2HSV)
cap_threshold = cv2.inRange(cap_HSV, (48, 5, 93), (89, 68,255))

newimg = cap_threshold
number_of_white_pix = np.sum(newimg != 0)
number_of_black_pix = np.sum(newimg == 0)
number_of_total_pix = np.sum([number_of_black_pix,number_of_white_pix])
print("The number of pixels (shown in white) that fit this parameter is:",
            number_of_white_pix)
print(number_of_black_pix)
print(number_of_total_pix)
desired_proportion = number_of_white_pix / number_of_total_pix
print(desired_proportion)




#Saving the image as a new file
png_img_name = ''

def rename_img(img_name, file_type):
    index_num = img_name.index(file_type)
    img_name = img_name[0:index_num]
    img_name += '_Edited.png'
    return img_name

if '.jpg' in img_path:
    png_img_name = rename_img(img_path, '.jpg')
elif '.JPG' in img_path:
    png_img_name = rename_img(img_path, '.JPG')
elif '.jpeg' in img_path:
    png_img_name = rename_img(img_path, '.jpeg')
elif '.JPEG' in img_path:
    png_img_name = rename_img(img_path, '.JPEG')
elif '.png' in img_path:
    png_img_name = rename_img(img_path, '.png')
elif '.PNG' in img_path:
    png_img_name = rename_img(img_path, '.png')
else:
    print('unsupported img type')

#save selected color in file
def write_to_file(imgName, pix_count, desired_pix_count):
    f = open("saved_colors.txt", "a")
    White_color = str(imgName) + ":" + str(pix_count) + \
    "; proportion: " + str(desired_pix_count) + str("\r")
    f.write(White_color)
    f.close()

write_to_file(png_img_name, number_of_white_pix, desired_proportion)
cv2.imwrite(png_img_name, newimg)
