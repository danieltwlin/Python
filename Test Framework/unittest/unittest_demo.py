#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
import unittest

class IntegerArithmeticTestCase(unittest.TestCase):
	def testAdd(self):  # test method names begin with 'test'
		self.assertEqual((1 + 2), 3)
		self.assertEqual(0 + 1, 1)
		
	def testMultiply(self):
		self.assertEqual((0 * 10), 0)
		self.assertEqual((5 * 8), 40)

	def testSubtract(self):
		self.assertEqual((10 - 5), 5)
		self.assertEqual((7 - 3), 1)	

if __name__ == '__main__':
	unittest.main()