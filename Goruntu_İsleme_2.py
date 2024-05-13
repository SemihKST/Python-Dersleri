import cv2
from PIL import Image
import numpy as np

dosya = "../../../manzara.png"

img = cv2.imread(r"C:\Users\Semih\Pictures\manzara.png")
print(img.shape)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

threshold = np.array([120,120,120])

mask = np.all(img_rgb > threshold, axis=-1)

img_rgb[mask] = (153, 217, 234)

cv2.imshow("Original Image",img)  #==>(Orjinal görüntü)
cv2.imshow("Turkuaz Goruntu", cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)) #==> (Turquoise image)
cv2.waitKey(0)
cv2.destroyAllWindows()