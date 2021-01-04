#!/usr/bin/env sh

######################################################################
# @author      : Chris Phibbs (chris@$HOSTNAME)
# @file        : update
# @created     : Monday Jan 04, 2021 19:14:56 AEDT
#
# @description : Run to update country/location data 
######################################################################

echo -n "Updating country list..."
./scripts/updateCountries.py
echo "Done!"

echo -n "Updating region list..."
./scripts/updateRegions.py
echo "Done!"
