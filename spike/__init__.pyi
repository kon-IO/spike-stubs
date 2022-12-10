from typing import Literal, TypeAlias, Optional, Tuple, Union

PortLetter: TypeAlias = Literal["A", "B", "C", "D", "E", "F"]


class Motor:
    """To use the motors, you must first initialize them.

    Example
    -------
    ::

        from spike import Motor


        # Initialize the motor
        motor = Motor('A')

    """

    def __init__(self, port: PortLetter) -> None: ...

    def run_to_position(self, degrees: int, direction: Literal["Shortest path", "Clockwise", "Counterclockwise"] = "Shortest path", speed: Optional[int] = None) -> None:
        """Runs the motor to an absolute position.
        The sign of the speed will be ignored (i.e., absolute value), and the motor will always travel in the direction that’s been specified by the "direction" parameter. If the speed is greater than "100," it will be limited to "100."

        Parameters
        ----------
        degrees : int
            The target position (0 to 359 inclusive).
        direction : Literal[&quot;Shortest path&quot;, &quot;Clockwise&quot;, &quot;Counterclockwise&quot;], optional
            The direction to use to reach the target position.
            "Shortest path" could run in either direction, depending on the shortest distance to the target. "Clockwise" will make the motor run clockwise until it reaches the target position. "Counterclockwise" will make the motor run counterclockwise until it reaches the target position. By default "Shortest path"
        speed : Optional[int], optional
            The motor’s speed.
            If no value is specified, it will use the default speed that’s been set by set_default_speed(). By default None

        Raises
        ------
        TypeError
            degrees or speed is not an integer or direction is not a string.
        ValueError
            direction is not one of the allowed values or degrees is not within the range of 0-359 (both inclusive).
        RuntimeError
            The motor has been disconnected from the Port.


        Example
        -------
        ::

            from spike import Motor

            motor = Motor('A')


            # Set the motor to position "0," aligning the markers

            motor.run_to_position(0)
        """

    def run_to_degrees_counted(self, degrees: int, speed: Optional[int] = None) -> None:
        """Runs the motor until the number of degrees counted is equal to the value that has been specified by the "degrees" parameter.
        The sign of the speed will be ignored, and the motor will always travel in the direction required to reach the specified number of degrees. If the speed is greater than "100," it will be limited to "100."

        Parameters
        ----------
        degrees : int
            The target degrees counted.
        speed : Optional[int], optional
            The desired speed (always positive or 0), by default None

        Raises
        ------
        TypeError
            degrees or speed is not an integer.
        RuntimeError
            The motor has been disconnected from the Port.


        Example
        -------
        ::

            from spike import Motor
            from spike.control import wait_for_seconds

            motor = Motor('A')

            for deg in range(0, 721, 90):
                motor.run_to_degrees_counted(deg)
                wait_for_seconds(1)
        """

    def run_for_degrees(self, degrees: int, speed: Optional[int] = None) -> None:
        """Runs the motor for a specified number of degrees.

        Parameters
        ----------
        degrees : int
            The number of degrees that the motor should run.
        speed : Optional[int], optional
            The motor’s speed. If no value is specified (None), it will use the default speed that’s been set by set_default_speed(). By default None

        Raises
        ------
        TypeError
            degrees or speed is not an integer.
        RuntimeError
            The motor has been disconnected from the Port.


        Example
        -------
        ::

            from spike import Motor

            motor = Motor('A')


            # Run the motor 90 degrees clockwise

            motor.run_for_degrees(90)


            # Run the motor 90 degrees counterclockwise

            motor.run_for_degrees(-90)


            # Run the motor 360 degrees clockwise at maximum (100%) speed

            motor.run_for_degrees(360, 100)

        """

    def run_for_rotations(self, rotations: float, speed: Optional[int] = None) -> None:
        """Runs the motor for a specified number of rotations.

        Parameters
        ----------
        rotations : float
            The number of rotations that the motor should run.
        speed : Optional[int], optional
            The motor’s speed. If no value is specified (None), it will use the default speed that’s been set by set_default_speed(). By default None

        Raises
        ------
        TypeError
            rotations is not a number or speed is not an integer.
        RuntimeError
            The motor has been disconnected from the Port.


        Example
        -------
        ::

            from spike import Motor

            motor = Motor('A')


            # Run the motor 90 degrees clockwise:

            motor.run_for_rotations(0.25)


            # Run the motor 90 degrees counterclockwise:

            motor.run_for_rotations(-0.25)

        """

    def run_for_seconds(self, seconds: float, speed: Optional[int] = None) -> None:
        """Runs the motor for a specified number of seconds.

        Parameters
        ----------
        seconds : float
            The number of seconds for which the motor should run.
        speed : Optional[int], optional
            The motor’s speed. If no value is specified (None), it will use the default speed that’s been set by set_default_speed(). By default None

        Raises
        ------
        TypeError
            seconds is not a number or speed is not an integer.
        RuntimeError
            The motor has been disconnected from the Port.


        Example
        -------
        ::

            from spike import Motor

            motor = Motor('A')


            # Run clockwise for half a second at 75% speed

            motor.run_for_seconds(0.5, 75)


            # Run counterclockwise for 6 seconds at 30% speed

            motor.run_for_seconds(6, -30)
        """

    def start(self, speed: Optional[int] = None) -> None:
        """Starts running the motor at a specified speed.
        The motor will keep moving at this speed until you give it another motor command or when your program ends.

        Parameters
        ----------
        speed : Optional[int], optional
            The motor’s speed. If no value is specified, it will use the default speed that’s been set by set_default_speed(). By default None

        Raises
        ------
        TypeError
            speed is not an integer.
        RuntimeError
            The motor has been disconnected from the Port.


        Example
        -------
        ::

            from spike import Motor

            motor = Motor('A')

            motor.start()

            # wait until something

            motor.stop()

        """

    def stop(self) -> None:
        """Stops the motor.
        What the motor does after it stops depends on the action that’s been set in set_stop_action(). The default value of set_stop_action() is "coast."

        Raises
        ------
        RuntimeError
            The motor has been disconnected from the Port.

        Example
        -------
        ::

            from spike import Motor

            motor = Motor('A')

            motor.start()

            # wait until something

            motor.stop()

        """

    def start_at_power(self, power: int) -> None:
        """Starts rotating the motor at a specified power level.
        The motor will keep moving at this power level until you give it another motor command or when your program ends.

        Parameters
        ----------
        power : int
            Power of the motor (-100 to 100 both inclusive).

        Raises
        ------
        TypeError
            power is not an integer.
        RuntimeError
            The motor has been disconnected from the Port.
        """

    def get_speed(self) -> int:
        """Retrieves the motor speed.

        Returns
        -------
        int
            The motor’s current speed (-100 to 100 both inclusive)

        Raises
        ------
        RuntimeError
            The motor has been disconnected from the Port.
        """

    def get_position(self) -> int:
        """Retrieves the motor position. This is the clockwise angle between the moving marker and the zero-point marker on the motor.

        Returns
        -------
        int
            The motor’s position (0 to 359 both inclusive).

        Raises
        ------
        RuntimeError
            The motor has been disconnected from the Port.
        """

    def get_degrees_counted(self) -> int:
        """Retrieves the number of degrees that have been counted by the motor.

        Returns
        -------
        int
            The number of degrees that’s been counted.

        Raises
        ------
        RuntimeError
            The motor has been disconnected from the Port.
        """

    def get_default_speed(self) -> int:
        """Retrieves the current default motor speed.

        Returns
        -------
        int
            The default motor’s speed (-100 to 100 both inclusive).
        """

    def was_interrupted(self) -> bool:
        """Tests whether the motor was interrupted.

        Returns
        -------
        bool
            True if the motor was interrupted since the last time was_interrupted() was called, otherwise false.

        Raises
        ------
        RuntimeError
            The motor has been disconnected from the Port.

        Example
        -------
        ::

            from spike import Motor

            motor = Motor('A')

            motor.run_for_rotations(2)
            if motor.was_interrupted():
                # the motor did not complete two rotations
        """

    def was_stalled(self) -> bool:
        """Tests whether the motor was stalled.

        Returns
        -------
        bool
            True if the motor has stalled since the last time was_stalled() was called, otherwise false.

        Raises
        ------
        RuntimeError
            The motor has been disconnected from the Port.

        Example
        -------
        ::

            from spike import Motor

            motor = Motor('A')

            motor.set_stall_detection(True)
            motor.run_for_rotations(2)
            if motor.was_stalled():
                # the motor did not complete two rotations
        """

    def set_degrees_counted(self, degrees_counted: int) -> None:
        """Sets the "number of degrees counted" to the desired value.

        Parameters
        ----------
        degrees_counted : int
            The value to which the number of degrees counted should be set.

        Raises
        ------
        TypeError
            degrees_counted is not an integer.
        RuntimeError
            The motor has been disconnected from the Port.
        """

    def set_default_speed(self, default_speed: int) -> None:
        """Sets the default motor speed. This speed will be used when you omit the speed argument in one of the other methods, such as run_for_degrees.
        Setting the default speed does not affect any motors that are currently running.
        It will only have an effect when another motor method is called after this method.
        If the value of default_speed is outside of the allowed range, the default speed will be set to "-100" or "100" depending on whether the value is negative or positive.

        Parameters
        ----------
        default_speed : int
            The default speed value (-100 to 100 inclusive).

        Raises
        ------
        TypeError
            default_speed is not an integer.
        """

    def set_stop_action(self, action: Literal["coast", "brake", "hold"] = "coast") -> None:
        """Sets the default behavior when a motor stops.

        Parameters
        ----------
        action : Literal[&quot;coast&quot;, &quot;brake&quot;, &quot;hold&quot;], optional
            The desired motor behavior when the motor stops. By default "coast"

        Raises
        ------
        TypeError
            action is not a string.
        ValueError
            action is not one of the allowed values.
        RuntimeError
            The motor has been disconnected from the Port.
        """

    def set_stall_detection(self, stop_when_stalled: bool = True) -> None:
        """Turns stall detection on or off.
        Stall detection senses when a motor has been blocked and can’t move. If stall detection has been enabled and a motor is blocked, the motor will be powered off after two seconds and the current motor command will be interrupted. If stall detection has been disabled, the motor will keep trying to run and programs will "get stuck" until the motor is no longer blocked.
        Stall detection is enabled by default.

        Parameters
        ----------
        stop_when_stalled : bool, optional
            Choose "true" to enable stall detection or "false" to disable it. By default True

        Raises
        ------
        TypeError
            stop_when_stalled is not a boolean.
        RuntimeError
            The motor has been disconnected from the Port.
        """


