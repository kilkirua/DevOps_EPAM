def lists_2_dict(list1, list2):
    dict = {}
    for key in list1:
        for value in list2:
            dict[key] = value
            list2.remove(value)
            break
    return dict
