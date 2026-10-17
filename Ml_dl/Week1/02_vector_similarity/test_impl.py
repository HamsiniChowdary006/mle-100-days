import pytest
import numpy as np
from impl import cosine_similarity, euclidean_distance

# Normal cosine similarity
def test_1():
    query = np.array([1.0, 0.0])
    vectors = np.array([[2.0, 0.0], [0.0, 2.0], [1.0, 1.0]])
    expected = np.array([1.0, 0.0, 1 / np.sqrt(2)])
    np.testing.assert_allclose(cosine_similarity(query, vectors), expected)

# Normal Euclidean distance
def test_2():
    query = np.array([1.0, 0.0])
    vectors = np.array([[2.0, 0.0], [0.0, 2.0], [1.0, 1.0]])
    expected = np.array([1.0, np.sqrt(5), 1.0])
    np.testing.assert_allclose(euclidean_distance(query, vectors), expected)

# Identical vectors
def test_3():
    query = np.array([1.0, 2.0])
    vectors = np.array([[1.0, 2.0]])
    assert cosine_similarity(query, vectors)[0] == pytest.approx(1.0)
    assert euclidean_distance(query, vectors)[0] == pytest.approx(0.0)

# Zero vector
def test_4():
    query = np.array([1.0, 0.0])
    vectors = np.array([[0.0, 0.0], [1.0, 0.0]])
    actual = cosine_similarity(query, vectors)
    assert actual[0] == 0.0
    assert np.all(np.isfinite(actual))

# Opposite vectors
def test_5():
    query = np.array([1.0, 0.0])
    vectors = np.array([[-1.0, 0.0]])
    assert cosine_similarity(query, vectors)[0] == pytest.approx(-1.0)
    assert euclidean_distance(query, vectors)[0] == pytest.approx(2.0)