_Unit: TypeAlias = Literal["cm", "in", "rotations", "degrees", "seconds"]


class MotorPair:
    """MotorPair objects are used to control 2 motors simultaneously in opposite directions.
    To be able to use MotorPair, you must initialize both motors.

    Example
    -------
    ::

        from spike import MotorPair


        # If the left motor is connected to Port B

        # And the right motor is connected to Port A
        motor_pair = MotorPair('B', 'A')

    """

    def __init__(self, motor_a: PortLetter, motor_b: PortLetter) -> None: ...

    def move(self, amount: float, unit: _Unit = 'cm', steering: int = 0, speed: Optional[int] = None) -> None:
        """Start both motors simultaneously to move a Driving Base.

        Steering = "0" makes the Driving Base go straight. Negative numbers make the Driving Base turn left. Positive numbers make the Driving Base turn right.

        The program will not continue until the specified value is reached.

        If the value of steering is equal to "-100" or "100," the Driving Base will perform a rotation on itself (i.e., "tank move") at the default speed of each motor.

        If the value of steering is outside of the allowed range, the value will be set to "-100" or "100," depending on whether the value is positive or negative.

        If speed is outside of the allowed range, the value will be set to "-100" or "100," depending on whether the value is positive or negative.

        If the speed is negative, the Driving Base will move backward instead of forward. Likewise, if the "amount" is negative, the Driving Base will move backward instead of forward. If both the speed and the "amount" are negative, the Driving Base will move forward.

        When the specified unit is "cm" or "in," the "amount" of the unit parameter is equal to the horizontal distance that the Driving Base will travel before stopping. The relationship between the motor rotations and distance traveled can be adjusted by calling set_motor_rotation().

        When the "unit" is "rotations" or "degrees," the "amount" parameter value specifies how much the motor axle will turn before stopping.

        When the "unit" is "seconds," the "amount" parameter value specifies the duration that the motors will run before stopping.


        Parameters
        ----------
        amount : float
            The quantity to move in relation to the specified unit of measurement.
        unit : _Unit, optional
            The unit of measurement specified for the "amount" parameter. By default 'cm'
        steering : int, optional
            The direction and quantity to steer the Driving Base (-100 to 100 both inclusive). By default 0
        speed : Optional[int], optional
            The motor speed (-100 to 100 both inclusive). By default None

        Raises
        ------
        TypeError
            amount is not a number, or steering or speed is not an integer, or unit is not a string.
        ValueError
            unit is not one of the allowed values.
        RuntimeError
            One or both of the motors has been disconnected or the motors could not be paired.

        Example
        -------
        ::

            import math
            from spike import MotorPair

            motor_pair = MotorPair('B', 'A')


            # turn a Driving Base 180 degrees in place (if wheels are 8.1 cm apart)

            motor_pair.move(8.1 * math.pi / 2, 'cm', steering=100)

        """

    def start(self, steering: int = 0, speed: Optional[int] = None) -> None:
        """Start both motors simultaneously to move a Driving Base.

        Steering = "0" makes the Driving Base go straight. Negative numbers make the Driving Base turn left. Positive numbers make the Driving Base turn right.

        The program flow is not interrupted. This is most likely interrupted by sensor input and a condition.

        If the value of steering is equal to "-100" or "100," the Driving Base will perform a rotation on itself (i.e., "tank move") at the default speed of each motor.

        If the value of "steering" is outside of the allowed range, the value will be set to "-100" or "100," depending on whether the value is positive or negative.

        If speed is outside of the allowed range, the value will be set to "-100" or "100," depending on whether the value is positive or negative.

        If the speed is negative, the Driving Base will move backward instead of forward. Likewise, if the "amount" is negative, the Driving Base will move backward instead of forward. If both the speed and the "amount" are negative, the Driving Base will move forward.


        Parameters
        ----------
        steering : int, optional
            The direction and quantity to steer the Driving Base (-100 to 100 both inclusive). by default 0
        speed : Optional[int], optional
            The speed at which the Driving Base will move while performing a curve (-100 to 100 both inclusive). by default None

        Raises
        ------
        TypeError
            steering or speed is not an integer.
        RuntimeError
            One or both of the motors has been disconnected or the motors could not be paired.

        Example
        -------
        ::

            from spike import MotorPair

            motor_pair = MotorPair('B', 'A')

            motor_pair.start()

            # wait for something

            motor_pair.stop()
        """

    def stop(self) -> None:
        """Stops both motors simultaneously, which will stop a Driving Base.

        The motors will either actively hold their current position or coast freely depending on the option that’s been selected by set_stop_action().

        Raises
        ------
        RuntimeError
            One or both of the motors has been disconnected or the motors could not be paired.

        Example
        -------
        ::

            from spike import MotorPair

            motor_pair = MotorPair('B', 'A')

            motor_pair.start()

            # wait for something

            motor_pair.stop()

        """

    def move_tank(self, amount: float, unit: _Unit = "cm", left_speed: Optional[int] = None, right_speed: Optional[int] = None) -> None:
        """Moves the Driving Base using differential (tank) steering.

        The speed of each motor can be controlled independently for differential (tank) drive Driving Bases.

        When the specified unit is "cm" or "in," the "amount" of the unit parameter is equal to the horizontal distance that the Driving Base will travel before stopping. The relationship between the motor rotations and distance traveled can be adjusted by calling set_motor_rotation().

        When the "unit" is "rotations" or "degrees," the "amount" parameter value specifies how much the motor axle will turn before stopping.

        When the "unit" is "seconds," the "amount" parameter value specifies the duration that the motors will run before stopping.

        If left_speed or right_speed is outside of the allowed range, the value will be set to "-100" or "100" depending on whether the value is positive or negative.

        If one of the speeds (i.e., left_speed or right_speed) is negative, the negative-speed motor will run backward instead of forward. If the "amount" parameter value is negative, both motors will rotate backward instead of forward. If both of the speed values (i.e., left_speed and right_speed) are negative and the "amount" parameter value is negative, both motors will rotate forward.

        The program will not continue until the specified value is reached.


        Parameters
        ----------
        amount : float
            The quantity to move in relation to the specified unit of measurement.
        unit : _Unit, optional
            The unit of measurement specified for the "amount" parameter. By default "cm"
        left_speed : Optional[int], optional
            The speed of the left motor. If None, left_speed will be the speed set by set_default_speed(). By default None
        right_speed : Optional[int], optional
            The speed of the right motor. If None, right_speed will be the speed set by set_default_speed(). By default None

        Raises
        ------
        TypeError
            amount, left_speed or right_speed is not a number or unit is not a string.
        ValueError
            unit is not one of the allowed values.
        RuntimeError
            One or both of the Ports do not have a motor connected or the motors could not be paired.

        Example
        -------
        ::

            from spike import MotorPair

            motor_pair = MotorPair('B', 'A')
            motor_pair.move_tank(10, 'cm', left_speed=25, right_speed=75)

        """

    def start_tank(self, left_speed: int, right_speed: int) -> None:
        """Starts moving the Driving Base using differential (tank) steering.

        The speed of each motor can be controlled independently for differential (tank) drive Driving Bases.

        If left_speed or right_speed is outside of the allowed range, the value will be set to "-100" or "100" depending on whether the value is positive or negative.

        If the speed is negative, the motors will move backward instead of forward.

        The program flow is not interrupted. This is most likely interrupted by sensor input and a condition.


        Parameters
        ----------
        left_speed : int
            The speed of the left motor.
        right_speed : int
            The speed of the right motor.

        Raises
        ------
        TypeError
            left_speed or right_speed is not an integer
        RuntimeError
            One or both of the Ports do not have a motor connected or the motors could not be paired.

        Example
        -------
        ::

            from spike import MotorPair

            motor_pair = MotorPair('B', 'A')


            # Rotate the Driving Base in place to the right

            motor_pair.start_tank(100, -100)

        """

    def start_at_power(self, power: int, steering: int = 0) -> None:
        """Starts moving the Driving Base without speed control.

        The motors can also be driven without speed control. This is useful when using your own control algorithm (e.g., a proportional line-follower).

        If the steering is outside of the allowed range, the value will be set to "-100" or "100" depending on whether the value is positive or negative.

        If the power is outside of the allowed range, the value will be set to "-100" or "100" depending on whether the value is positive or negative.

        If the power is negative, the Driving Base will move backward instead of forward.

        The program flow is not interrupted. This can most likely be interrupted by sensor input and a condition.


        Parameters
        ----------
        power : int
            The amount of power to send to the motors (-100 to 100 both inclusive).
        steering : int, optional
            The steering direction (-100 to 100). "0" makes the Driving Base move straight. Negative numbers make the Driving Base turn left. Positive numbers make the Driving Base turn right. By default 0

        Raises
        ------
        TypeError
            steering or power is not an integer.
        RuntimeError
            One or both of the Ports do not have a motor connected or the motors could not be paired.

        Example
        -------
        ::

            from spike import MotorPair, ColorSensor

            motor_pair = MotorPair('B', 'A')
            color_sensor = ColorSensor('F')

            while True:
                steering = color_sensor.get_reflected_light() - 50
                motor_pair.start_at_power(50, steering)

        """

    def start_tank_at_power(self, left_power: int, right_power: int) -> None:
        """Starts moving the Driving Base using differential (tank) steering without speed control.

        The motors can also be driven without speed control. This is useful when using your own control algorithm (e.g., a proportional line-follower).

        If the left_power or right_power is outside of the allowed range, the value will be rounded to "-100" or "100" depending on whether the value is positive or negative.

        If the power is a negative value, the corresponding motor will move backward instead of forward.

        The program flow is not interrupted. This can most likely be interrupted by sensor input and a condition.


        Parameters
        ----------
        left_power : int
            The power of the left motor.
        right_power : int
            The power of the right motor.

        Raises
        ------
        TypeError
            left_power or right_power is not an integer.
        RuntimeError
            One or both of the Ports do not have a motor connected or the motors could not be paired.

        Example
        -------
        ::

            from spike import MotorPair

            motor_pair = MotorPair('B', 'A')

            # Rotate the Driving Base in place to the right

            motor_pair.start_tank_at_power(100, -100)
        """

    def get_default_speed(self) -> int:
        """Retrieves the default motor speed.

        Returns
        -------
        int
            The default motor speed (-100 to 100 both inclusive).
        """

    def set_motor_rotation(self, amount: float = 17.6, unit: Literal["cm", "in"] = "cm") -> None:
        """Sets the ratio of one motor rotation to the distance traveled.

        If there are no gears used between the motors and the wheels of the Driving Base, the "amount" is the circumference of one wheel.

        Calling this method does not affect the Driving Base if it’s already running. It will only have an effect the next time one of the move or start methods is used.


        Parameters
        ----------
        amount : float, optional
            The distance that the Driving Base moves when both motors move one rotation each. By default 17.6
        unit : Literal[&quot;cm&quot;, &quot;in&quot;], optional
            The unit of measurement specified for the "amount" parameter. By default "cm"

        Raises
        ------
        TypeError
            amount is not a number or unit is not a string.
        ValueError
            unit is not one of the allowed values.

        Example
        -------
        ::

            import math
            from spike import MotorPair

            motor_pair = MotorPair('B', 'A')

            # The SPIKE Prime wheels have a diameter of 17.6 cm Multiplying by "π" gives the distance traveled (circumference)

            motor_pair.set_motor_rotation(17.6 * math.pi, 'cm')
        """

    def set_default_speed(self, speed: int) -> None:
        """Sets the default motor speed.

        If speed is outside of the allowed range, the value will be set to "-100" or "100" depending on whether the value is positive or negative.

        Setting the speed will not have any effect until one of the move or start methods is called, even if the Driving Base is already moving.


        Parameters
        ----------
        speed : int
            The default motor speed.

        Raises
        ------
        TypeError
            speed is not a number.
        """

    def set_stop_action(self, action: Literal["brake", "hold", "coast"] = "coast") -> None:
        """Sets the motor action that will be used when the Driving Base stops.

        If the action is "brake," the motors will stop quickly and be allowed to turn freely.

        If the action is "hold," the motors will actively hold their current position and cannot be turned manually.

        If the action is set to "coast," the motors will stop slowly and can be turned freely.

        Setting the "stop" action does not take immediate effect on the motors. The setting will be saved and used whenever stop() is called or when one of the move methods has completed without being interrupted.


        Parameters
        ----------
        action : Literal[&quot;brake&quot;, &quot;hold&quot;, &quot;coast&quot;], optional
            The desired action of the motors when the Driving Base stops. By default "coast"

        Raises
        ------
        TypeError
            action is not a string.
        ValueError
            action is not one of the allowed values.

        Example
        -------
        ::

            from spike import MotorPair

            motor_pair = MotorPair('B', 'A')


            # Allow the motors to turn freely after stopping

            motor_pair.set_stop_action('coast')

        """


