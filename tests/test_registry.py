import pytest

from PAGOZA.utils.registers import METHOD_REGISTRY, get_method, register_method


def test_register_method_and_get_method_roundtrip() -> None:
    group = "_test_group_registry"
    method = "_test_method"

    @register_method(name=method, group=group)
    class _TestImplementation:
        pass

    try:
        resolved = get_method(group, method)
        assert resolved is _TestImplementation
    finally:
        METHOD_REGISTRY.pop(group, None)


def test_get_method_unknown_group_lists_available_groups() -> None:
    with pytest.raises(
        ValueError, match="Unknown group 'definitely_missing_group'"
    ) as exc_info:
        get_method("definitely_missing_group", "anything")

    message = str(exc_info.value)
    assert "Available groups:" in message


def test_get_method_unknown_method_lists_available_methods() -> None:
    group = "_test_group_unknown_method"
    method = "known_method"

    @register_method(name=method, group=group)
    class _KnownImplementation:
        pass

    try:
        with pytest.raises(
            ValueError, match=f"Unknown method 'missing' for group '{group}'"
        ) as exc_info:
            get_method(group, "missing")

        message = str(exc_info.value)
        assert "Available methods:" in message
        assert "known_method" in message
    finally:
        METHOD_REGISTRY.pop(group, None)
