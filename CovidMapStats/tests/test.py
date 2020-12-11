#!/usr/bin/python3

"""
    Test Cases:
        - Test all cases forward and backwards
        - Both dates valid
        - Potentially invalid conversion
        - Single digit day values

"""

import unittest
from CovidMapStats.covid import convertDateToAU, convertDateToUS
from CovidMapStats.fields import defaultFields, regionFields, selectFields

class testConvertDate(unittest.TestCase):

    def testEasyConversions(self):
        self.assertEqual(convertDateToAU("20201001"), "01102020")
        self.assertEqual(convertDateToUS("01102020"),"20201001")


