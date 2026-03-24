from abc import ABC, abstractmethod
from enum import Enum
from typing import Protocol

from PAGOZA.utils.base_method import MethodWrapper
from PAGOZA.utils.registers import register_method


###### Base classes and protocols ######
class DimensionalityMethod(Enum):
    SLIDING_WINDOW = "sliding_window"


class DimensionalityMeasurerProtocol(Protocol):
    def measure_dimensionality(self, X): ...


class BaseDimensionalityMeasurer(ABC):
    def measure_dimensionality(self, X):
        self._validate_input(X)
        return self._measure_dimensionality(X)

    def _validate_input(self, X):
        return X == X  # Placeholder for actual validation logic
        # (e.g., check if X is a numpy array, check dimensions, etc.)

    @abstractmethod
    def _measure_dimensionality(self, X):
        pass


###### Public API ######
class DimensionalityMeasurer(MethodWrapper):
    GROUP = "dimensionality_measurer"
    METHOD_NAME = "measure_dimensionality"

    def __init__(self, method: str | DimensionalityMethod = "sliding_window"):
        super().__init__(method, DimensionalityMethod)

    def measure_dimensionality(self, X):
        return self.run(X)


###### Implementations of dimensionality measurers ######
@register_method(name="sliding_window", group="dimensionality_measurer")
class SlidingWindowDimensionalityMeasurer(BaseDimensionalityMeasurer):
    def _measure_dimensionality(self, X):
        # Implement the logic to measure dimensionality using a sliding window approach
        pass
