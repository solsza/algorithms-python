def intersection(a, b):
    set_a = set(a)
    intersection_tab = []
    for item in b:
        if item in set_a:
            intersection_tab.append(item)
    return intersection_tab
    # return [item for item in b if item in set_a] -> one line solution