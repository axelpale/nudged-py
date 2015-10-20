# -*- coding: utf-8 -*-
import nudged
import unittest
import pkg_resources  # part of setuptools

class TestVersion(unittest.TestCase):

    def test_equal(self):
        '''
        should have version that match package
        '''
        setuppy_version = pkg_resources.require('nudged')[0].version
        self.assertEqual(nudged.version, setuppy_version)

if __name__ == '__main__':
    unittest.main()