_Color: TypeAlias = Literal['black', 'violet', 'blue',
                            'cyan', 'green', 'yellow', 'red', 'white', None]


class ColorSensor:
    """To use the Color Sensor, you must first initialize it.

    Example
    -------
    ::

        from spike import ColorSensor


        # Initialize the Color Sensor
        color = ColorSensor('E')

    """

    def __init__(self, port: PortLetter) -> None: ...

    def get_color(self) -> _Color:
        """Retrieves the detected color of a surface.

        Returns
        -------
        _Color
            Name of the color.

        Raises
        ------
        RuntimeError
            The sensor has been disconnected from the Port.

        Example
        -------
        ::

            from spike import ColorSensor


            # Initialize the Color Sensor

            paper_scanner = ColorSensor('E')


            # Measure the color

            color = paper_scanner.get_color()


            # Print the color name to the console

            print('Detected:', color)


            # Check if it's a specific color

            if color == 'red':
                print('It is red!')
        """

    def get_ambient_light(self) -> int:
        """Retrieves the intensity of the ambient light.

        This causes the Color Sensor to change modes, which can affect your program in unexpected ways. For example, the Color Sensor can't read colors when it's in ambient light mode.

        Returns
        -------
        int
            The ambient light intensity (0 to 100 both inclusive).

        Raises
        ------
        RuntimeError
            The sensor has been disconnected from the Port.
        """

    def get_reflected_light(self) -> int:
        """Retrieves the intensity of the reflected light.

        Returns
        -------
        int
            The reflected light intensity (0 to 100 inclusive).

        Raises
        ------
        RuntimeError
            The sensor has been disconnected from the Port.
        """

    def get_rgb_intensity(self) -> Tuple[int, int, int, int]:
        """Retrieves the overall color intensity, and intensity of red, green, and blue.

        Returns
        -------
        Tuple[int, int, int]
            Tuple that holds the RGB and overall intensities (0 to 1024 each).

        Raises
        ------
        RuntimeError
            The sensor has been disconnected from the Port.
        """

    def get_red(self) -> int:
        """Retrieves the color intensity of red.

        Returns
        -------
        int
            Intensity (0 to 1024)

        Raises
        ------
        RuntimeError
            The sensor has been disconnected from the Port.
        """

    def get_green(self) -> int:
        """Retrieves the color intensity of green.

        Returns
        -------
        int
            Intensity (0 to 1024)

        Raises
        ------
        RuntimeError
            The sensor has been disconnected from the Port.
        """

    def get_blue(self) -> int:
        """Retrieves the color intensity of blue.

        Returns
        -------
        int
            Intensity (0 to 1024)

        Raises
        ------
        RuntimeError
            The sensor has been disconnected from the Port.
        """

    def wait_until_color(self, color: _Color) -> None:
        """Waits until the Color Sensor detects the specified color.

        Parameters
        ----------
        color : _Color
            The name of the color

        Raises
        ------
        TypeError
            color is not a string or None.
        ValueError
            color is not one of the allowed values.
        RuntimeError
            The sensor has been disconnected from the Port.

        Example
        -------
        ::

            from spike import ColorSensor

            color_sensor = ColorSensor('A')

            color_sensor.wait_until_color('blue')

            # Add actions after this

        """

    def wait_for_new_color(self) -> _Color:
        """Waits until the Color Sensor detects a new color.

        The first time this method is called, it immediately returns the detected color. After that, it waits until the Color Sensor detects a color that’s different from the color that was detected the last time this method was used.

        Returns
        -------
        _Color
            The name of the new color

        Raises
        ------
        RuntimeError
            The sensor has been disconnected from the Port.

        Example
        -------
        ::

            from spike import ColorSensor

            color_sensor = ColorSensor('A')

            while True:
                color = color_sensor.wait_for_new_color()
                if color == 'black':
                    # For example, steer left
                elif color == 'white':
                    # For example, steer right

        """

    def light_up_all(self, brightness: int = 100) -> None:
        """Lights up all of the lights on the Color Sensor at the specified brightness.

        This causes the Color Sensor to change modes, which can affect your program in unexpected ways. For example, the Color Sensor can't read colors when it's in light up mode.

        Parameters
        ----------
        brightness : int, optional
            The desired brightness of the lights on the Color Sensor (0 is off, 100 is full brightness), by default 100

        Raises
        ------
        TypeError
            brightness is not an integer.
        RuntimeError
            The sensor has been disconnected from the Port.
        """

    def light_up(self, light_1: int, light_2: int, light_3: int) -> None:
        """Sets the brightness of the individual lights on the Color Sensor.

        This causes the Color Sensor to change modes, which can affect your program in unexpected ways. For example, the Color Sensor can't read colors when it's in light up mode.

        Parameters
        ----------
        light_1 : int
            The desired brightness of light 1 (0 is off, 100 is full brightness).
        light_2 : int
            The desired brightness of light 2 (0 is off, 100 is full brightness).
        light_3 : int
            The desired brightness of light 3 (0 is off, 100 is full brightness).

        Raises
        ------
        TypeError
            light_1, light_2, or light_3 is not an integer.
        RuntimeError
            The sensor has been disconnected from the Port.
        """


