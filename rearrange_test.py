#!/usr/bin/env python3

from rearrange import rearrange_name
import unittest
import doctest

class TestRearrange(unittest.TestCase):

    def test_doc(self):
        '''This is an example of the doctest type of unit test'''
        assert rearrange_name("Lovelace, Linda") == "Linda Lovelace"

    def test_basic(self):
        testcase = "Lovelace, Linda"
        expected = "Linda Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)

    def test_onename(self):
        testcase = "Prince"
        expected = "Prince"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_nocomma(self):
        testcase = "Lovelace Linda"
        expected = "Lovelace Linda"
        self.assertEqual(rearrange_name(testcase), expected, msg="No comma test failed")

    def test_specialchars(self):
        testcase = "Love$Lace, Linda"
        expected = "Love$Lace, Linda"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_threenames(self):
        testcase = "Lovelace, Linda, Smith"
        expected = "Lovelace, Linda, Smith"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_hyphenated_name(self):
        testcase = "Lovelace-Hockingsmith, Linda"
        expected = "Linda Lovelace-Hockingsmith"
        self.assertEqual(rearrange_name(testcase), expected)

unittest.main()
