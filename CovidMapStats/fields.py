#!/usr/bin/python3

defaultFields = {
    # present in all results
    "sample_size": "sample size for calculating the targeted value.",
    "survey_date": "date when survey was taken",
    "country": "country name of the data.",
    "gid_0": "the code for join country level data to the GADM country level data",
    "iso_code": "2 or 3 letter ISO code of country",
}

regionFields = {
    # if region specified
    "region": "sub-country region name of the data. Generally, it is at state or province level or equivalent.",
    "gid_1": "the code for join region level data to the GADM region level data",
}

selectFields = {
    "covid": {

        "daily": {
            # covid fields (cli - covid-like illness) - daily
           "percent_cli": "weighted percentage of survey respondents that have reported CLI.",
           "cli_se": "standard error of percent_cli.",
           "percent_cli_unw": "unweighted percentage of survey respondents that have reported CLI.",
           "cli_se_unw": " standard error of percent_cli_unw.",
        },

        "smoothed": {
            # covid fields (cli - covid-like illness) - smoothed
           "smoothed_cli": "seven-day rolling average of percent_cli values.",
           "smoothed_cli_se": " standard error of smoothed_cli.",
        }
    },

    "flu":  {
        "daily": {
            # flu fields (ili - influence-like illness) - daily
           "percent_ili": "weighted percentage of survey respondents that have reported ILI.",
           "percent_ili_unw": "unweighted percentage of survey respondents that have reported ILI.",
           "ili_se": "standard error of percent_ili.",
           "ili_se_unw": " standard error of percent_ili_unw.",
        },

        "smoothed": {
            # flu fields (ili - influence-like illness) - smoothed
           "smoothed_ili": "seven-day rolling average of percent_ili values.",
           "smoothed_ili_se": "standard error of smoothed_ili.",
        }
    },

    "mask":  {
        "daily": {
            # mask fields (mc) - daily
           "percent_mc": "weighted percentage of survey respondents that have reported use mask cover.",
           "percent_mc_unw": "unweighted percentage of survey respondents that have reported use mask cover.",
           "mc_se": "standard error of percent_mc.",
           "mc_se_unw": " standard error of percent_mc_unw.",
        },

        "smoothed": {
            # mask fields (mc) - smoothed 
           "smoothed_mc": "seven-day rolling average of percent_mc values.",
           "smoothed_mc_se": "standard error of smoothed_mc.",
       }
    },

    "contact":  {
        "daily": {
           # contact fields (dc - direct contact) - daily
           "percent_dc": "weighted percentage of survey respondents that have reported had direct contact  (longer than one minute) with people not staying with them in last 24 hours.",
           "percent_dc_unw": "unweighted percentage of survey respondents that have reported use have direct contact with people not staying with them.",
           "dc_se": "standard error of percent_dc.",
           "dc_se_unw": " standard error of percent_dc_unw.",
        },

        "smoothed": {
           # contact fields (dc - direct contact) - smoothed
           "smoothed_dc": "seven-day rolling average of percent_dc values.",
           "smoothed_dc_se": "standard error of smoothed_dc.",
       }
    },
      
    "finance":  {
        "daily": {
            # finance fields (hf - household finance) - daily
           "percent_hf": "weighted percentage of survey respondents that are worried about themselves and their household’s finances in the next month.",
           "percent_hf_unw": "unweighted percentage of survey respondents that are worried about themselves and their household’s finances in the next month.",
           "hf_se": "standard error of percent_hf.",
           "hf_se_unw": " standard error of percent_hf_unw.",
        },

        "smoothed": {
            # finance fields (hf - household finance) - smoothed
           "smoothed_hf": "seven-day rolling average of percent_hf values.",
           "smoothed_hf_se": "standard error of smoothed_hf.",
       }
    }
}
