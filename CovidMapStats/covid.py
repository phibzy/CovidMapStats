#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Friday Nov 27, 2020 13:48:49 AEDT
  @file        : covid

"""

import pprint, requests
import re, csv, sys
import logging, shelve
from requests.exceptions import HTTPError
from CovidMapStats.fields import defaultFields, regionFields, selectFields
from CovidMapStats.dateConverters import convertDateToUS, convertDateToAU

# Setting basic config for debugging prompts
logging.basicConfig(level=logging.DEBUG, format="%(msg)s")

# Uncomment this to disable debugging output
logging.disable(logging.DEBUG)
# CLI = Covid-like illness

# Flag to indicate input/output format
# True by default since API date format is US
# and I happen to be Australian
aussieDateFormat = True

# Load regions dict from shelve file
regions = shelve.open('regions')

country = "Australia" # Mandatory
region = "New South Wales"

# Check country and region are both valid
if country not in regions:
    print(f"Error: Country not in dataset. Did you spell it correctly (with capital at start)?")
    sys.exit()

if region and region not in regions[country]:
    print(f"Error: Region not in dataset.")
    sys.exit()

# Close shelve file once checks are done
regions.close()

indicator = "mask" # Mandatory
typ = "daily"      # Mandatory

# Dates must be in format YYYYMMDD
dateStart = "01102020"
dateEnd   = "31102020"

# Checks which fields you selected, then creates
# a dictionary with all of those fields present
# (once it passes input checks of course)
if indicator not in selectFields:
    print(f"Error: '{indicator}' is not a valid indicator")
    sys.exit()

if typ not in selectFields[indicator]:
    print(f"Error: typ value '{typ}' is not 'daily' or 'smoothed'")
    sys.exit()

fields = dict(selectFields[indicator][typ], **defaultFields)

# If region was given, add region fields as well
if region:
    fields.update(regionFields)

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
    sys.exit()

except Exception as err:
    print(f"Other Error Occurred: {err}")
    sys.exit()

# Convert from json data into a dict
jsonData = response.json() 

output = list()

# If there's no data for selected parameters,
# then there's nothing to write to the csv file
if not jsonData['data']:
    print(f"No data available for selected parameters")
    sys.exit()

for i in jsonData['data']:
    # For each entry in data dict, grab the key/value pairs
    # for the specified fields that we want!
    entry = {k: i[k] for k in i.keys() and fields}

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
