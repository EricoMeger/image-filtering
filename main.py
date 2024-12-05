import cv2

def Mean3x3Filter(img):
    img_filtered = img.copy()
    for i in range(1, img_filtered.shape[0] - 1):
        for j in range(1, img_filtered.shape[1] - 1):
            mean = (img_filtered[i-1, j-1] + img_filtered[i-1, j] + img_filtered[i-1, j+1] + img_filtered[i, j-1] + img_filtered[i, j] + img_filtered[i, j+1] + img_filtered[i+1, j-1] + img_filtered[i+1, j] + img_filtered[i+1, j+1]) / 9
            img_filtered[i, j] = mean

    return img_filtered

def Median3x3Filter(img):
    img_filtered = img.copy()

    return img_filtered


path = "./image.jpg"
img = cv2.imread(path)
filtered_img = Average3x3Filter(img)
cv2.imshow("img", img)
cv2.imshow("filtered", filtered_img)
cv2.waitKey(0)

cv2.destroyAllWindows()