from collections.abc import Callable
from typing import Any, TypeVar

T = TypeVar("T")

METHOD_REGISTRY: dict[str, dict[str, type[Any]]] = {"default": {}}


def register_method(name: str, group: str = "default") -> Callable[[type[T]], type[T]]:
    def decorator(cls: type[T]) -> type[T]:
        if group not in METHOD_REGISTRY:
            METHOD_REGISTRY[group] = {}
        METHOD_REGISTRY[group][name] = cls
        return cls

    return decorator


def get_method(group: str, method: str) -> type[Any]:
    if group not in METHOD_REGISTRY:
        available = ", ".join(f"'{g}'" for g in METHOD_REGISTRY)
        raise ValueError(f"Unknown group '{group}'. Available groups: {available}") from None
    if method not in METHOD_REGISTRY[group]:
        available = ", ".join(f"'{m}'" for m in METHOD_REGISTRY[group])
        raise ValueError(
            f"Unknown method '{method}' for group '{group}'. Available methods: {available}"
        ) from None
    return METHOD_REGISTRY[group][method]
