__author__ = 'Nick Hirakawa'

import unittest

from src.invdx import *
from src.rank import *


class ParseTester(unittest.TestCase):

	def run_tests(self):
		pass


class RankTest(unittest.TestCase):

	def test_BM25(self):
		result = rank_BM25(40000, 15, 1, 0, 500000, 9, 10)
		result += rank_BM25(300, 25, 1, 0, 500000, 9, 10)
		self.assertAlmostEqual(result, 20.66, delta=0.05)

	def test_computeK(self):
		self.assertAlmostEqual(compute_K(9, 10), 1.11, delta=0.05)


class DataStructureTest(unittest.TestCase):

	def test_inverted_index(self):
		idx = InvertedIndex()
		idx.add('abc', 3)
		self.assertEqual(idx.get_document_frequency('abc', 3), 1)
		idx.add('abc', 3)
		self.assertEqual(idx.get_document_frequency('abc', 3), 2)

		self.assertEqual(idx.get_index_frequency('abc'), 1)
		idx.add('abc', 2)
		self.assertEqual(idx.get_index_frequency('abc'), 2)

	def test_inverted_index_contains(self):
		idx = InvertedIndex()
		idx.add('abc', 1)
		self.assertTrue('abc' in idx)
		self.assertFalse('cba' in idx)
		idx.add('cba', 2)
		self.assertTrue('cba' in idx)

	def test_inverted_index_get_item(self):
		idx = InvertedIndex()
		idx.add('abc', 1)
		self.assertEqual(idx['abc'], {1 : 1})
		idx.add('abc', 1)
		self.assertEqual(idx['abc'], {1 : 2})
		idx.add('abc', 2)
		self.assertEqual(idx['abc'], {1 : 2, 2 : 1})

	def test_document_length_table(self):
		dlt = DocumentLengthTable()
		dlt.add(1, 32)
		self.assertEqual(dlt.get_length(1), 32)
		dlt.add(2, 99)
		self.assertEqual(dlt.get_length(2), 99)

	def test_average_document_length(self):
		dlt = DocumentLengthTable()
		dlt.add(1, 1)
		dlt.add(2, 3)
		self.assertAlmostEqual(dlt.get_average_length(), 2, delta=0.05)
