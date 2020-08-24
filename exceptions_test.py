#!/usr/bin/env python3

import unittest
from exceptions import validate_user
from exceptions import RemoveValue

class TestValidateUser(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate_user("validuser", 6), True)

    def test_too_short(self):
        self.assertEqual(validate_user("small", 6), False)

    def test_invalid_chars(self):
        self.assertEqual(validate_user("invalid_user", 5), False)

    def test_invalid_minlen(self):
        self.assertRaises(ValueError, validate_user, "user", -1)

    def test_assertion_error(self):
        self.assertRaises(AssertionError, validate_user, [3], 10)

    def test_list_value_error(self):
        self.assertRaises(ValueError, RemoveValue, [1,2,3,4,5], 6)

unittest.main()