_Gesture_With_none: TypeAlias = Literal["shaken",
                                        "tapped", "double-tapped", "falling", "none"]
_Gesture: TypeAlias = Literal["shaken", "tapped", "double-tapped", "falling"]
_Orientation: TypeAlias = Literal["front",
                                  "back", "up", "down", "leftside", "rightside"]


class MotionSensor:
    """Do not instantiate this class manually. Use hub = PrimeHub(); hub.motion_sensor instead.
    """

    def __init__(self) -> None: ...

    def was_gesture(self, gesture: _Gesture_With_none) -> bool:
        """Tests whether a gesture has occurred since the last time was_gesture() was used, or since the beginning of the program (for the first use).

        Parameters
        ----------
        gesture : _Gesture
            The name of the gesture.

        Returns
        -------
        bool
            True if the gesture has occurred since the last time was_gesture() was called, otherwise false.

        Raises
        ------
        TypeError
            gesture is not a string.
        ValueError
            gesture is not one of the allowed values.

        Example
        -------
        ::

            from spike import PrimeHub
            from spike.control import wait_for_seconds

            hub = PrimeHub()

            wait_for_seconds(5)
            if hub.motion_sensor.was_gesture('shaken'):
                # the Hub was shaken some time within the last 5 seconds
        """

    def wait_for_new_gesture(self) -> _Gesture:
        """Waits until a new gesture happens.

        Returns
        -------
        _Gesture
            The new gesture.

        Example
        -------
        ::

            from spike import PrimeHub

            hub = PrimeHub()

            gesture = hub.motion_sensor.wait_for_new_gesture()
            if gesture == 'shaken':
                # do one thing
            elif gesture == 'tapped':
                # do another thing

        """

    def wait_for_new_orientation(self) -> _Orientation:
        """Waits until the Hub’s orientation changes.

        The first time this method is called, it will immediately return the current value. After that, calling this method will block the program until the Hub’s orientation has changed since the previous time this method was called.

        Returns
        -------
        _Orientation
            The Hub’s new orientation.

        Example
        -------
        ::

            from spike import PrimeHub

            hub = PrimeHub()

            orientation = hub.motion_sensor.wait_for_new_orientation()
            if orientation == 'leftside':
                # do one thing
            elif orientation == 'rightside':
                # do another thing

        """

    def get_orientation(self) -> _Orientation:
        """Retrieves the Hub's current orientation.

        Returns
        -------
        _Orientation
            The Hub’s current orientation.


        Example
        -------
        ::

            from spike import PrimeHub

            hub = PrimeHub()

            if hub.motion_sensor.get_orientation() == 'front':
                # do something

        """

    def get_gesture(self) -> _Gesture:
        """Retrieves the most recently-detected gesture.

        Returns
        -------
        _Gesture
            The gesture.

        Example
        -------
        ::

            from spike import PrimeHub

            hub = PrimeHub()

            while True:
                if hub.motion_sensor.get_gesture() == 'falling':
                    print("Aaah!")

        """

    def get_roll_angle(self) -> int:
        """Retrieves the Hub’s roll angle.

        Roll is the rotation around the front-back (longitudinal) axis. Yaw is the rotation around the front-back (vertical) axis. Pitch is the rotation around the left-right (transverse) axis.

        Returns
        -------
        int
            The roll angle, specified in degrees (-180 to 180).

        Example
        -------
        ::

            from spike import PrimeHub

            hub = PrimeHub()

            if hub.motion_sensor.get_roll_angle() > 90:
                # do something

        """

    def get_pitch_angle(self) -> int:
        """Retrieves the Hub’s pitch angle.

        Pitch is the rotation around the left-right (transverse) axis. Roll is the rotation around the front-back (longitudinal) axis. Yaw is the rotation around the front-back (vertical) axis.

        Returns
        -------
        int
            The pitch angle, specified in degrees (-180 to 180).

        Example
        -------
        ::

            from spike import PrimeHub

            hub = PrimeHub()

            if hub.motion_sensor.get_pitch_angle() > 90:
                # do something

        """

    def get_yaw_angle(self) -> int:
        """Retrieves the Hub’s yaw angle.

        Yaw is the rotation around the front-back (vertical) axis. Pitch the is rotation around the left-right (transverse) axis. Roll the is rotation around the front-back (longitudinal) axis.

        Returns
        -------
        int
            The yaw angle, specified in degrees (-180 to 180).

        Example
        -------
        ::

            from spike import PrimeHub

            hub = PrimeHub()

            if hub.motion_sensor.get_yaw_angle() > 90:
                # do something

        """

    def reset_yaw_angle(self) -> None:
        """Sets the yaw angle to "0."

        Example
        -------
        ::

            from spike import PrimeHub

            hub = PrimeHub()

            hub.motion_sensor.reset_yaw_angle()
            angle = hub.motion_sensor.get_yaw_angle()
            print('Angle:', angle)

            # Angle is now 0

        """


