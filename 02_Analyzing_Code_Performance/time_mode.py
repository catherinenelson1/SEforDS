import numpy as np
import timeit

random_integers = np.random.randint(1, 100_000, 1000)


def slow_way_to_calculate_mode(list_of_numbers):
    result_dict = {}
    for i in list_of_numbers:
        if i not in result_dict:
            result_dict[i] = 1
        else:
            result_dict[i] += 1
    mode = max(result_dict, key=result_dict.get)
    if result_dict[mode] == 1:
        return min(list_of_numbers)
    else:
        return mode


mode_timer = timeit.Timer(
    stmt="slow_way_to_calculate_mode(random_integers)",
    setup="from __main__ import slow_way_to_calculate_mode, random_integers",
)

time_taken = mode_timer.timeit(number=10)

print(f"Execution time: {time_taken} seconds")
