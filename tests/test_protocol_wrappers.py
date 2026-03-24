import numpy as np

from PAGOZA.measure_dimensionality import (
    DimensionalityMeasurer,
    DimensionalityMeasurerProtocol,
    DimensionalityMethod,
)
from PAGOZA.pair_generation import PairGenerationMethod, PairGenerator, PairGeneratorProtocol


def test_pair_generator_runtime_protocol_conformance() -> None:
    X = np.array([[1.0, 2.0], [3.0, 4.0]])
    generator = PairGenerator(method=PairGenerationMethod.GRADIENT)

    assert isinstance(generator, PairGeneratorProtocol)
    generated = generator.generate_pairs(X)
    assert generated.shape == X.shape


def test_dimensionality_measurer_runtime_protocol_conformance() -> None:
    X = np.array([[1.0, 2.0], [3.0, 4.0]])
    measurer = DimensionalityMeasurer(method=DimensionalityMethod.SLIDING_WINDOW)

    assert isinstance(measurer, DimensionalityMeasurerProtocol)
    dimensionality = measurer.measure_dimensionality(X)
    assert isinstance(dimensionality, float)
