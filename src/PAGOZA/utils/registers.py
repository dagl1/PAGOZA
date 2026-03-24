from abc import ABC
from typing import Dict

METHOD_REGISTRY: Dict[str, Dict[str, ABC]] = {"default": {}}


def register_method(name: str, group: str = "default"):
    def decorator(cls):
        if group not in METHOD_REGISTRY:
            METHOD_REGISTRY[group] = {}
        METHOD_REGISTRY[group][name] = cls
        return cls

    return decorator


def get_method(group: str, method: str):
    if group not in METHOD_REGISTRY:
        available = ", ".join(f"'{g}'" for g in METHOD_REGISTRY)
        raise ValueError(f"Unknown group '{group}'. Available groups: {available}") from None
    if method not in METHOD_REGISTRY[group]:
        available = ", ".join(f"'{m}'" for m in METHOD_REGISTRY[group])
        raise ValueError(
            f"Unknown method '{method}' for group '{group}'. Available methods: {available}"
        ) from None
    return METHOD_REGISTRY[group][method]
