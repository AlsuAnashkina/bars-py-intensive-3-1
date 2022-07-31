def decorator_maker(func):
    """
    Обертка, которая повторяет вызов функции times раз с паузой delay секунд
    Args:
        times: количество повторений
        delay: задержка (с)

    Returns:
        валидное значение (при вызове bool() -> True)
    """
    from time import sleep
    def wrapper(times, delay):
        for el in range(times):
            result = func()
            if result == True:
                break
            sleep(delay)
        else:
            raise MyException

        return result
    return wrapper
    raise NotImplementedError


