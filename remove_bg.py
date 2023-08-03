import cv2
import numpy as np

def isolate_kiwis(img_path, save_path):
    # İmajı oku
    img = cv2.imread(img_path)

    # Görüntüyü HSV renk uzayına dönüştür
    hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Arka planı yok etmek için renk aralığı belirle (örn. yeşil tonlar)
    lower_green = np.array([30, 50, 50])
    upper_green = np.array([90, 255, 255])

    # Renk aralığına uyan pikselleri beyaz, diğerlerini siyah yapacak maske oluştur
    mask = cv2.inRange(hsv_image, lower_green, upper_green)

    # Yaprakları filtrelemek için bir dizi maske oluştur
    leaf_mask = np.zeros_like(mask)

    # Daireleri ve yarım daireleri içeren bir maske oluştur
    kiwi_mask = np.zeros_like(mask)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        # Konturun dış hattını yaklaşık olarak bul
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # Daireler ve yarım daireler için kontrol yap ve maskeye ekle
        if len(approx) >= 8 and cv2.isContourConvex(approx):
            cv2.drawContours(kiwi_mask, [contour], -1, 255, thickness=cv2.FILLED)
        else:
            # Eğer kontur yarı çevresel ise yarım daire olarak kabul et ve maskeye ekle
            x, y, w, h = cv2.boundingRect(contour)
            aspect_ratio = w / float(h)
            if 0.7 <= aspect_ratio <= 1.3:
                cv2.drawContours(kiwi_mask, [contour], -1, 255, thickness=cv2.FILLED)
            else:
                # Kontur yarı çevresel değilse yaprak olarak kabul et ve yaprak maskesine ekle
                cv2.drawContours(leaf_mask, [contour], -1, 255, thickness=cv2.FILLED)

    # Yaprak maskesini kiwi maskesinden çıkararak sadece kivileri içeren maskeyi elde et
    kiwi_mask = cv2.bitwise_and(kiwi_mask, cv2.bitwise_not(leaf_mask))

    # Orijinal resme maskeyi uygula
    isolated_kiwis = cv2.bitwise_and(img, img, mask=kiwi_mask)

    # Sonucu dosyaya kaydet
    cv2.imwrite(save_path, isolated_kiwis)

    # Maskelenmiş resmi göster
    cv2.imshow("Isolated Kiwis", isolated_kiwis)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = "images/kiwi.jpeg"  # İmajın dosya yolunu doğru şekilde değiştirin
    save_path = "images/isolated_kiwi.jpg"  # Sonucun kaydedileceği dosya yolunu belirleyin
    isolate_kiwis(image_path, save_path)
