from typing import Callable, TypeVar, Protocol, Any
from abc import abstractmethod


def wait_for_seconds(seconds: float) -> None:
    """Waits for a specified number of seconds before continuing the program.

    Parameters
    ----------
    seconds : float
        The time to wait, specified in seconds.

    Returns
    -------
    None

    Example
    -------
    ::

        from spike.control import wait_for_seconds


        # wait for 3 seconds (pause the program flow)

        wait_for_seconds(3)

    """


# Thanks to https://stackoverflow.com/a/65224102 !
class _Comparable(Protocol):
    """Protocol for annotating comparable types"""

    # @abstractmethod
    # def __lt__(self: _Any_Comp, other: Any) -> bool: ...
    @abstractmethod
    def __lt__(self: _Any_Comp, other: _Any_Comp, /) -> bool: ...


_Any = TypeVar('_Any')
_Any_Comp = TypeVar('_Any_Comp', bound=_Comparable)


def wait_until(get_value_function: Callable[[], _Any_Comp], operator_funtion: Callable[[_Any_Comp, _Any_Comp], bool], target_value: _Any_Comp) -> None:
    """Waits until the condition is true before continuing with the program.

    Parameters
    ----------
    get_value_function : Callable[[], Any]
        A function that returns the current value to be compared to the target value.
    operator_funtion : Callable[[Any, Any], bool]
        A function that compares two arguments. The first argument will be the result of get_value_function(), and the second argument will be target_value. The function will compare both values and return the result.
    target_value : Any
        Any object that can be compared by operator_function.

    Returns
    -------
    None


    Raises
    ------
    TypeError
        get_value_function or operator_function is not callable or operator_function does not compare two arguments.

    Example
    -------
    ::

        from spike import ColorSensor
        from spike.control import wait_until
        from spike.operator import equal_to

        color_sensor = ColorSensor('A')


        # Wait for the Color Sensor to detect "red"

        wait_until(color_sensor.get_color, equal_to, 'red')


    Example
    -------
    ::

        from spike import ColorSensor, Motor
        from spike.control import wait_until

        color_sensor = ColorSensor('A')
        motor = Motor('B')

        def red_or_position():
            return color_sensor.get_color() == 'red' or motor.get_position() > 90

        wait_until(red_or_position)
    """


class Timer:
    """To use the Timer, you must first initialize it.

    Example
    -------
    ::

        from spike.control import Timer


        # InitialiZe the Timer
        timer = Timer()

    """

    def __init__(self) -> None: ...

    def reset(self) -> None:
        """Sets the Timer to "0."

        Example
        -------
        ::

            timer = Timer()
            # After some time...
            timer.reset()
        """

    def now(self) -> int:
        """Retrieves the "right now" time of the Timer.

        Returns
        -------
        int
            The current time, specified in seconds (always positive).

        Example
        -------
        ::

            from spike.control import Timer

            timer = Timer()

            while True:
                # If it has been more than 5 seconds since the Timer started
                if timer.now() > 5:
                    # then break out of the while loop
                    break
        """
