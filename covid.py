#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Friday Nov 27, 2020 13:48:49 AEDT
  @file        : covid

"""

import requests
import json
import re
import csv


# FEEL FREE TO CHANGE THESE FOR WHATEVER DATA YOU WANT
##########################

country = "Australia"
indicator = "mask"
typ = "daily"
region = "New South Wales"

# Dates must be in format YYYYMMDD - TODO: Add tests for invalid ranges, test one day range
dateStart = "20201001"
dateEnd= "20201031"

###########################

# Replaces space characters in country/region entries so API call works
region = re.sub(" ", "+", region)
country = re.sub(" ", "+", country)

daterange = f"{dateStart}-{dateEnd}"

response = requests.get(f"https://covidmap.umd.edu/api/resources?indicator={indicator}&type={typ}&country={country}&region={region}&daterange={daterange}").text

# Convert from json data into a dict
jsonData = json.loads(response)

# TODO: Error check here lol

output = list()

# Say what fields you want out of this data
fields = {
    'percent_mc_unw',
    'percent_mc',
    'sample_size',
    'survey_date'
}

for i in jsonData['data']:
    # For each entry in data dict, grab the key/value pairs
    # for the specified fields that we want!
    entry = {k: i[k] for k in i.keys() and fields}

    # Swaps our dates into DDMMYYYY format for us beloved Aussies
    if "survey_date" in entry:
        entry["survey_date"] = re.sub(r"^([0-9]{4})([0-9]{2})([0-9]{2})$", r"\3\2\1", entry["survey_date"]) 

    output.append(entry)

for i in output:
    print(i)

# convert to csv (excel) format
csv_filename = "data.csv"
try:
    with open(csv_filename, "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)

        # Writes fields to top of excel file
        writer.writeheader()
        for data in output:
            writer.writerow(data)


except IOError:
    print("I/O Error")


"""
Damo wants:
    percent_mc_unw
    sample_size




"""
