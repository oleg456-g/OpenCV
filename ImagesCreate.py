import cv2
import numpy as np

#Создаём фон
photo = np.zeros((450, 400, 3), dtype='uint8')
#Изменение цвета фона, формат BGR
# photo[10:100, 100:280] = 255, 10, 200
#Создаём квадрат
cv2.rectangle(photo, (290, 90), (100, 10), (255, 10, 200), thickness=cv2.FILLED)
#ДЕлаем линию по центру в методе shape 0 индекс высота
cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[1], photo.shape[0] // 2), (255, 10, 200), thickness=5 )

cv2.putText(photo, 'Hello', (225, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 4)

cv2.imshow('Photo', photo)
cv2.waitKey(0)
