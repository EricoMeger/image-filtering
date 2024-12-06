import cv2
import numpy as np

def Mean3x3Filter(img):
    img_filtered = img.copy()
    for i in range(1, img_filtered.shape[0] - 1):
        for j in range(1, img_filtered.shape[1] - 1):
            mean = (int(img_filtered[i-1, j-1]) + int(img_filtered[i-1, j]) + int(img_filtered[i-1, j+1]) + 
                    int(img_filtered[i, j-1]) + int(img_filtered[i, j]) + int(img_filtered[i, j+1]) + 
                    int(img_filtered[i+1, j-1]) + int(img_filtered[i+1, j]) + int(img_filtered[i+1, j+1])) // 9
            
            img_filtered[i, j] = min(mean, 255)

    #Tratar borda
    return img_filtered

def orderByValue(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def Median3x3Filter(img):
    img_filtered = img.copy()
    for i in range(1, img_filtered.shape[0] - 1):
        for j in range(1, img_filtered.shape[1] - 1):
            items = [img_filtered[i-1, j-1], img_filtered[i-1, j], img_filtered[i-1, j+1], img_filtered[i, j-1], img_filtered[i, j], img_filtered[i, j+1], img_filtered[i+1, j-1], img_filtered[i+1, j], img_filtered[i+1, j+1]]
            ordered = orderByValue(items)
            median = ordered[len(ordered)//2]
            img_filtered[i, j] = median

    return img_filtered


path = "./image.jpg"

img = cv2.imread(path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

mean_filter = Mean3x3Filter(img)
median_filter = Median3x3Filter(img)

cv2.imshow("img", img)
cv2.imshow("mean", mean_filter)
cv2.imshow("median", median_filter) 
cv2.waitKey(0)

cv2.destroyAllWindows()