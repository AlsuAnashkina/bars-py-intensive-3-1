def get_next_date(some_date):
    """Возвращает следующую дату для заданной

    Args:
        some_date: определенная исходная дата

    Returns: следующая дата
    """
    from datetime import timedelta
    return some_date + timedelta(1)

    raise NotImplementedError
