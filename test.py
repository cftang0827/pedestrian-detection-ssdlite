import cv2
from pedestrian_detection_ssdlite import api
from matplotlib import pyplot as plt

img = cv2.imread('test_img/example.jpg')
bbox_list = api.get_person_bbox(img, thr=0.6)
print(bbox_list)

for i in bbox_list:
    cv2.rectangle(img, i[0], i[1], (125, 255, 51), thickness=2)

plt.imshow(img[:, :, ::-1])
plt.show()
