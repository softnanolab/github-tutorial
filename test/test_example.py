from softnanoexample.example import function, distance, distances
import numpy as np


def test_function():
    assert function() == 'Hello World!'
    return

def test_distance():
    #assert distance(3, 4) == 5
    distance(1, 1)
    return

def test_distances():
    example_array = np.array([
        [0, 0],
        [1, 0],
    ])
    expected_answer = np.array([
        [0.0, 1.0],
        [1.0, 0.0]
    ])
    assert (distances(example_array) == expected_answer).all() 
