import pandas as pd
from scipy.stats import linregress


def fit_trendline(year_timestamps, data):
    """Fits a trendline to the given data using linear regression.

    Args:
        year_timestamps (list): A list of year timestamps.
        data (list): A list of data points.

    Returns:
        tuple: A tuple containing the slope and R-squared value of the trendline.
    """
    result = linregress(year_timestamps, data)
    slope = round(result.slope, 3)
    r_squared = round(result.rvalue**2, 3)
    return slope, r_squared


def process_sdg_data(input_excel_file, columns_to_drop):
    """Process SDG data from an input Excel file downloaded from the SDG website.

    Args:
        input_excel_file (str): The path to the input Excel file.
        columns_to_drop (list): A list of column names to drop from the DataFrame.

    Returns:
        pandas DataFrame: The processed DataFrame with dropped columns and transposed index.
    """
    df = pd.read_excel(input_excel_file)
    df = df.drop(columns_to_drop, axis=1)
    df = df.set_index("GeoAreaName").transpose()
    return df


def country_trendline(country_name):
    """Calculate the slope and R-squared value of the trendline for a given country.

    Args:
        country_name (str): The name of the country as represented in the SDG database.

    Returns:
        tuple: A tuple containing the slope and R-squared value of the trendline.
    """
    df = process_sdg_data(
        "../data/SG_GEN_PARL.xlsx",
        [
            "Goal",
            "Target",
            "Indicator",
            "SeriesCode",
            "SeriesDescription",
            "GeoAreaCode",
            "Reporting Type",
            "Sex",
            "Units",
        ],
    )
    timestamps = [int(i) for i in df.index.tolist()]
    country_data = df[country_name].tolist()
    slope, r_squared = fit_trendline(timestamps, country_data)
    return slope, r_squared
