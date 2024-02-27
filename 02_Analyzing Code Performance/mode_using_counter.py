import numpy as np
from collections import Counter


def mode_using_counter(n_integers):
    random_integers = np.random.randint(1, 100_000, n_integers)
    c = Counter(random_integers)
    return c.most_common(1)[0][0]


if __name__ == "__main__":
    print(mode_using_counter(10_000_000))
