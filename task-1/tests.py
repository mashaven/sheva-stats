import unittest
import numpy as np
from transform import Transform


class TestMatrixTransforms(unittest.TestCase):

    def setUp(self):
        self._vector = (1, 2)

    def test_SRT(self):
        transform = (
            Transform()
            .scale(2, 1.2)
            .rotate(33)
            .translate(1, 2)
        )
        RESULT_EXPECTED = (-1.00243001, 5.33275241, 1.)
        result = transform.transform(*self._vector)
        self.assertTrue(np.allclose(result, RESULT_EXPECTED))

    def test_TRS(self):
        transform = (
            Transform.Translate(1, 2) @
            Transform.Rotate(16) @
            Transform.Scale(1, 2)
        )
        RESULT_EXPECTED = (0.85871227, 6.12068414, 1.)
        result = transform.transform(*self._vector)
        self.assertTrue(np.allclose(result, RESULT_EXPECTED))


if __name__ == '__main__':
    unittest.main()
