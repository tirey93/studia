import cv2
from utilities import *
from config import *
import sys

def main(starting_frame, th_min, th_max, blur):
    device = FILENAME
    cap = cv2.VideoCapture(device)

    if not cap.isOpened():
        print("Error: Could not open video file.")
        sys.exit()

    cap.set(cv2.CAP_PROP_POS_FRAMES, starting_frame)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    boxes = []

    ### MAIN LOOP ###
    while True:
        ret, frame = cap.read()
        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        thresh_belt, belt = prepare_frame(frame, th_min, th_max, blur)

        # Detect the boxes
        contours, _ = cv2.findContours(thresh_belt, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            (x, y, w, h) = cv2.boundingRect(cnt)
            if y <= ENTRY_BUFFER_HEIGHT:
                continue

            found,existing_box = try_find_box(boxes, x, y)
            if not found:
                if y >= ADDING_BOXES_LIMIT_Y:
                    continue
                # Add new box
                existing_box = Box(x, y, w, h)
                boxes.append(existing_box)
            existing_box.update_position(x, y)
            box_subframe = belt[y:y+h, x:x+w]
            qr = decode_qr_code(box_subframe)
            if qr:
                box_size, box_id = decode_qr_data(qr.data.decode('utf-8'))
                existing_box.update_qr_data(size=box_size, id=box_id)
            

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
            add_limits_to_frame(result_frame)
        result_frame, stats = add_info_panel(result_frame, boxes)
        cv2.imshow("result", result_frame)
        key = cv2.waitKey(1)
        # return stats # uncomment to calc the stats
        if key == 27: # ESC KEY
            break
        elif key == ord('r'):  # R KEYs
            # Debug purpose
            # Reset the video to the starting framer
            # for box in boxes:
            cap.set(cv2.CAP_PROP_POS_FRAMES, STARTING_FRAME)
            boxes.clear()
            continue

        current_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
        print(current_frame)
        if current_frame >= total_frames:
            # Reset the video to the beginning
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            
            # Clear the boxes list
            boxes.clear()
        
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main(STARTING_FRAME, FRAME_THRESHOLD_MIN, FRAME_THRESHOLD_MAX, BLUR)