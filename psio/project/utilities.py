import cv2
import numpy as np
from pyzbar.pyzbar import decode
from config import *

class Box:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.size = 0
        self.id = 0
        self.shouldBeDisplayed = True
        self.qrFound = False
        self.isInvalid = False
        self.framesPassed = 0

    def update_position(self, x, y):
        self.x = x
        self.y = y

    def update_qr_data(self, size, id):
        self.qrFound = True
        self.size = size
        self.id = id

    def get_bounding_rect(self):
        return self.x, self.y, self.w, self.h


def prepare_frame(frame):
    frame_resized = cv2.resize(frame, (FRAME_WIDTH, FRAME_HEIGHT))
    belt = frame_resized
    gray_belt = cv2.cvtColor(belt, cv2.COLOR_BGR2GRAY)
    blurred_belt = cv2.GaussianBlur(gray_belt, (17, 17), 0)
    _, thresh_belt = cv2.threshold(blurred_belt, FRAME_THRESHOLD_MIN, FRAME_THRESHOLD_MAX, cv2.THRESH_BINARY)
    kernel = np.ones((15, 15), np.uint8)
    cleaned_frame = cv2.morphologyEx(thresh_belt, cv2.MORPH_OPEN, kernel)
    return cleaned_frame, belt

def render_box_info(frame, box):
    (x, y, w, h) = box.get_bounding_rect()

    if box.qrFound:
        cv2.rectangle(frame, (x, y), (x + w, y + h), GREEN_COLOR, 2)
        cv2.putText(frame, f'size: {box.size}', (x, y - 39), 0, FONT_SCALE, GREEN_COLOR)
        cv2.putText(frame, f'id: {box.id}', (x, y - 22), 0, FONT_SCALE, GREEN_COLOR)
        cv2.putText(frame, f'area: {box.w * box.h / 100} cm2', (x, y - 5), 0, FONT_SCALE, GREEN_COLOR)
    
    elif box.isInvalid:
        cv2.rectangle(frame, (x, y), (x + w, y + h), RED_COLOR, 2)
        cv2.putText(frame, f'Error:', (x, y - 22), 0, FONT_SCALE, RED_COLOR)
        cv2.putText(frame, f'No QR code', (x, y - 5), 0, FONT_SCALE, RED_COLOR)
    
    return frame
def add_limits_to_frame(frame):
    cv2.line(frame, (0, ENTRY_BUFFER_HEIGHT), (500, ENTRY_BUFFER_HEIGHT), RED_COLOR)
    cv2.line(frame, (0, ADDING_BOXES_LIMIT_Y), (500, ADDING_BOXES_LIMIT_Y), RED_COLOR)
def decode_qr_data(qr_data):
    size_id = qr_data[:1]
    box_id = qr_data[1:]

    if size_id == 'A':
        return "Small", box_id
    if size_id == 'B':
        return "Medium", box_id
    if size_id == 'C':
        return "Large", box_id

def decode_qr_code(frame):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh_frame = cv2.threshold(gray_frame, QR_THRESHOLD_MIN, QR_THRESHOLD_MAX, cv2.THRESH_BINARY)
    decoded_qr_codes = decode(thresh_frame)

    if decoded_qr_codes:
        return decoded_qr_codes[0]
    
    return None

def try_find_box(boxes, x, y, tolerance=100):
    found_box:Box = None
    for box in boxes:
        if abs(box.x - x) <= tolerance and abs(box.y - y) <= tolerance and box.shouldBeDisplayed:
            found_box = box
            return True, found_box
    return False, found_box

def add_info_panel(frame, boxes):
    info_bar = np.zeros((FRAME_HEIGHT, FRAME_WIDTH + INFO_PANEL_WIDTH, 3), dtype=np.uint8)
    info_bar[0:FRAME_HEIGHT, 0:FRAME_WIDTH] = frame

    total_boxes = len(boxes)

    small_count = 0
    medium_count = 0
    large_count = 0
    invalid_count = 0
    unread_qrs = 0

    for box in boxes:
        if box.size == "Small":
            small_count += 1
        elif box.size == "Medium":
            medium_count += 1
        elif box.size == "Large":
            large_count += 1
        elif box.isInvalid == True:
            invalid_count += 1
        elif box.qrFound == False:
            unread_qrs += 1
        

    text_color = WHITE_COLOR

    y_position = 35
    cv2.putText(info_bar, f'Total number of boxes: {total_boxes}', (FRAME_WIDTH + 10, y_position),
                cv2.FONT_HERSHEY_SIMPLEX, INFO_PANEL_FONT_SCALE, text_color, 2)
    
    y_position += 100
    cv2.putText(info_bar, f'Number of small boxes: {small_count}', (FRAME_WIDTH + 10, y_position),
            cv2.FONT_HERSHEY_SIMPLEX, INFO_PANEL_FONT_SCALE, text_color, 2)
    
    y_position += 30
    cv2.putText(info_bar, f'Number of medium boxes: {medium_count}', (FRAME_WIDTH + 10, y_position),
            cv2.FONT_HERSHEY_SIMPLEX, INFO_PANEL_FONT_SCALE, text_color, 2)
    
    y_position += 30
    cv2.putText(info_bar, f'Number of large boxes: {large_count}', (FRAME_WIDTH + 10, y_position),
            cv2.FONT_HERSHEY_SIMPLEX, INFO_PANEL_FONT_SCALE, text_color, 2)
    
    y_position += 100
    if invalid_count != 0:
        text_color = DARK_RED_COLOR

    cv2.putText(info_bar, f'Number of invalid boxes: {invalid_count}', (FRAME_WIDTH + 10, y_position),
        cv2.FONT_HERSHEY_SIMPLEX, INFO_PANEL_FONT_SCALE, text_color, 2)
    y_position += 30
    cv2.putText(info_bar, f'Number of unread qrs: {unread_qrs}', (FRAME_WIDTH + 10, y_position),
        cv2.FONT_HERSHEY_SIMPLEX, INFO_PANEL_FONT_SCALE, text_color, 2)

    return info_bar