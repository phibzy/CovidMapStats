#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Monday Jan 04, 2021 18:03:54 AEDT
  @file        : dateConverters

  Functions for converting date types

"""

import re

# Date conversion helper functions 
def convertDateToUS(date: str) -> str:
    return re.sub(r"^([0-9]{2})([0-9]{2})([0-9]{4})$", r"\3\2\1", date)

def convertDateToAU(date: str) -> str:
    return re.sub(r"^([0-9]{4})([0-9]{2})([0-9]{2})$", r"\3\2\1", date)
