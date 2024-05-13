import cv2

# 0 => gri seviye ==> (0 => Grey Level )
# 1 => renkli seviye (varsayılan renkli olarak okumasıdır) ==> (1 => Colourful Level (default is to read in color))

# Görüntüyü, dosya yolundan okur ==> (Reads the image from the file path)

img = cv2.imread(r"C:\Users\Semih\Pictures\resim.webp")

print(type(img))

# Görüntünün boyutlarını öğrenme ==> (Learning the dimensions of the image)
print(img.shape)

# Normalde 3 kanallı görüntüler RGB halindedir. ==> (Normally, 3-channel images are RGB.)
# opencv'de ise 3 kanallı görüntüler BGR halindedir ==> (In opencv, 3-channel images are in BGR state)

#Görüntüyü yeniden boyutlandırma (resize işlemi) ==> (Resizing the image (resize process))

# büyütmek için interplasyon = cv2.INTER_CUBIC
# interpolation to enlarge =  cv2.INTER_CUBIC
# küçültmek için interplasyon = cv2.INTER_AREA
# interpolation to shrink = cv2.INTER_AREA

#Artık her ikisi için de cv2.INTER_LANCZOS4 ==> (for both cv2.INTER_LANCZOS4)

my_resized_img = cv2.resize(img,(684,512),cv2.INTER_LANCZOS4)

cv2.imwrite(r"C:\Users\Semih\Pictures\resim.webp",my_resized_img)

img_b = img[:,:,0]
img_g = img[:,:,1]
img_r = img[:,:,2]

# Görüntüyü gösterir ==> (Shows the image)

cv2.imshow("Original Image",img)  #=> Orjinal resim
cv2.imshow("Blue Channel Image",img_b) #=> Mavi Kanal Resmi
cv2.imshow("Green Channel Image",img_g) #=) Yeşil Kanal Resmi
cv2.imshow("Red Channel Image",img_r) #=> Kırmızı Kanal Resmi
cv2.waitKey(0)
cv2.destroyAllWindows()
