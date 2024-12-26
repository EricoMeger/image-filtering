import cv2
from filters.mean_filter import mean3x3Filter
from filters.median_filter import median3x3Filter

path = "./imgs/image.jpg"

img = cv2.imread(path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

mean_filter = mean3x3Filter(img)
median_filter = median3x3Filter(img)

cv2.imshow("img", img)
cv2.imshow("mean", mean_filter)
cv2.imshow("median", median_filter)

cv2.waitKey(0)
cv2.destroyAllWindows()