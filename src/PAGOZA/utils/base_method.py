from typing import ClassVar

from PAGOZA.utils.registers import get_method


class MethodWrapper:
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

    def __init__(self, method, enum_cls=None):
        if enum_cls is not None and isinstance(method, enum_cls):
            method = method.value

        cls = get_method(self.GROUP, method)
        self._impl = cls()

    def __getattr__(self, item):
        return getattr(self._impl, item)

    def run(self, *args, **kwargs):
        return getattr(self._impl, self.METHOD_NAME)(*args, **kwargs)
