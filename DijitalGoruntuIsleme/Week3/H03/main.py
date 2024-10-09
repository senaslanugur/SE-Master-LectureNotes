import cv2
import numpy as np
import matplotlib.pyplot as plt

img_path = "./images/mamogram.png"
r = cv2.imread(img_path, 0)

print(r.shape)

# print(r[155,155,0]) #blue kanalı
# print(r[155,155,1]) #green kanalı
# print(r[155,155,2]) #red kanalı

# print(r[155,155])

# s = L - 1 - r

# 1 - 256 --> L-1
# 0 - 255 --> L

print(np.max(r))
L = np.max(r)

s = L - r

# cv2.imshow("negatif", s)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

yanyana = np.hstack((r, s))
altalta = np.vstack((r, s))

plt.imshow(altalta, cmap="gray")
plt.show()

