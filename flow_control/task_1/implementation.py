def get_numbers():
    """Возвращает все числа от 1000 до 2000, которые делятся на 7, но не кратны 5

    Returns: итерируемый объект с нужными числами
    """
    multiple_of_7_list = []
    for el in range(1000, 2001):
        if all([el % 7 == 0, el % 5 != 0]):
            multiple_of_7_list.append(el)
    return multiple_of_7_list
    raise NotImplementedError

