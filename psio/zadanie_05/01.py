
import cv2
import numpy as np
device = 0
# cap = cv2.VideoCapture(device)
cap = cv2.VideoCapture("Snooker2.mp4")
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_POS_FRAMES, 10)

flag, obraz = cap.read()
obraz = cv2.cvtColor(obraz, cv2.COLOR_BGR2RGB)
img = obraz[250:300, 250:300,:]
carr = img.reshape(-1, 3)
color = np.average(carr, axis=0)
# print(f"col: {color}")
print(np.shape(obraz))



# cv2.rectangle(obraz, (250, 250), (300, 300), color=(0, 0, 255), thickness=2)


cv2.imshow("Obraz", obraz)
cv2.waitKey(0)
cap.release()