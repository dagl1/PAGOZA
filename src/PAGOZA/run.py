"""
This script during development includes all the wrapper, util, and base/protocols,
that the actual functionality is built from. Later on we can separate it out into proper
submodules.
"""

import numpy as np

from PAGOZA.measure_dimensionality import (
    DimensionalityMeasurer,
    DimensionalityMeasurerProtocol,
    DimensionalityMethod,
)
from PAGOZA.pair_generation import PairGenerationMethod, PairGenerator, PairGeneratorProtocol


###### Base classes and protocols ######
class PAGOZA:
    def __init__(
        self,
        dimensionality_method: str | DimensionalityMethod = "sliding_window",
        pair_generation_method: str | PairGenerationMethod = "gradient",
    ):
        self.dimensionality_measurer: DimensionalityMeasurerProtocol = DimensionalityMeasurer(
            method=dimensionality_method
        )
        self.pair_generator: PairGeneratorProtocol = PairGenerator(
            method=pair_generation_method
        )

    def run(self, X: np.array):
        """
        Run the PAGOZA method on the input data X.

        Args:
            X (np.array): Input data for which to measure dimensionality and generate pairs.
        """
        dimensionality = self.dimensionality_measurer.measure_dimensionality(X)
        pairs = self.pair_generator.generate_pairs(X)
        # Further processing with dimensionality and pairs
        return dimensionality, pairs
