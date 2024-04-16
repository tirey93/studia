
import cv2

device = 0
# cap = cv2.VideoCapture(device)
cap = cv2.VideoCapture("Snooker2.mp4")
pos_frame = 0
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
while not cap.isOpened():
    cap = cv2.VideoCapture(device)
    print("Czekam")
    cv2.waitKey(2000)
keep = True
while keep:
    # t = time.time()
    flag, frame = cap.read()
    if flag:
        pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
        obraz_sz = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # obraz_fil = cv2.GaussianBlur(obraz_sz, (5, 5,), 0)
        obraz_kr = cv2.Canny(obraz_sz, 60, 150)
        cv2.imshow("Obraz", frame)
        # cv2.imshow("Filtr", obraz_fil)
        cv2.imshow("krawedzie", obraz_kr)
    else:
        cap.set(cv2.CAP_PROP_POS_FRAMES, pos_frame-1)
        print("ramka nie gotowa")
        cv2.waitKey(100)
    if cv2.waitKey(1) == 27:
        keep = False
        cv2.destroyAllWindows()
        break
cap.release()