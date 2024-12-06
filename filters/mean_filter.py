
def mean3x3Filter(img):
    img_filtered = img.copy()
    for i in range(1, img_filtered.shape[0] - 1):
        for j in range(1, img_filtered.shape[1] - 1):
            mean = (int(img_filtered[i-1, j-1]) + int(img_filtered[i-1, j]) + int(img_filtered[i-1, j+1]) + 
                    int(img_filtered[i, j-1]) + int(img_filtered[i, j]) + int(img_filtered[i, j+1]) + 
                    int(img_filtered[i+1, j-1]) + int(img_filtered[i+1, j]) + int(img_filtered[i+1, j+1])) // 9
            
            img_filtered[i, j] = min(mean, 255)

    return img_filtered