#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Friday Nov 27, 2020 13:48:49 AEDT
  @file        : covid

"""

import requests
import re, csv#, sys
import logging
from requests.exceptions import HTTPError

# Setting basic config for debugging prompts
logging.basicConfig(level=logging.DEBUG, format="%(msg)s")

# Uncomment this to disable debugging output
# logging.disable(logging.DEBUG)
# CLI = Covid-like illness

#TODO: class format for easy testing

# Date conversion helper functions 
def convertDateToUS(date: str) -> str:
    return re.sub(r"^([0-9]{2})([0-9]{2})([0-9]{4})$", r"\3\2\1", date)

def convertDateToAU(date: str) -> str:
    return re.sub(r"^([0-9]{4})([0-9]{2})([0-9]{2})$", r"\3\2\1", date)

# FEEL FREE TO CHANGE THESE FOR WHATEVER DATA YOU WANT
##########################

# Flag to indicate input/output format
# True by default since API date format is US
# and I happen to be Australian
aussieDateFormat = True

# Will do checks later on when data returns
# TODO: country/region checkers
country = "Australia" # Mandatory
region = "New South Wales"

# TODO: Might as well check valid fields too
indicator = "mask" # Mandatory
typ = "daily"      # Mandatory

# Dates must be in format YYYYMMDD - TODO: Add tests for invalid ranges, test one day range
dateStart = "01102020"
dateEnd   = "31102020"

# Say what fields you want out of this data
# TODO: Check field possibilities for each set of data
fields = {
    # Present in all query results
    'country',
    'iso_code',
    'gid_0',
    'sample_size',

    # Present if region given
    "region",
    "gid_1",

    # cli - covid indicator fields

    # ili - flu indicator fields

    'percent_mc_unw',
    'percent_mc'
}
fields = {
    "country": "country name of the data.",
    "gid_0": "the code for join country level data to the GADM country level data",
    "sample_size": "sample size for calculating the targeted value.",
    "survey_date": "date when survey was taken",
    "iso_code": "2 or 3 letter ISO code of country",


    # if region specified
    "region": "sub-country region name of the data. Generally, it is at state or province level or equivalent.",
    "gid_1": "the code for join region level data to the GADM region level data",

    # covid fields - daily
   "percent_cli": "weighted percentage of survey respondents that have reported CLI.",
   "cli_se": "standard error of percent_cli.",
   "percent_cli_unw": "unweighted percentage of survey respondents that have reported CLI.",
   "cli_se_unw": " standard error of percent_cli_unw.",

    # covid fields - smoothed
   "smoothed_cli": "seven-day rolling average of percent_cli values.",
   "smoothed_cli_se": " standard error of smoothed_cli.",



   "percent_ili": "weighted percentage of survey respondents that have reported ILI.",
   "percent_mc": "weighted percentage of survey respondents that have reported use mask cover.",
   "percent_dc": "weighted percentage of survey respondents that have reported had direct contact  (longer than one minute) with people not staying with them in last 24 hours.",
   "percent_hf": "weighted percentage of survey respondents that are worried about themselves and their household’s finances in the next month.",
   "percent_ili_unw": "unweighted percentage of survey respondents that have reported ILI.",
   "percent_mc_unw": "unweighted percentage of survey respondents that have reported use mask cover.",
   "percent_dc_unw": "unweighted percentage of survey respondents that have reported use have direct contact with people not staying with them.",
   "percent_hf_unw": "unweighted percentage of survey respondents that are worried about themselves and their household’s finances in the next month.",
   "smoothed_ili": "seven-day rolling average of percent_ili values.",
   "smoothed_mc": "seven-day rolling average of percent_mc values.",
   "smoothed_dc": "seven-day rolling average of percent_dc values.",
   "smoothed_hf": "seven-day rolling average of percent_hf values.",
   "smoothed_ili_se": "standard error of smoothed_ili.",
   "smoothed_mc_se": "standard error of smoothed_mc.",
   "smoothed_dc_se": "standard error of smoothed_dc.",
   "smoothed_hf_se": "standard error of smoothed_hf.",
   "ili_se": "standard error of percent_ili.",
   "mc_se": "standard error of percent_mc.",
   "dc_se": "standard error of percent_dc.",
   "hf_se": "standard error of percent_hf.",
   "ili_se_unw": " standard error of percent_ili_unw.",
   "mc_se_unw": " standard error of percent_mc_unw.",
   "dc_se_unw": " standard error of percent_dc_unw.",
   "hf_se_unw": " standard error of percent_hf_unw.",
}

###########################

# Convert dates to US format if using Aussie format
# I.e. convert from YYYYMMDD to DDMMYYYY
if aussieDateFormat:
    dateStart = convertDateToUS(dateStart)
    dateEnd   = convertDateToUS(dateEnd)

# Replaces space characters in country/region entries so API call works
region = re.sub(" ", "+", region)
country = re.sub(" ", "+", country)

daterange = f"{dateStart}-{dateEnd}"

try:
    url = f"https://covidmap.umd.edu/api/resources?indicator={indicator}&type={typ}&country={country}&region={region}&daterange={daterange}"
    
    # Print URL for debugging purposes
    logging.debug(f"URL: {url}")
    response = requests.get(url)

    # Check status of response
    response.raise_for_status()

except HTTPError as err:
    print(f"HTTP Error: {err}")

except Exception as err:
    print(f"Other Error Occurred: {err}")

# Convert from json data into a dict
jsonData = response.json() 

output = list()

# TODO: Error handling if there's no data at all in daterange
for i in jsonData['data']:
    # For each entry in data dict, grab the key/value pairs
    # for the specified fields that we want!
    entry = {k: i[k] for k in i.keys() and fields}

    # TODO: Some form of error if chosen output field isn't
    # in the set of data we get back from the API call

    # Swaps our dates back into DDMMYYYY format for us beloved Aussies
    if aussieDateFormat and "survey_date" in entry:
        entry["survey_date"] = convertDateToAU(entry["survey_date"])

    output.append(entry)

# Debugging contents of output to be written to csv file 
for i in output:
    logging.debug(i)

# convert to csv (excel) format
csv_filename = "data.csv"
try:
    with open(csv_filename, "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)

        # Writes field names to top of excel file
        writer.writeheader()
        for data in output:
            writer.writerow(data)


except IOError:
    print("I/O Error")

