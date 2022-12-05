#importing the module cv2
import cv2
imageread = cv2.imread('/mnt/newdisk/home/arjun.ashok/files/TwoStageDubbing/temp/gfpgan_infer/04-12-2022-21:16:58/gfpgan_outputs/restored_imgs/0000.jpg')
dimensions = imageread.shape
height = imageread.shape[0]
width = imageread.shape[1]
channels = imageread.shape[2]

print('The dimension of the input image is : ', dimensions)
print('The height of the input image is : ', height)
print('The width of the input image is : ', width)
print('The Number of Channels in the input image are : ', channels)