def swap_max_and_min(list):
    maximum = max(list)
    minimum = min(list)
    if len(list) != len(set(list)):
        raise ValueError()
    for i in range(len(list)):
        if list[i] == maximum:
            list[i] = minimum
        elif list[i] == minimum:
            list[i] = maximum
    return list
