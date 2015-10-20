# -*- coding: utf-8 -*-
import unittest2 as unittest  # to support Python 2.6
import nudged

samples = [
  {
    'id': 'Simple translation',
    'a': [[0, 0], [0, 1]],
    'b': [[1, 1], [1, 2]],
    's': 1, 'r': 0, 'tx': 1, 'ty': 1
  },
  {
    'id': 'Simple rotation',
    'a': [[ 1,  1], [-1, -1]],
    'b': [[-1, -1], [ 1,  1]],
    's': -1, 'r': 0, 'tx': 0, 'ty': 0
  },
  {
    'id': 'Simple scaling',
    'a': [[1, 1], [-1, -1]],
    'b': [[2, 2], [-2, -2]],
    's': 2, 'r': 0, 'tx': 0, 'ty': 0
  },
  {
    'id': 'Simple rotation & scaling',
    'a': [[ 1,  1], [-1, -1]],
    'b': [[-2, -2], [ 2,  2]],
    's': -2, 'r': 0, 'tx': 0, 'ty': 0
  },
  {
    'id': 'Simple translation & rotation',
    'a': [[0, 0], [2, 0], [ 1, 2]],
    'b': [[1, 1], [1, 3], [-1, 2]],
    's': 0, 'r': 1, 'tx': 1, 'ty': 1
  },
  {
    'id': 'Simple translation, rotation, & scaling',
    'a': [[1, -1], [ 3, -2]],
    'b': [[3,  4], [10,  8]],
    's': 2, 'r': 3, 'tx': -2, 'ty': 3
  },
  {
    'id': 'Approximating non-uniform scaling',
    'a': [[0, 0], [2, 0], [0, 2], [2, 2]],
    'b': [[0, 0], [2, 0], [0, 4], [2, 4]],
    's': 1.5, 'r': 0, 'tx': -0.5, 'ty': 0.5
  },
]

class TestEstimate(unittest.TestCase):

    def test_estimation(self):
        '''
        should estimate correctly
        '''
        for sple in samples:
            t = nudged.estimate(sple['a'], sple['b'])
            for k in ['s', 'r', 'tx', 'ty']:
                msg = sple['id'] + ': ' + k + '=' + str(getattr(t, k))
                self.assertEqual(getattr(t, k), sple[k], msg)

    def test_lists(self):
        '''
        should allow arrays of different length
        but ignore the points without a pair
        '''
        dom = [[1,-1], [ 3, -2], [1, 2]]
        ran = [[3, 4], [10,  8]]
        # 's': 2, 'r': 3, 'tx': -2, 'ty': 3
        t = nudged.estimate(dom, ran)
        self.assertEqual(t.transform([1,1]), [-3,8])

    def test_list_len_one(self):
        '''
        should allow lists of length one
        '''
        t = nudged.estimate([[1,1]], [[5,5]])
        self.assertEqual(t.transform([4,4]), [8,8])

    def test_list_len_zero(self):
        '''
        should allow lists of length zero
        '''
        t = nudged.estimate([], []);
        # Identity transform
        self.assertEqual(t.transform([0,0]), [0,0]);
        self.assertEqual(t.transform([7,7]), [7,7]);

    def test_identical_points(self):
        '''
        should allow a list of identical points
        '''
        t = nudged.estimate([[1,1], [1,1]], [[5,5], [7,7]])
        self.assertEqual(t.transform([1,1]), [6,6])

if __name__ == '__main__':
    unittest.main()
