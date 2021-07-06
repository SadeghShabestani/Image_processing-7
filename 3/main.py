import cv2
import numpy as np
import argparse

parse = argparse.ArgumentParser()
parse.add_argument('-image', type=str, default='mr_bean.jpeg')
args = parse.parse_args()

image = cv2.imread(args.image, cv2.IMREAD_GRAYSCALE)
rows, columns = image.shape

# ======================== Noise ========================
noise = np.random.randint(0, 30, size=(rows, columns))
zeros = np.where(noise == 15)
ones = np.where(noise == 10)
image[zeros] = 0
image[ones] = 255

cv2.imwrite('noise.jpg', image)

# ======================== Delete Noise ========================
image = cv2.medianBlur(image, 3)
cv2.imwrite('delete_noise.jpg', image)

cv2.imshow('output', image)
cv2.waitKey()