_Image: TypeAlias = Literal["ANGRY", "ARROW_E", "ARROW_N", "ARROW_NE", "ARROW_NW", "ARROW_S", "ARROW_SE", "ARROW_SW", "ARROW_W", "ASLEEP", "BUTTERFLY", "CHESSBOARD", "CLOCK1", "CLOCK10", "CLOCK11", "CLOCK12", "CLOCK2", "CLOCK3", "CLOCK4", "CLOCK5", "CLOCK6", "CLOCK7", "CLOCK8", "CLOCK9", "CONFUSED", "COW", "DIAMOND", "DIAMOND_SMALL", "DUCK", "FABULOUS", "GHOST", "GIRAFFE", "GO_RIGHT",
                            "GO_LEFT", "GO_UP", "GO_DOWN", "HAPPY", "HEART", "HEART_SMALL", "HOUSE", "MEH", "MUSIC_CROTCHET", "MUSIC_QUAVER", "MUSIC_QUAVERS", "NO", "PACMAN", "PITCHFORK", "RABBIT", "ROLLERSKATE", "SAD", "SILLY", "SKULL", "SMILE", "SNAKE", "SQUARE", "SQUARE_SMALL", "STICKFIGURE", "SURPRISED", "SWORD", "TARGET", "TORTOISE", "TRIANGLE", "TRIANGLE_LEFT", "TSHIRT", "UMBRELLA", "XMAS", "YES"]


