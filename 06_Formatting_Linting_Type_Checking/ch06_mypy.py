from collections import Counter


def mode_using_counter(some_list: float) -> float:
    c = Counter(some_list)
    return c.most_common(1)[0][0]


from typing import List


def mode_using_counter(some_list: List[float]) -> float:
    c = Counter(some_list)
    return c.most_common(1)[0][0]
