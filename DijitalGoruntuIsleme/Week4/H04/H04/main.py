import cv2
import numpy as np
import matplotlib.pyplot as plt

img_path = "./images/fourier_spectrum.tif"

img = cv2.imread(img_path, 0)

print(img.shape)

def log_trans(r, c):
    r = r.astype(np.float32)
    s = c * np.log(1 + r)
    s = img_rescale(s)
    return s.astype(np.uint8)

def img_rescale(img):
    #img = img - np.min(img)
    img -= np.min(img)
    img /= np.max(img)
    img *=255
    return img


img_log = log_trans(img, 1)

hstacked = np.hstack((img, img_log))

plt.imshow(hstacked, cmap="gray")
plt.show()

# print(np.min(img_log))
# print(np.max(img_log))

# plt.imsave("./images/deneme.jpg", img_log)


# plt.imshow(img_log, cmap="gray")
# plt.show()


a = np.array([5,50,150,254,255], dtype=np.uint8)

a_log = log_trans(a, 1)

a_log = a_log - np.min(a_log)
print(a_log)
a_log = a_log / np.max(a_log)
print(a_log)
a_log = a_log * 255
print(a_log)

