from utils.order_ascending import orderAscending

def median3x3Filter(img):
    img_filtered = img.copy()
    for i in range(1, img_filtered.shape[0] - 1):
        for j in range(1, img_filtered.shape[1] - 1):
            items = [img_filtered[i-1, j-1], img_filtered[i-1, j], img_filtered[i-1, j+1], img_filtered[i, j-1], img_filtered[i, j], img_filtered[i, j+1], img_filtered[i+1, j-1], img_filtered[i+1, j], img_filtered[i+1, j+1]]
            ordered = orderAscending(items)
            median = ordered[len(ordered)//2]
            img_filtered[i, j] = median

    return img_filtered