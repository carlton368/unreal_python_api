# import unittest
#
# class TestStringMethods(unittest.TestCase):
#     def test_upper(self):
#         self.assertEqual("foo".upper(), "FOO")
#         self.assertEqual("foo".upper(), "FOo")
#
#
# if __name__ == "__main__":
#     unittest.main()

import pytest

def test_upper():
    assert "foo".upper() == "FOOo"