import numpy as np


np.allclose()

class Transform:

    def __init__(self, matrix=None):
        if matrix is None:
            matrix = np.eye(3, 3)
        self._matrix = matrix

    def __matmul__(self, other):
        '''
            The `@` operator combines two transforms into a sequence

            Parameters:
            ----------
            other: Transform

            Returns:
            ----------
            Transform
        '''
        assert isinstance(other, Transform)
        matrix = self._matrix @ other._matrix
        return Transform(matrix)

    def transform(self, x, y):
        '''
            Applies a transformation to the (`x`, `y`) point 

            Parameters:
            ----------
            x: int or float
            y: int or float

            Returns:
            ----------
            point: np.array[1, 3]
        '''
        vector = np.array([x, y, 1])
        return self._matrix @ vector

    def rotate(self, theta: float):
        '''
            Adds a rotation by `theta` degrees to the transform

            Rotates the coordinate space over its center
            
            Parameters:
            ----------
            theta: int or float
            
            Returns:
            ----------
            Transform
        '''
        theta = theta * np.pi / 180
        matrix = np.array([
            [np.cos(theta), -np.sin(theta), 0],
            [np.sin(theta), np.cos(theta), 0],
            [0, 0, 1]
        ])
        self._matrix = self._matrix @ matrix
        return self

    def translate(self, x, y):
        '''
            Adds a translation by (`x`, `y`) to the transform

            Moves the coordinate space horozontally and/or vertically

            Parameters:
            ----------
            x: int or float
            y: int or float
            
            Returns:
            ----------
            Transform
        '''
        matrix = np.array([
            [1, 0, x],
            [0, 1, y],
            [0, 0, 1]
        ])
        self._matrix = self._matrix @ matrix
        return self

    def scale(self, x, y):
        '''
            Adds a scale by (`x`, `y`) to the transform

            Stretches and/or compresses the coordinate space

            Parameters:
            ----------
            x: int or float
            y: int or float
            
            Returns:
            ----------
            Transform
        '''
        matrix = np.array([
            [x, 0, 0],
            [0, y, 0],
            [0, 0, 1]
        ])
        self._matrix = self._matrix @ matrix
        return self

    @staticmethod
    def Rotate(theta: float):
        '''
            Creates a one-step `rotation` transform

            Parameters:
            ----------
            theta: int or float
            
            Returns:
            ----------
            rotate: Transform
        '''
        return Transform().rotate(theta)

    @staticmethod
    def Translate(x: float, y: float):
        '''
            Creates a one-step `translation` transform

            Parameters:
            ----------
            x: int or float
            y: int or float
            
            Returns:
            ----------
            translate: Transform
        '''
        return Transform().translate(x, y)

    @staticmethod
    def Scale(x: float, y: float):
        '''
            Creates a one-step `scaling` transform

            Parameters:
            ----------
            x: int or float
            y: int or float
            
            Returns:
            ----------
            scale: Transform
        '''
        return Transform().scale(x, y)
