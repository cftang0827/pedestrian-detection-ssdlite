import api
import cv2
from matplotlib import pyplot as plt 

img = cv2.imread('example.jpg')
bbox_list = api.api(img, 0.6)

for i in bbox_list:
    cv2.rectangle(img, i[0], i[1], (125, 255, 51), thickness=2)

plt.imshow(img[:,:,::-1])
plt.show()

