from math import sqrt
import numpy as np

def function() -> str:
    return 'Hello World!'

def distance(x, y) -> float:
    return sqrt(x ** 2 + y ** 2)

def distances(array: np.array) -> np.ndarray:
    """Returns array of distances between 2D vectors"""
    result = np.zeros((len(array), len(array)))
    for i, a in enumerate(array):
        for j, b in enumerate(array):
            vector = b-a
            result[i][j] = distance(vector[0], vector[1])
    return result