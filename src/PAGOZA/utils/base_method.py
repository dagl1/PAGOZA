from enum import Enum
from typing import Any, ClassVar, Generic, TypeVar, cast

from PAGOZA.utils.registers import get_method

TProtocol = TypeVar("TProtocol")


class MethodWrapper(Generic[TProtocol]):
    GROUP: ClassVar[str]
    METHOD_NAME: ClassVar[str]

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if not hasattr(cls, "GROUP") or not isinstance(cls.GROUP, str):
            raise TypeError(
                f"{cls.__name__} must define a class variable 'GROUP' of type str."
            )
        if not hasattr(cls, "METHOD_NAME") or not isinstance(cls.METHOD_NAME, str):
            raise TypeError(
                f"{cls.__name__} must define a class variable 'METHOD_NAME' of type str."
            )

    def __init__(self, method: str | Enum, enum_cls: type[Enum] | None = None) -> None:
        if enum_cls is not None and isinstance(method, enum_cls):
            method = method.value

        if not isinstance(method, str):
            raise TypeError("method must be a string or enum value")

        cls = get_method(self.GROUP, method)
        self._impl: TProtocol = cast(TProtocol, cls())

    def __getattr__(self, item: str) -> Any:
        return getattr(self._impl, item)

    def run(self, *args: Any, **kwargs: Any) -> Any:
        return getattr(self._impl, self.METHOD_NAME)(*args, **kwargs)
