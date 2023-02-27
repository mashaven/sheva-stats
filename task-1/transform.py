import numpy as np


class Transform:

    def __init__(self, matrix=None):
        if matrix is None:
            matrix = np.eye(3, 3)
        self._matrix = matrix

    def __matmul__(self, other):
        assert isinstance(other, Transform)
        matrix = self._matrix @ other._matrix
        return Transform(matrix)

    def transform(self, x, y):
        vector = np.array([x, y, 1])
        return self._matrix @ vector

    def rotate(self, theta: float):
        theta = theta * np.pi / 180
        matrix = np.array([
            [np.cos(theta), -np.sin(theta), 0],
            [np.sin(theta), np.cos(theta), 0],
            [0, 0, 1]
        ])
        self._matrix = self._matrix @ matrix
        return self

    def translate(self, x, y):
        matrix = np.array([
            [1, 0, x],
            [0, 1, y],
            [0, 0, 1]
        ])
        self._matrix = self._matrix @ matrix
        return self

    def scale(self, x, y):
        matrix = np.array([
            [x, 0, 0],
            [0, y, 0],
            [0, 0, 1]
        ])
        self._matrix = self._matrix @ matrix
        return self

    @staticmethod
    def Rotate(theta: float):
        return Transform().rotate(theta)

    @staticmethod
    def Translate(x: float, y: float):
        return Transform().translate(x, y)

    @staticmethod
    def Scale(x: float, y: float):
        return Transform().scale(x, y)
