import cv2

def Mean3x3Filter(img):
    image_matrix = img.copy()
    for i in range(1, image_matrix.shape[0] - 1):
        for j in range(1, image_matrix.shape[1] - 1):
            mean = (image_matrix[i-1, j-1] + image_matrix[i-1, j] + image_matrix[i-1, j+1] + image_matrix[i, j-1] + image_matrix[i, j] + image_matrix[i, j+1] + image_matrix[i+1, j-1] + image_matrix[i+1, j] + image_matrix[i+1, j+1]) / 9
            image_matrix[i, j] = mean

    return image_matrix


path = "./image.jpg"
img = cv2.imread(path)
filtered_img = Average3x3Filter(img)
cv2.imshow("img", img)
cv2.imshow("filtered", filtered_img)
cv2.waitKey(0)

cv2.destroyAllWindows()