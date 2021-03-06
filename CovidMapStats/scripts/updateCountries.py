#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Sunday Jan 03, 2021 10:34:28 AEDT
  @file        : populateRegion

  Use this for making a call to API to populate dict
  with all possible countries and all possible regions.

  Will help greatly for checking valid input.

"""

import requests, sys
import shelve
from pprint import pprint
from requests.exceptions import HTTPError

try: 
    url = "https://covidmap.umd.edu/api/country"
    response = requests.get(url)

    # Check response status
    response.raise_for_status()

# Handle HTTP Exception
except HTTPError as err:
    print(f"HTTP Error: {err}")
    sys.exit()

# Handling any other weird exception
except Exception as err:
    print(f"Other Error Occurred: {err}")
    sys.exit()

# Convert JSON to dict object, with country name as keys
# mapping to a dict of region names
data = response.json()

# 'n' flag used to write to new shelve file
# even if it already exists. Using this instead of
# 'clear()' due to shelve files not reclaiming free space
with shelve.open('regions', flag='n', writeback=True) as regions:
    # Create blank dicts for each country,
    # which we can then use to add regions later
    for entry in data['data']:
        regions[entry['country']] = dict()
