
# Read, Write, Show videos

import cv2


# Для отображения уже записанного видео необходимо в
# качестве аргумента указать его название с соответсвующим расширением:
cap = cv2.VideoCapture('name.avi')
# cap содержит в себе некоторые свойства.

print(cap.isOpened())
while cap.isOpened():
    # Экземпляр класса cv2.VideoCapture предоставляет несколько методов, например -
    # is.Opened(). В случае неправильно указанного пути или имени файла метод вернет
    # False, в ином случае - True.

    ret, frame = cap.read()

    # Метод gate() позволяет получать свойства кадра:
    # Размеры кадра:
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # Все свойства:
    # https://docs.opencv.org/4.0.0/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
