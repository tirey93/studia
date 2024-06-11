import cv2
from utilities import *
from config import *

device = FILENAME
cap = cv2.VideoCapture(device)

cap.set(cv2.CAP_PROP_POS_FRAMES, STARTING_FRAME)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

boxes = []

### MAIN LOOP ###
while True:
    ret, frame = cap.read()
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    thresh_belt, belt = prepare_frame(frame)

    # Detect the boxes
    contours, _ = cv2.findContours(thresh_belt, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)
        if y <= ENTRY_BUFFER_HEIGHT:
            continue

        try:
            existing_box = box_exists(boxes, x, y)
            existing_box.update_position(x, y)
            if not existing_box.qrFound:
                box_subframe = belt[y:y+h, x:x+w]
                qr = decode_qr_code(box_subframe)
                if qr:
                    box_size, box_id = decode_qr_data(qr.data.decode('utf-8'))
                    existing_box.update_qr_data(size=box_size, id=box_id)
        except BoxNotFoundException:
            if y >= ADDING_BOXES_LIMIT_Y:
                continue
            # Add new box
            box = Box(x, y, w, h)
            boxes.append(box)

    result_frame = belt
    # Iterate through all the boxes and process them
    for box in boxes:
        box.framesPassed += 1

        if box.framesPassed >= AMOUNT_OF_FRAMES_TO_READ_THE_QR and box.qrFound == False:
            box.isInvalid = True

        if box.y >= DISPLAY_LIMIT_Y:
            box.shouldBeDisplayed = False

        if box.shouldBeDisplayed:
            result_frame = render_box_info(result_frame, box)

    result_frame = add_info_panel(result_frame, boxes)

    cv2.imshow("result", result_frame)
    key = cv2.waitKey(1)
    if key == 27: # ESC KEY
        break
    elif key == ord('r'):  # R KEY
        # Debug purpose
        # Reset the video to the starting frame
        cap.set(cv2.CAP_PROP_POS_FRAMES, STARTING_FRAME)
        boxes.clear()
        continue

    current_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
    if current_frame >= total_frames:
        # Reset the video to the beginning
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        
        # Clear the boxes list
        boxes.clear()

cap.release()
cv2.destroyAllWindows()