class LightMatrix:
    """Do not instantiate this class manually. Use hub = PrimeHub(); hub.light_matrix instead.
    """

    def __init__(self) -> None: ...

    def show_image(self, image: _Image, brightness: int = 100) -> None:
        """Shows an image on the Light Matrix.

        Parameters
        ----------
        image : _Image
            Name of the image.
        brightness : int, optional
            Brightness of the image (0 to 100), by default 100

        Raises
        ------
        TypeError
            image is not a string or brightness is not an integer.
        ValueError
            image is not one of the allowed values.

        Example
        -------
        ::

            from spike import PrimeHub
            from spike.control import wait_for_seconds

            hub = PrimeHub()

            hub.light_matrix.show_image('HAPPY')
            wait_for_seconds(5)
            hub.light_matrix.show_image('ASLEEP')
            wait_for_seconds(5)

        """

    def set_pixel(self, x: int, y: int, brightness=100) -> None:
        # XXX: Contradicting documentation. Is x, y 1-5 or 0-4?
        """Sets the brightness of one pixel (one of the 25 LEDs) on the Light Matrix.

        Parameters
        ----------
        x : int
            Pixel position, counting from the left (1 to 5).
        y : int
            Pixel position, counting from the top (1 to 5).
        brightness : int, optional
            Brightness of the pixel (0 to 100), by default 100

        Raises
        ------
        TypeError
            x, y or brightness is not an integer.
        ValueError
            x, y is not within the allowed range of 0-4.

        Example
        -------
        ::

            from spike import PrimeHub

            hub = PrimeHub()

            hub.light_matrix.set_pixel(1, 4)

        """

    def write(self, text: str) -> None:
        """Displays text on the Light Matrix, one letter at a time, scrolling from right to left.

        Your program will not continue until all of the letters have been shown.

        Parameters
        ----------
        text : str
            Text to write.

        Example
        -------
        ::

            from spike import PrimeHub

            hub = PrimeHub()

            hub.light_matrix.write('Hello!')


            # Show the number "1" on the Light Matrix

            hub.light_matrix.write('1')

        """

    def off(self) -> None:
        """Turns off all of the pixels on the Light Matrix.

        Example
        -------
        ::

            from spike import PrimeHub

            hub = PrimeHub()

            hub.light_matrix.off()

        """


