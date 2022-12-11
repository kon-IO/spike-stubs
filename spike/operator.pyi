from abc import abstractmethod
from typing import TypeVar, Protocol


# Thanks to https://stackoverflow.com/a/65224102 !
class _Comparable(Protocol):
    """Protocol for annotating comparable types"""

    # @abstractmethod
    # def __lt__(self: _Any_Comp, other: Any) -> bool: ...
    @abstractmethod
    def __lt__(self: _Any_Comp, other: _Any_Comp, /) -> bool: ...


_Any_Comp = TypeVar('_Any_Comp', bound=_Comparable)


def greater_than(a: _Any_Comp, b: _Any_Comp) -> bool:
    """Tests whether value "a" is greater than value "b."

    This is the same as "a > b."

    Parameters
    ----------
    a : Any
        Any object that can be compared to "b."
    b : Any
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


def greater_than_or_equal_to(a: _Any_Comp, b: _Any_Comp) -> bool:
    """Tests whether value "a" is greater than or equal to value "b."

    This is the same as "a >= b."

    Parameters
    ----------
    a : Any
        Any object that can be compared to "b."
    b : Any
        Any object that can be compared to "a."

    Returns
    -------
    bool
        True if a >= b, otherwise False.

    Example
    -------
    ::

        from spike import ColorSensor
        from spike.control import wait_until
        from spike.operator import greater_than_or_equal_to

        color_sensor = ColorSensor('A')

        wait_until(color_sensor.get_reflected_light, greater_than_or_equal_to, 50)

    """


def less_than(a: _Any_Comp, b: _Any_Comp) -> bool:
    """Tests whether value "a" is less than value "b."

    This is the same as "a < b."

    Parameters
    ----------
    a : Any
        Any object that can be compared to "b."
    b : Any
        Any object that can be compared to "a."

    Returns
    -------
    bool
        True if a < b, otherwise False.

    Example
    -------
    ::

        from spike import ColorSensor
        from spike.control import wait_until
        from spike.operator import less_than

        color_sensor = ColorSensor('A')

        wait_until(color_sensor.get_reflected_light, less_than, 50)

    """


def less_than_or_equal_to(a: _Any_Comp, b: _Any_Comp) -> bool:
    """Tests whether value "a" is less than or equal to value "b."

    This is the same as "a <= b."

    Parameters
    ----------
    a : Any
        Any object that can be compared to "b."
    b : Any
        Any object that can be compared to "a."

    Returns
    -------
    bool
        True if a <= b, otherwise False.

    Example
    -------
    ::

        from spike import ColorSensor
        from spike.control import wait_until
        from spike.operator import less_than_or_equal_to

        color_sensor = ColorSensor('A')

        wait_until(color_sensor.get_reflected_light, less_than_or_equal_to, 50)

    """


def equal_to(a: _Any_Comp, b: _Any_Comp) -> bool:
    """Tests whether value "a" is equal to value "b."

    This is the same as "a == b."

    Parameters
    ----------
    a : Any
        Any object that can be compared to "b."
    b : Any
        Any object that can be compared to "a."

    Returns
    -------
    bool
        True if a == b, otherwise False.

    Example
    -------
    ::

        from spike import ColorSensor
        from spike.control import wait_until
        from spike.operator import equal_to

        color_sensor = ColorSensor('A')

        wait_until(color_sensor.get_color, equal_to, 'red')

    """


def not_equal_to(a: _Any_Comp, b: _Any_Comp) -> bool:
    """Tests whether value "a" is not equal to value "b."

    This is the same as "a != b."

    Parameters
    ----------
    a : Any
        Any object that can be compared to "b."
    b : Any
        Any object that can be compared to "a."

    Returns
    -------
    bool
        True if a != b, otherwise False.

    Example
    -------
    ::

        from spike import ColorSensor
        from spike.control import wait_until
        from spike.operator import not_equal_to

        color_sensor = ColorSensor('A')

        wait_until(color_sensor.get_color, not_equal_to, None)

    """
