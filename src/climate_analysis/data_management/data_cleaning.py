"""Function(s) for cleaning the data set(s)."""

# To log in print statements
import logging

import pandas as pd

logging.basicConfig(level=logging.INFO)

# List of CSV files to update
csv_files = [
    "src/climate_analysis/data/CO2_excl_LULUCF.csv",
    "src/climate_analysis/data/gdp_growthrate.csv",
    "src/climate_analysis/data/inflation_gdpdeflator.csv",
    "src/climate_analysis/data/population_total.csv",
    "src/climate_analysis/data/renewable_perc_of_total_EC.csv",
]

for file in csv_files:
    df = pd.read_csv(file)
    df.replace("Viet Nam", "Vietnam")
    df.to_csv(file, index=False)

logging.info("Spelling corrections applied!")
