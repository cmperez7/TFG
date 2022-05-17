from djitellopy import Tello


def mission_pads_control():
    tello = Tello()
    tello.connect()
    tello.streamon()

    # Configure Mission Pads
    tello.enable_mission_pads()

    # Set Downward Detection Only
    tello.set_mission_pad_detection_direction(0)

    # Tell Tello to Take Off
    print("Takeoff!")
    tello.takeoff()

    # Tell Tello to move down 30cm
    tello.move_down(30)

    # Detect Pad ID
    pad = tello.get_mission_pad_id()

    # Detect and React to Pads Until It Sees m4
    while pad != 4:

        if pad == 1:
            tello.rotate_clockwise(90)
            tello.move_forward(50)

        if pad == 2:
            tello.rotate_counter_clockwise(90)
            tello.move_forward(50)

        if pad == 3:
            tello.rotate_counter_clockwise(90)
            tello.move_forward(50)

        # Detect Pad ID
        pad = tello.get_mission_pad_id()

    tello.rotate_counter_clockwise(90)
    tello.move_forward(50)
    tello.rotate_clockwise(180)

    # Disable Detection
    tello.disable_mission_pads()

    # Tell Tello to Land
    tello.land()
    tello.end()

    # Tell us the flight has finished
    print("Flight Completed!")


