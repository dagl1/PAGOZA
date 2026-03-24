from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Protocol, TypeAlias, runtime_checkable

import numpy.typing as npt

from PAGOZA.utils.base_method import MethodWrapper
from PAGOZA.utils.registers import register_method

###### Base classes and protocols ######
ArrayLike: TypeAlias = npt.NDArray[Any]


class PairGenerationMethod(Enum):
    GRADIENT = "gradient"
    LOCAL_NOISE = "local_noise"


@runtime_checkable
class PairGeneratorProtocol(Protocol):
    def generate_pairs(self, X: ArrayLike) -> ArrayLike: ...


class BasePairGenerator(ABC):
    def generate_pairs(self, X: ArrayLike) -> ArrayLike:
        """
        Generate pairs from the input data X.

        Args:
            X (ArrayLike): Input data for which to generate pairs.

        Returns:
            Generated pairs based on the implemented method.
        """
        self._validate_input(X)
        return self._generate_pairs(X)

    def _validate_input(self, X: ArrayLike) -> None:
        if X.ndim == 0:
            raise ValueError("X must be at least one-dimensional")

    @abstractmethod
    def _generate_pairs(self, X: ArrayLike) -> ArrayLike:
        raise NotImplementedError


###### Public API ######
class PairGenerator(MethodWrapper[PairGeneratorProtocol]):
    GROUP = "pair_generator"
    METHOD_NAME = "generate_pairs"

    def __init__(self, method: str | PairGenerationMethod = "gradient"):
        super().__init__(method, PairGenerationMethod)

    def generate_pairs(self, X: ArrayLike) -> ArrayLike:
        return self.run(X)


###### Implementations of pair generators ######
@register_method(name="gradient", group="pair_generator")
class GradientPairGenerator(BasePairGenerator):
    def _generate_pairs(self, X: ArrayLike) -> ArrayLike:
        x = self._compute_gradients(X)
        return x
        # Implement the logic to generate pairs based on gradients

    def _compute_gradients(self, X: ArrayLike) -> ArrayLike:
        # Implement the logic to compute gradients for the input data
        return X


@register_method(name="local_noise", group="pair_generator")
class LocalNoisePairGenerator(BasePairGenerator):
    def _generate_pairs(self, X: ArrayLike) -> ArrayLike:
        # Implement the logic to generate pairs based on local noise
        return X
