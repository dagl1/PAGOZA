from abc import ABC, abstractmethod
from enum import Enum
from typing import Protocol

import numpy as np

from PAGOZA.utils.base_method import MethodWrapper
from PAGOZA.utils.registers import register_method


###### Base classes and protocols ######
class PairGenerationMethod(Enum):
    GRADIENT = "gradient"
    LOCAL_NOISE = "local_noise"


class PairGeneratorProtocol(Protocol):
    def generate_pairs(self, X): ...


class BasePairGenerator(ABC):
    def generate_pairs(self, X: np.array):
        """
        Generate pairs from the input data X.
        Args:
            X (np.array): Input data for which to generate pairs.
        Returns:
            Generated pairs based on the implemented method.
        """
        self._validate_input(X)
        return self._generate_pairs(X)

    def _validate_input(self, X):
        return X == X  # Placeholder for actual validation logic
        # (e.g., check if X is a numpy array, check dimensions, etc.)

    @abstractmethod
    def _generate_pairs(self, X):
        pass


###### Public API ######
class PairGenerator(MethodWrapper):
    GROUP = "pair_generator"
    METHOD_NAME = "generate_pairs"

    def __init__(self, method: str | PairGenerationMethod = "gradient"):
        super().__init__(method, PairGenerationMethod)

    def generate_pairs(self, X):
        return self.run(X)


###### Implementations of pair generators ######
@register_method(name="gradient", group="pair_generator")
class GradientPairGenerator(BasePairGenerator):
    def _generate_pairs(self, X):
        x = self._compute_gradients(X)
        return x
        # Implement the logic to generate pairs based on gradients

    def _compute_gradients(self, X):
        # Implement the logic to compute gradients for the input data
        pass


@register_method(name="local_noise", group="pair_generator")
class LocalNoisePairGenerator(BasePairGenerator):
    def _generate_pairs(self, X):
        # Implement the logic to generate pairs based on local noise
        pass
