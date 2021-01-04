#!/usr/bin/python3

"""
    Test Cases:
        - Test all cases forward and backwards
        - Both dates valid
        - Potentially invalid conversion
        - Single digit day values

"""

import unittest
import shelve
from pprint import pprint
from pathlib import Path
from CovidMapStats.dateConverters import convertDateToAU, convertDateToUS
from CovidMapStats.fields import defaultFields, regionFields, selectFields

class testHelpersAndDataStructures(unittest.TestCase):

    def testDateConversion(self):
        self.assertEqual(convertDateToAU("20201001"), "01102020")
        self.assertEqual(convertDateToUS("01102020"),"20201001")

    # Make sure to run tests from main project directory, otherwise
    # this won't work
    def testRegionChecker(self):
        # Work out some way to get absolute path working
        # for regions shelve file
        regions = shelve.open('regions')
        # pprint(dict(regions))

        # Test regions with spaces, weird punctuation and first/last entries
        self.assertTrue('Afghanistan' in regions)
        self.assertTrue('Australia' in regions)
        self.assertTrue('United States of America' in regions)
        self.assertTrue("Côte d'Ivoire" in regions)
        self.assertTrue('Bosnia and Herzegovina' in regions)
        self.assertTrue('Yemen' in regions)

        # Test regions with incorrect case and regions not in data (e.g. China)
        self.assertFalse('afghanistan' in regions)
        self.assertFalse('China' in regions)
        self.assertFalse('Middle Earth' in regions)
        self.assertFalse('australia' in regions)

        # Test regions within countries
        self.assertTrue('Kabul' in regions['Afghanistan'])
        self.assertTrue('New South Wales' in regions['Australia'])
        self.assertTrue('Ciudad Autónoma de Buenos Aires' in regions['Argentina'])
        self.assertTrue('Plzeňský' in regions['Czech Republic'])
        self.assertTrue("Sana'a" in regions['Yemen'])
        self.assertTrue("Thành phố Hồ Chí Minh" in regions['Vietnam'])

        # Test non-existent regions and case errors
        self.assertFalse("Murica" in regions['Vietnam'])
        self.assertFalse("thành phố Hồ Chí Minh" in regions['Vietnam'])
        self.assertFalse("new south wales" in regions['Australia'])

        regions.close()