_StatusLightColor: TypeAlias = Literal["azure", "black", "blue",
                                       "cyan", "green", "orange", "pink", "red", "violet", "yellow", "white"]


class StatusLight:
    """Do not instantiate this class manually. Use hub = PrimeHub(); hub.status_light instead.
    """

    def __init__(self) -> None: ...

    def on(self, color: _StatusLightColor = "white") -> None:
        """Sets the color of the light.

        Parameters
        ----------
        color : _StatusLightColor, optional
            Illuminates the Hub’s Brick Status Light in the specified color, by default 'white'

        Raises
        ------
        TypeError
            color is not a string.
        ValueError
            color is not one of the allowed values.

        Example
        -------
        ::

            from spike import PrimeHub

            hub = PrimeHub()

            hub.status_light.on('blue')

        """

    def off(self) -> None:
        """Turns off the light.

        Example
        -------
        ::

            from spike import PrimeHub

            hub = PrimeHub()

            hub.status_light.off()

        """


class Speaker:
    """Do not instantiate this class manually. Use hub = PrimeHub(); hub.speaker instead.
    """

    def __init__(self) -> None: ...

    def beep(self, note: float = 60, seconds: float = 0.2) -> None:
        """Plays a beep on the Hub.

        Your program will not continue until seconds have passed.

        Parameters
        ----------
        note : float, optional
            The MIDI note number (44 to 123, 60 is middle C), by default 60
        seconds : float, optional
            The duration of the beep, specified in seconds, by default 0.2

        Raises
        ------
        TypeError
            note is not an integer or seconds is not a number.
        ValueError
            note is not within the allowed range of 44-123.

        Example
        -------
        ::

            from spike import PrimeHub

            hub = PrimeHub()


            # beep beep beep!

            hub.speaker.beep(60, 0.5)
            hub.speaker.beep(67, 0.5)
            hub.speaker.beep(60, 0.5)

        """

    def start_beep(self, note: float = 60) -> None:
        """Starts playing a beep.

        The beep will play indefinitely until stop() or another beep method is called.

        Parameters
        ----------
        note : float, optional
            The MIDI note number (44 to 123, 60 is middle C), by default 60

        Raises
        ------
        TypeError
            note is not an integer.
        ValueError
            note is not within the allowed range of 44-123.

        Example
        -------
        ::

            from spike import PrimeHub

            hub = PrimeHub()

            hub.speaker.start_beep()

            # Do something

            hub.speaker.stop()

        """

    def stop(self) -> None:
        """Stops any sound that is playing.

        Example
        -------
        ::

            from spike import PrimeHub

            hub = PrimeHub()

            hub.speaker.start_beep()

            # Do something

            hub.speaker.stop()

        """

    def get_volume(self) -> int:
        """Retrieves the value of the speaker volume.

        This only retrieves the volume of the Hub, not the programming app.

        Returns
        -------
        int
            The current volume (0 to 100).

        Example
        -------
        ::

            from spike import PrimeHub

            hub = PrimeHub()


            # Increase the volume of the Hub speaker by 10%

            hub.speaker.set_volume(hub.speaker.get_volume() + 10)

        """

    def set_volume(self, volume: int) -> None:
        """Sets the speaker volume.

        If the assigned volume is out of range, the nearest volume (i.e., 0 or 100) will be used instead. This only sets the volume of the Hub, not the programming app.

        Parameters
        ----------
        volume : int
            The new volume percentage (0 to 100).

        Raises
        ------
        TypeError
            volume is not an integer.

        Example
        -------
        ::

            from spike import PrimeHub

            hub = PrimeHub()


            # Set the Hub speaker volume to 50%

            hub.speaker.set_volume(50)

        """
        raise TypeError


class ForceSensor:
    """To use the Force Sensor, you must first initialize it.

    Example
    -------
    ::

        from spike import ForceSensor


        # Initialize the Force Sensor
        force = ForceSensor('E')

    """

    def __init__(self) -> None: ...

    def is_pressed(self) -> bool:
        """Tests whether the button on the sensor is pressed.

        Returns
        -------
        bool
            True if the button is pressed.

        Raises
        ------
        RuntimeError
            The Force Sensor has been disconnected from the port.

        Example
        -------
        ::

            from spike import ForceSensor


            # Initialize the Force Sensor

            door_bell = ForceSensor('E')


            # Check whether the Force Sensor is pressed

            if door_bell.is_pressed():
                print('Hello!')

        """

    def get_force_newton(self) -> float:
        """Retrieves the measured force, in newtons.

        Returns
        -------
        float
            The measured force, specified in newtons (0 to 10)

        Raises
        ------
        RuntimeError
            The Force Sensor has been disconnected from the port.

        Example
        -------
        ::

            from spike import ForceSensor


            # Initialize the Force Sensor

            door_bell = ForceSensor('E')


            # Measure the force in newtons or as a percentage

            newtons = door_bell.get_force_newton()
            percentage = door_bell.get_force_percentage()


            # Print both results

            print('N:', newtons, '=', percentage, '%')


            # Check whether the Force Sensor is pressed

            if door_bell.is_pressed():
                print('Hello!')

        """

    def get_force_percentage(self) -> int:
        """Retrieves the measured force as a percentage of the maximum force.

        Returns
        -------
        int
            The measured force, given as a percentage (0 to 100).

        Raises
        ------
        RuntimeError
            The Force Sensor has been disconnected from the port.
        """

    def wait_until_pressed(self) -> None:
        """Waits until the Force Sensor is pressed.

        Raises
        ------
        RuntimeError
            The sensor has been disconnected from the port.

        Example
        -------
        ::

            from spike import ForceSensor

            force_sensor = ForceSensor('A')

            while True:
                force_sensor.wait_until_pressed()
                # do something, for example, start a motor
                force_sensor.wait_until_released()
                # do something, for example, stop a motor

        """

    def wait_until_released(self) -> None:
        """Waits until the Force Sensor is released.

        Raises
        ------
        RuntimeError
            The sensor has been disconnected from the Port.

        Example
        -------
        ::

            from spike import ForceSensor

            force_sensor = ForceSensor('A')

            while True:
                force_sensor.wait_until_pressed()
                # do something, for example, start a motor
                force_sensor.wait_until_released()
                # do something, for example, stop a motor

        """


