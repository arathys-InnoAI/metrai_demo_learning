import pytest
import pandas as pd
import numpy as np
from generator import generate_temperatures, get_daily_averages
#using the same parameters as in main.py for the test
@pytest.fixture
def default_df():
    return generate_temperatures("2024-01-01",20.0,5,5.0,42)

# shape test
def test_output_row_count(default_df):
    assert len(default_df) == 120


def test_output_column_names(default_df):
    assert list(default_df.columns) == ["temperature", "temp_change"]

#date format test
def test_index_is_datetimeindex(default_df):
    assert isinstance(default_df.index, pd.DatetimeIndex)


@pytest.mark.parametrize("num_days", [1, 3, 7, 14, 30])
def test_row_count_scales_with_num_days(num_days):
    df = generate_temperatures("2024-01-01", 20.0, num_days, 5.0, 42)
    assert len(df) == num_days * 24


def test_daily_averages_returns_one_per_day(default_df):
    daily = get_daily_averages(default_df)
    assert len(daily) == 5


#boundarytest for mean temperature being close to start_temp

@pytest.mark.parametrize("start_temp, variation", [
    (0.0,   3.0),
    (20.0,  5.0),
    (35.0,  2.0),
    (-10.0, 4.0),
])
def test_mean_is_close_to_start_temp(start_temp, variation):
    df = generate_temperatures("2024-01-01", start_temp, 5, variation, 42)
    tolerance = 3 * (variation / np.sqrt(120))
    assert abs(df["temperature"].mean() - start_temp) < tolerance


def test_first_temp_change_is_nan(default_df):
    assert pd.isna(default_df["temp_change"].iloc[0])


def test_remaining_temp_changes_not_nan(default_df):
    assert default_df["temp_change"].iloc[1:].notna().all()


# validation tests for input parameters
@pytest.mark.parametrize("bad_date", [
    "01-01-2024",
    "2024/01/01",
    "not-a-date",
    "2024-13-01",
])
def test_invalid_date_raises_value_error(bad_date):
    with pytest.raises(ValueError):
        generate_temperatures(bad_date, 20.0, 5, 5.0, 42)


@pytest.mark.parametrize("bad_days", [0, -1, 366, 1000])
def test_invalid_num_days_raises_value_error(bad_days):
    with pytest.raises(ValueError):
        generate_temperatures("2024-01-01", 20.0, bad_days, 5.0, 42)


def test_string_temp_raises_type_error():
    with pytest.raises(TypeError):
        generate_temperatures("2024-01-01", "hot", 5, 5.0, 42)


def test_float_days_raises_type_error():
    with pytest.raises(TypeError):
        generate_temperatures("2024-01-01", 20.0, 5.5, 5.0, 42)


#validation tests for boundary values

@pytest.mark.parametrize("valid_days", [1, 365])
def test_boundary_day_counts_are_accepted(valid_days):
    df = generate_temperatures("2024-01-01", 20.0, valid_days, 5.0, 42 )
    assert len(df) == valid_days * 24