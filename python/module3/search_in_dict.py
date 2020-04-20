def search_in_dict(list_or_set, dict):
    new_set = set()
    for i in list_or_set:
        if i in dict:
            new_set.add(i)
    return new_set
