from djitellopy import Tello

if __name__ == '__main__':

    print('Take off test:')
    tello = Tello()
    tello.connect()
    tello.takeoff()
    print('\n')

    print('Land test:')
    tello.land()
    print('\n')

    tello.end()