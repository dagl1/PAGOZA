from typing import ClassVar

from PAGOZA.utils.registers import get_method


class MethodWrapper:
    GROUP: ClassVar[str | None] = None
    METHOD_NAME: ClassVar[str | None] = None

    def __init__(self, method, enum_cls=None):
        if enum_cls is not None and isinstance(method, enum_cls):
            method = method.value

        cls = get_method(self.GROUP, method)
        self._impl = cls()

    def __getattr__(self, item):
        return getattr(self._impl, item)

    def run(self, *args, **kwargs):
        return getattr(self._impl, self.METHOD_NAME)(*args, **kwargs)
