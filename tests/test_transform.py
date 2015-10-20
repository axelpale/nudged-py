# -*- coding: utf-8 -*-
import unittest2 as unittest  # to support Python 2.6
import nudged
from math import pi

class TestTransform(unittest.TestCase):

    def setUp(self):
        dom = [[1, -1], [ 3, -2]]
        ran = [[3,  4], [10,  8]]
        self.t = nudged.estimate(dom, ran)

    def test_single_points(self):
        '''
        should allow single points
        '''
        self.assertEqual(self.t.transform([1,1]), [-3,8])
        self.assertEqual(self.t.transform([[1, 1]]), [[-3,8]])

    def test_matrix_list_repr(self):
        '''
        should be able to return matrix in array form
        '''
        matrix = [[2,-3,-2], [3, 2, 3], [0, 0, 1]]
        self.assertEqual(self.t.get_matrix(), matrix)

    def test_rotation_in_radians(self):
        '''
        should give rotation in radians
        '''
        t = nudged.estimate([[ 1, 1], [-1,-1]], [[-2,-2], [ 2, 2]]);
        # 's': -2, 'r': 0, 'tx': 0, 'ty': 0
        self.assertEqual(t.get_rotation(), pi)

    def test_scale(self):
        '''
        should give scale
        '''
        t = nudged.estimate([[ 1, 1], [-1,-1]], [[-2,-2], [ 2, 2]]);
        # 's': -2, 'r': 0, 'tx': 0, 'ty': 0
        self.assertEqual(t.get_scale(), 2.0)

    def test_translation(self):
        '''
        should give translation
        '''
        self.assertEqual(self.t.get_translation(), [-2, 3])


if __name__ == '__main__':
    unittest.main()
