from djitellopy import Tello

if __name__ == '__main__':

    print('Connectivity test:')
    tello = Tello()
    tello.connect()
    print('\n')

    print('Streaming video test:')
    tello.streamon()
    print('\n')

    tello.end()
