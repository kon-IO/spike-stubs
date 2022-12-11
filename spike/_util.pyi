from abc import abstractmethod
from typing import Protocol, TypeVar


# Thanks to https://stackoverflow.com/a/65224102 !
class _Comparable(Protocol):
    """Protocol for annotating comparable types"""

    # @abstractmethod
    # def __lt__(self: _Any_Comp, other: Any) -> bool: ...
    @abstractmethod
    def __lt__(self: _Any_Comp, other: _Any_Comp, /) -> bool: ...


_Any_Comp = TypeVar('_Any_Comp', bound=_Comparable)
