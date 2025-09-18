def count_common_elements(*lists):
    if not lists:
        return 0

    # Находим пересечение всех списков
    common_elements = set(lists[0])
    for lst in lists[1:]:
        common_elements = common_elements.intersection(set(lst))

    return len(common_elements)