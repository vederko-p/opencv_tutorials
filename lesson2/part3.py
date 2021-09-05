
# Read, Write, Show videos

import cv2


cap = cv2.VideoCapture(0)
# Для сохранения видео необходимо задействовать другой класс - cv2.VideoWriter:
fourcc = cv2.VideoWriter_fourcc(*'XVID')   # Спецификация FOURCC-кода
# или: cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')

out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
# Первый аргумент - имя файла
# Второй аргумент - FOURCC-код - для спецификации видео-кодека
# Подробнее о FOURCC: https://www.fourcc.org/codecs.php
# Третий аргумент - количество кадров/сек.
# Четвертый аругмент - размер кадра.

print(cap.isOpened())
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Сохранение видео (сохранение происходит покадрово)
        out.write(frame)
        # Видео будет сохранено в оригинальном цвете, так как мы сохраняем его
        # перед тем, как перевести в grayscale

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # маска & 0xFF применяется для 64-битных систем (если без маски не работает)
            break
    else:
        break

# Не забываем отчиситить память:
cap.release()
out.release()
cv2.destroyAllWindows()
