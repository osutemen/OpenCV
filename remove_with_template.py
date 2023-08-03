import cv2
import numpy as np

def get_geometric_shape(approx, area, perimeter):
    # Konturun alanına ve çevresine göre şeklini belirle
    if perimeter <= 0:
        circularity = 0
    else:
        circularity = 4 * np.pi * area / (perimeter ** 2)

    if circularity > 0.7:
        return "Yarım Daire"
    elif len(approx) == 3:
        return "Üçgen"
    elif len(approx) == 4:
        x, y, w, h = cv2.boundingRect(approx)
        aspect_ratio = float(w) / h
        if 0.95 <= aspect_ratio <= 1.05:
            return "Kare"
        else:
            return "Dikdörtgen"
    elif len(approx) == 5:
        return "Beşgen"
    elif len(approx) > 5:
        # Hilal, yarıçapları farklı iki daireden oluşur.
        # Konturun alanına ve merkezine göre kontrol et
        (x, y), (major_axis, minor_axis), angle = cv2.fitEllipse(approx)
        if area > 1.5 * np.pi * (major_axis / 2) * (minor_axis / 2) and \
           area < 2.5 * np.pi * (major_axis / 2) * (minor_axis / 2):
            return "Hilal"
        else:
            return "Daire"
    else:
        return "Daire"

def main():
    # Resmi yükle
    image = cv2.imread("images/isolated_kiwi.jpg")

    # Resmi griye çevir ve bulanıklaştır
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Kenarları algıla
    edges = cv2.Canny(blurred, 50, 150)

    # Konturları bul
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Konturu yaklaşıklaştır
        epsilon = 0.04 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # Konturu çiz
        cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)

        # Konturun alanını ve çevresini al
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)

        # Konturun geometrik şeklini al
        shape = get_geometric_shape(approx, area, perimeter)

        # Şekli resimde göster (turuncu renkte)
        x, y = approx[0][0]
        cv2.putText(image, shape, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 165, 255), 2)

    # Sonuçları göster
    cv2.imshow("Geometrik Şekiller", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