_DistanceUnit: TypeAlias = Literal["cm", "in", "%"]


class DistanceSensor:
    """To use the Distance Sensor, you must first initialize it.

    Example
    -------
    ::

        from spike import DistanceSensor


        # Initialize the Distance Sensor
        distance = DistanceSensor('A')

    """

    def __init__(self) -> None: ...

    def light_up_all(self, brightness: int = 100) -> None:
        """Lights up all of the lights on the Distance Sensor at the specified brightness.

        Parameters
        ----------
        brightness : int, optional
            The specified brightness of all of the lights (0 is off, 100 is full brightness). By default 100

        Raises
        ------
        TypeError
            brightness is not a number.
        RuntimeError
            The sensor has been disconnected from the Port.

        Example
        -------
        ::

            from spike import DistanceSensor

            distance_sensor = DistanceSensor('A')


            # Turn on the lights

            distance_sensor.light_up_all()


            # Turn off the lights

            distance_sensor.light_up_all(0)

        """

    def light_up(self, right_top: int, left_top: int, right_bottom: int, left_bottom: int) -> None:
        """Sets the brightness of the individual lights on the Distance Sensor.

        Parameters
        ----------
        right_top : int
            The brightness of the light that’s above the right part of the Distance Sensor.
        left_top : int
            The brightness of the light that’s above the left part of the Distance Sensor.
        right_bottom : int
            The brightness of the light that’s below the right part of the Distance Sensor.
        left_bottom : int
            The brightness of the light that’s below the left part of the Distance Sensor.

        Raises
        ------
        TypeError
            right_top, left_top, right_bottom or left_bottom is not a number.
        RuntimeError
            The sensor has been disconnected from the Port.

        Example
        -------
        ::

            from spike import DistanceSensor

            distance_sensor = DistanceSensor('A')


            # Switch on the top lights of the Distance Sensor

            distance_sensor.light_up(100, 100, 0, 0)

        """

    def get_distance_cm(self, short_range: bool = False) -> Union[float, Literal["none"]]:
        """Retrieves the measured distance in centimeters.

        Parameters
        ----------
        short_range : bool, optional
            Whether or not to use short range mode. Short range mode increases accuracy, but it can only detect nearby objects. By default False

        Returns
        -------
        Union[float, Literal["none"]]
            The measured distance or "none" if the distance can't be measured.

        Raises
        ------
        TypeError
            short_range is not a boolean.
        RuntimeError
            The sensor has been disconnected from the Port.
        """

    def get_distance_inches(self, short_range: bool = False) -> Union[float, Literal["none"]]:
        """Retrieves the measured distance in inches.

        Parameters
        ----------
        short_range : bool, optional
            Whether or not to use short range mode. Short range mode increases accuracy, but it can only detect nearby objects. By default False

        Returns
        -------
        Union[float, Literal["none"]]
            The measured distance or "none" if the distance can't be measured.

        Raises
        ------
        TypeError
            short_range is not a boolean.
        RuntimeError
            The sensor has been disconnected from the Port.
        """
        raise TypeError
        raise RuntimeError

    def get_distance_percentage(self, short_range: bool = False) -> Union[int, Literal["none"]]:
        """Retrieves the measured distance as a percentage.

        Parameters
        ----------
        short_range : bool, optional
            Whether or not to use short range mode. Short range mode increases accuracy, but it can only detect nearby objects. By default False

        Returns
        -------
        Union[int, Literal["none"]]
            The measured distance or "none" if the distance can't be measured.

        Raises
        ------
        TypeError
            short_range is not a boolean.
        RuntimeError
            The sensor has been disconnected from the Port.
        """

    def wait_for_distance_farther_than(self, distance: float, unit: _DistanceUnit = "cm", short_range: bool = False) -> None:
        """Waits until the measured distance is greater than the specified distance.

        Parameters
        ----------
        distance : float
            The target distance to be detected from the sensor to an object.
        unit : _DistanceUnit, optional
            The unit in which the distance is measured. By default 'cm'
        short_range : bool, optional
            Whether or not to use short range mode. Short range mode increases accuracy, but it can only detect nearby objects. By default False

        Raises
        ------
        TypeError
            distance is not a number or unit is not a string or short_range is not a boolean.
        ValueError
            unit is not one of the allowed values.
        RuntimeError
            The sensor has been disconnected from the Port.

        Example
        -------
        ::

            from spike import DistanceSensor

            distance_sensor = DistanceSensor('A')

            while True:
                distance_sensor.wait_for_distance_farther_than(20, 'cm')
                # do something, for example, start a motor
                distance_sensor.wait_for_distance_closer_than(20, 'cm')
                # do something, for example, stop a motor

        """

    def wait_for_distance_closer_than(self, distance: float, unit: _DistanceUnit = "cm", short_range: bool = False) -> None:
        """Waits until the measured distance is less than the specified distance.

        Parameters
        ----------
        distance : float
            The target distance to be detected from the sensor to an object.
        unit : _DistanceUnit, optional
            The unit in which the distance is measured. By default 'cm'
        short_range : bool, optional
            Whether or not to use short range mode. Short range mode increases accuracy, but it can only detect nearby objects. By default False

        Raises
        ------
        TypeError
            distance is not a number or unit is not a string or short_range is not a boolean.
        ValueError
            unit is not one of the allowed values.
        RuntimeError
            The sensor has been disconnected from the Port.

        Example
        -------
        ::

            from spike import DistanceSensor

            distance_sensor = DistanceSensor('A')

            while True:
                distance_sensor.wait_for_distance_farther_than(20, 'cm')
                # do something, for example, start a motor
                distance_sensor.wait_for_distance_closer_than(20, 'cm')
                # do something, for example, stop a motor

        """


class PrimeHub:
    """The Hub is divided into six components, each with a number of functions linked to it.

    To use the Hub, you must first initialize it.

    Example
    -------
    ::

        from spike import PrimeHub


        # Initialize the Hub
        hub = PrimeHub()

    """

    def __init__(self) -> None:
        self.motion_sensor = MotionSensor()
        self.light_matrix = LightMatrix()
        self.status_light = StatusLight()
        self.speaker = Speaker()
