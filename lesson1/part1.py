
# Read, Write, Show images

import cv2


# Чтение изображения:
img = cv2.imread('lena.jpg', 1)
# Первый аргумент - название изображения
# Второй аргумент - флаг:
# 1 - цветное изображение (cv2.IMREAD_COLOR)
# 0 - grayscale изображение (cv2.IMREAD_GRAYSCALE)
# -1 - изображение с alpha-каналом (cv2.IMREAD_UNCHANGED)

# Функция imread не возвращает ошибку в случае неверного имени или пути до картинки.
# В этом случае метод print() вернет None.

print(img)
# Результат - numpy-матрица (или матрицы в случае картинок с несколькими цветовыми каналами)

# Отображение картинки:
cv2.imshow('image', img)
# Первый аругмент - название окна, в котором будет открыто изображение
# Второй аругмент - изображение, прчитанное с помощью функции imread.

# imshow отобразит изображение на секунду. Необходимо добавить элемент, удерживающий изображение:

cv2.waitKey(5000)
# Аргумент - время ожидания в миллисекундах (по умолчанию None - ожидание будь сколь угодно долгим)

# Закроем все окна после ожидания:
cv2.destroyAllWindows()
# Данный метод закрывает все окна, которые мы создали

# Запишем изображение в файл:
cv2.imwrite('lena_copy.png', img)
# Первый аругмент - название будущего файла
# Второй аргумент - изображене, которое нужно сохранить
