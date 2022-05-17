from djitellopy import Tello


class TelloKeyboardController:
    def __init__(self, tello: Tello):
        self.tello = tello

    def control(self, key):
        if key == ord('f'):
            self.tello.move_forward(30)
        elif key == ord('b'):
            self.tello.move_back(30)
        elif key == ord('l'):
            self.tello.move_left(30)
        elif key == ord('r'):
            self.tello.move_right(30)
        elif key == ord('c'):
            self.tello.rotate_clockwise(30)
        elif key == ord('t'):
            self.tello.rotate_counter_clockwise(30)
        elif key == ord('u'):
            self.tello.move_up(30)
        elif key == ord('d'):
            self.tello.move_down(30)
