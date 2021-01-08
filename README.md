# CovidMapStats
Program which takes data from the University of Maryland's Covid Map API and spits it out into a nice csv file. I am in no way affiliated with them.

Within the CovidMapStats subdirectory, simply open the fields.py file and comment out any fields you don't want. Note that some fields are only present for particular queries.

Within the same directory, run covid.py and it will spit out a nice csv file for you with all your selected fields for your given parameters.

Includes support for both AU/US format date inputs - which can be toggled within covid.py.

# Citation
Junchuan Fan, Yao Li, Kathleen Stewart, Anil R. Kommareddy, Adrianne Bradford, Samantha Chiu, Frauke Kreuter, Neta Barkay, Alyssa Bilinski, Brian Kim, Roee Eliat, Tal Galili, Daniel Haimovich, Sarah LaRocca, Stanley Presser, Katherine Morris, Joshua A Salomon, Elizabeth A. Stuart, Ryan Tibshirani, Tali Alterman Barash, Curtiss Cobb, Andres Garcia, Andi Gros, Ahmed Isa, Alex Kaess, Faisal Karim, Ofir Eretz Kedosha, Shelly Matskel, Roee Melamed, Amey Patankar, Irit Rutenberg, Tal Salmona, David Vannette (2020). COVID-19 World Symptom Survey Data API. https://covidmap.umd.edu/api.html
