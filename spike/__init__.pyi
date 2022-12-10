from typing import Literal, TypeAlias, Optional, Tuple

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
