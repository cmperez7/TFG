# simple example demonstrating how to control a Tello using your keyboard.
# When starting the script the Tello will takeoff, pressing ESC makes it land
#  and the script exit.

from djitellopy import Tello
import cv2, math, time
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# For webcam input:
hands = mp_hands.Hands(
    min_detection_confidence=0.5, min_tracking_confidence=0.5)

tello = Tello()
tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()

tello.takeoff()

while True:
    # In reality you want to display frames in a seperate thread. Otherwise
    #  they will freeze while the drone moves.
    image = frame_read.frame

    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow('Drone', image)

    key = cv2.waitKey(1) & 0xff
    if key == 27: # ESCArgument parsing
        break
    elif key == 32:  # Space
        if not in_flight:
            # Take-off drone
            tello.takeoff()
            in_flight = True

        elif in_flight:
            # Land tello
            tello.land()
            in_flight = False
    elif key == ord('f'):
        tello.move_forward(30)
    elif key == ord('b'):
        tello.move_back(30)
    elif key == ord('l'):
        tello.move_left(30)
    elif key == ord('r'):
        tello.move_right(30)
    elif key == ord('c'):
        tello.rotate_clockwise(30)
    elif key == ord('t'):
        tello.rotate_counter_clockwise(30)
    elif key == ord('u'):
        tello.move_up(30)
    elif key == ord('d'):
        tello.move_down(30)

hands.close()
tello.land()