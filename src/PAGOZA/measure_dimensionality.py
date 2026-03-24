from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Protocol, TypeAlias, runtime_checkable

import numpy.typing as npt

from PAGOZA.utils.base_method import MethodWrapper
from PAGOZA.utils.registers import register_method

###### Base classes and protocols ######
ArrayLike: TypeAlias = npt.NDArray[Any]


class DimensionalityMethod(Enum):
    SLIDING_WINDOW = "sliding_window"


@runtime_checkable
class DimensionalityMeasurerProtocol(Protocol):
    def measure_dimensionality(self, X: ArrayLike) -> float: ...


class BaseDimensionalityMeasurer(ABC):
    def measure_dimensionality(self, X: ArrayLike) -> float:
        self._validate_input(X)
        return self._measure_dimensionality(X)

    def _validate_input(self, X: ArrayLike) -> None:
        if X.ndim == 0:
            raise ValueError("X must be at least one-dimensional")

    @abstractmethod
    def _measure_dimensionality(self, X: ArrayLike) -> float:
        raise NotImplementedError


###### Public API ######
class DimensionalityMeasurer(MethodWrapper[DimensionalityMeasurerProtocol]):
    GROUP = "dimensionality_measurer"
    METHOD_NAME = "measure_dimensionality"

    def __init__(self, method: str | DimensionalityMethod = "sliding_window"):
        super().__init__(method, DimensionalityMethod)

    def measure_dimensionality(self, X: ArrayLike) -> float:
        return self.run(X)


###### Implementations of dimensionality measurers ######
@register_method(name="sliding_window", group="dimensionality_measurer")
class SlidingWindowDimensionalityMeasurer(BaseDimensionalityMeasurer):
    def _measure_dimensionality(self, X: ArrayLike) -> float:
        # Placeholder implementation until the real algorithm lands.
        return float(X.shape[1]) if X.ndim > 1 else 1.0
