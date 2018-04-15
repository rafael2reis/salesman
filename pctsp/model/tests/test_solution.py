import unittest

from pctsp.model import solution
from pctsp.model import pctsp
import numpy as np

class TestTrain(unittest.TestCase):
    def setUp(self):
        self.p = pctsp.Pctsp()
        self.p.prize = np.array([0, 4, 8])
        self.p.penal = np.array([1000, 7, 3])
        self.cost = np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]])

    def test_quality(self):
        s = solution.Solution(self.p)
        s.route = [0, 1, 2]
        print("Quality: ", s.quality)
        self.assertEqual(s.quality, 9)

if __name__ == '__main__':
    unittest.main()
