def weighted_mean(num_list, weights):
    running_total = 0
    for i in range(len(num_list)):
        running_total += num_list[i] * weights[0]
        breakpoint()
    return running_total / len(num_list)


weighted_mean([1, 6, 8], [1, 3, 2])
