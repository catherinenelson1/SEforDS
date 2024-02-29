from ch07_functions import weighted_mean, fit_trendline, process_sdg_data


def test_weighted_mean():
    result = weighted_mean([1, 1, 1], [1, 1, 1])

    assert result == 1

    empty_list_result = weighted_mean([], [])

    assert not empty_list_result


def test_fit_trendline():
    data = [1, 2, 3]
    timestamps = [2020, 2021, 2022]

    slope, r_squared = fit_trendline(timestamps, data)

    assert slope == 1
    assert r_squared == 1


def test_processing_trendline():
    df = process_sdg_data("../data/SG_GEN_PARL.xlsx")
    timestamps = [int(i) for i in df.index.tolist()]
    uk_parl = df["United Kingdom of Great Britain and Northern Ireland"].tolist()

    slope, r_squared = fit_trendline(timestamps, uk_parl)

    assert slope == 0.836
    assert r_squared == 0.868
