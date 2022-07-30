def get_days_count_by_month(month):
    """Возвращает количество дней по месяцу

    Args:
        month: название месяца

    Returns: количество дней
    """
    days_in_a_month = {'январь': 31, 'февраль': (28, 29), 'март': 31, 'апрель': 30, 'май': 31, 'июнь': 30,
                       'июль': 31, 'август': 31, 'сентябрь': 30, 'октябрь': 31, 'ноябрь': 30, 'декабрь': 31}
    for el in days_in_a_month.keys():
        if el == month:
            return days_in_a_month.get(el)
    else:
        return 0


    raise NotImplementedError

#print(get_days_count_by_month('февраль'))