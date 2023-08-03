import cv2


def main():
    # Resmi yükle
    image_path = "images/kiwi.jpeg"
    image = cv2.imread(image_path)

    # Kivi sınıflandırıcısını yükle (Dilerseniz daha fazla sınıflandırıcı ekleyebilirsiniz.)
    kivi_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    # Grayscale çevirme
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Nesneleri tespit et
    kiviler = kivi_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

    # Tespit edilen kivileri işaretle
    for (x, y, w, h) in kiviler:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, "Kivi", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Sonucu göster
    cv2.imshow("Kiviler", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
