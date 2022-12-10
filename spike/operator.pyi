from typing import TypeVar

_Any = TypeVar('_Any')

def greater_than(a: _Any, b: _Any) -> bool:
    """Tests whether value "a" is greater than value "b."
    This is the same as "a > b."

    Parameters
    ----------
    a : _Any
        Any object that can be compared to "b."
    b : _Any
        Any object that can be compared to "a."

    Returns
    -------
    bool
        True if a > b, otherwise False.
    
    Example
    -------
    ::

        from spike import ColorSensor
        from spike.control import wait_until
        from spike.operator import greater_than

        color_sensor = ColorSensor('A')

        wait_until(color_sensor.get_reflected_light, greater_than, 50)
    """