def weighted_mean(num_list, weights):
    if not (num_list or weights):
        return None
    running_total = 0
    for i in range(len(num_list)):
        running_total += num_list[i] * weights[i]
    return running_total / sum(weights)


from scipy.stats import linregress
import pandas as pd


def fit_trendline(year_timestamps, data):
    result = linregress(year_timestamps, data)
    slope = round(result.slope, 3)
    r_squared = round(result.rvalue**2, 3)
    return slope, r_squared


def process_sdg_data(excel_file, columns_to_drop):
    df = pd.read_excel(excel_file)
    df = df.drop(
        columns_to_drop,
        axis=1,
    )
    df = df.set_index("GeoAreaName").transpose()
    return df
