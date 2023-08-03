import cv2
import numpy as np

# Resmi yükle
image = cv2.imread("images/isolated_kiwi.jpg")

# Koordinatları belirle (örneğin, x=100, y=150)
x, y = 50, 270

# Siyah blok boyutunu belirle (örneğin, 50x50 piksel)
block_width, block_height = 50, 50

# Siyah bir blok oluştur
black_block = np.zeros((block_height, block_width, 3), dtype=np.uint8)

# Resmin üzerine siyah bloğu yerleştir
image[y:y+block_height, x:x+block_width] = black_block

# Sonucu göster
cv2.imshow("final", image)
cv2.imwrite("images/final_kiwi.png", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
