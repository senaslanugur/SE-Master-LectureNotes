# kutuphanelerin eklenmesi
import cv2
import numpy as np

# resim yolunun eklenmesi
img_path = "./images/manzara.jpg"

# resmin matris haline getirilmesi
img = cv2.imread(img_path)

# RGB kanallarının gösterilmesi
# yukseklik, genislik, kanal sayisi
print("goruntu kanallarinın degeri: ",img.shape)    #(415, 830, 3)

# renk scalalarının minimum ve maksimum kısmını gösteriyor
print("Minimum: ", np.min(img))     # 0
print("Maksimum: ", np.max(img))    # 255

# belirli bir pikselin RGB değerleri 
print("Resim R kanalı degeri: ", img[0,0,2]) #(0,0) pikselinin R(2) kanal degeri
print("Resim G kanalı degeri: ", img[0,0,1]) #(0,0) pikselinin G(1) kanal degeri
print("Resim B kanalı degeri: ", img[0,0,0]) #(0,0) pikselinin B(0) kanal degeri


# belirli bir bölgeden resim alıp yazdirmak
satir_baslangic = 210
sutun_baslangic = 210
satir_bitis = 300
sutun_bitis = 360

img_kesilen = img[satir_baslangic:satir_bitis, sutun_baslangic:sutun_bitis]

# secilen bolgenin ekranda gosterilmesi 
cv2.imshow("kesilen alan", img_kesilen)
cv2.waitKey(0)
cv2.destroyAllWindows()

# secilen bolgenin RGB kadnal degerleri
img_kesilen_R = img_kesilen[:,:,2] # kesilen tum bolgenin R kanali degerleri 
img_kesilen_G = img_kesilen[:,:,1] # kesilen tum bolgenin G kanali degerleri 
img_kesilen_B = img_kesilen[:,:,0] # kesilen tum bolgenin B kanali degerleri 

cv2.imshow("Secilen alanın R kanalı degerleri: ", img_kesilen_R) #secilen alanın R kanalı üzerinden gorunumu
cv2.waitKey(0)
cv2.destroyAllWindows()

# resmi siyah beyaz a cevirmek
img_grayscale = cv2.imread(img_path,0) # 0 demek siyah beyaz olarak gostermek ıcım RGB ortalamasını alır

# siyah beyaz'a cevirilen resmin RGB kanal sayisi
print(img_grayscale.shape) #(415, 830)

# siyah beyaz'a cevirilen goruntunun gosterilmesi
cv2.imshow("siyah beyaz alan", img_grayscale)
cv2.waitKey(0)
cv2.destroyAllWindows()