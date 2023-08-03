import cv2
import numpy as np

# 1. Resmi yükle ve NumPy dizisine dönüştür
gul_resmi = cv2.imread("images/result.jpeg")
gul_resmi = cv2.cvtColor(gul_resmi, cv2.COLOR_BGR2RGB)

# 2. Kırmızı rengin RGB kodu: (255, 0, 0)
# Mor rengin RGB kodu: (128, 0, 128)
red_color = np.array([128, 0, 0])
purple_color = np.array([10, 0, 10])

# 3. Kırmızı rengin olan pikselleri seç
mask = np.all(gul_resmi == red_color, axis=-1)

# 4. Mor rengin olan pikselleri kırmızı rengin pikselleri ile değiştir
gul_resmi[mask] = purple_color

# 5. Sonucu görselleştir
cv2.imshow("Mor Gul Resmi", gul_resmi)
cv2.waitKey(0)
cv2.destroyAllWindows()
