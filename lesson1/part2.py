
# Небольшая практика
# Будем сохранять картинку в случае нажатия определенной клавиши

import cv2


img = cv2.imread('lena.jpg', -1)
cv2.imshow('image', img)
k = cv2.waitKey(0)
# внутри k будет лежать нажатая клавиша

if k == 27:  # Каждая клавиша имеет свой уникальный номер (27 ~ Esc)
    cv2.destroyAllWindows()
elif k == ord('s'):  # ord - встроенная в Python ф-я; возвращает номер клавиши
    cv2.imwrite('lena_practice_copy.png', img)
    cv2.destroyAllWindows()
