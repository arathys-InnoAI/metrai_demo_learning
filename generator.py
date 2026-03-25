import numpy as np
import pandas as pd
from datetime import datetime


def validate_inputs(start_date, start_temp, num_days, variation, seed):
    try:
        #date object from string
        datetime.strptime(start_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError(
            f"start_date '{start_date}' is not valid, Use YYYY-MM-DD"
        )

    if not isinstance(start_temp, (int, float)):
        raise TypeError(
            f"start_temp must be a integer/float, got {type(start_temp)}"
        )


    if not isinstance(num_days, int):
        raise TypeError(
            f"num_days must be an integer, got {type(num_days)}"
        )

    if not isinstance(variation, (int, float)):
        raise TypeError(
            f"variation must be a integer/float, got {type(variation)}"
        )

    if not isinstance(seed, int):
        raise TypeError(
            f"seed must be an integer, got {type(seed)}"
        )
    if num_days < 1 or num_days > 365:
        raise ValueError(
            f"num_days {num_days} must be between 1 and 365."
        )

def generate_temperatures(start_date,start_temp,num_days,variation,seed):
    
    validate_inputs(start_date, start_temp, num_days, variation, seed)

    total_hours = num_days * 24

    np.random.seed(seed)
    temperatures = np.random.normal(loc=start_temp,scale=variation,size=total_hours)

    timestamps = pd.date_range(start=start_date,periods=total_hours,freq="h")

    df = pd.DataFrame({
        "timestamp": timestamps,
        "temperature": temperatures
    })
    df.set_index("timestamp", inplace=True)
    df["temp_change"] = df["temperature"].diff()

    return df


def get_daily_averages(df):
    return df["temperature"].groupby(df.index.date).mean().round(2)