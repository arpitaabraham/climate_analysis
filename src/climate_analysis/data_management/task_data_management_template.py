"""Tasks for managing the data."""

import pandas as pd
import pytask

from climate_analysis.config import BLD, SRC
from climate_analysis.data_management.data_cleaning import (
    clean_stats4schools_smoking,
)


def task_clean_stats4schools_smoking_data(
    script=SRC / "data_management" / "data_cleaning.py",
    data=SRC / "data" / "stats4schools_smoking_template.csv",
    produces=BLD / "data" / "stats4schools_smoking.pickle",
):
    """Clean the stats4schools smoking data set."""
    data = pd.read_csv(data)
    data = clean_stats4schools_smoking(data)
    data.to_pickle(produces)


@pytask.mark.r(
    script=SRC / "data_management" / "stats4schools_smoking_template.r",
    serializer="yaml",
)
def task_clean_stats4schools_smoking_data_r(
    data=SRC / "data" / "stats4schools_smoking_template.csv",
    produces=BLD / "data" / "stats4schools_smoking.rds",
):
    """Clean the stats4schools smoking data set (R version)."""
