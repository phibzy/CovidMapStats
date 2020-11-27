#!/usr/bin/python3

"""
    Test Cases:
        - Test all cases forward and backwards
        - Both dates valid
        - Potentially invalid conversion
        - Single digit day values

"""

import unittest
from covid import convertDate

class testConvertDate(unittest.TestCase):

    def testEasyConversions(self):
        self.assertEqual(convertDate("20201001"), "01102020")
        self.assertEqual(convertDate("01102020"),"20201001")


