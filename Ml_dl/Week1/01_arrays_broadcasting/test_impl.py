import pytest
from impl import broadcast_shape

# Normal broadcasting
def test_1():
    assert broadcast_shape((3, 1), (1, 4)) == (3, 4)

# Different number of dimensions
def test_2():
    assert broadcast_shape((5, 3), (3,)) == (5, 3)

# Scalar shape
def test_3():
    assert broadcast_shape((), (2, 3)) == (2, 3)

# Zero -sized dimension
def test_4():
    assert broadcast_shape((0, 3), (1, 3)) == (0, 3)

# Incompatible shapes
def test_5():
    with pytest.raises(ValueError):
        broadcast_shape((2, 3), (4, 3))