import cv2

for i in range(12):
    img = cv2.imread('./data/train/' + str(i+1) + '.jpg')
    resimg = cv2.resize(img, (256, 256))
    status = cv2.imwrite('./data/resize/' + str(i+1) + '.jpg', resimg)
    print(status)
