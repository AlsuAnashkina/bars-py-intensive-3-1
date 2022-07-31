def counter(func):
    """
    Обертка для подсчёта количества вызовов обернутой функции.

    Returns:
        int - количество вызовов функции.
    """
    call_counter = 0
    def wrapper():
        nonlocal call_counter
        result = func()
        call_counter += 1
        print(call_counter)
        return result
    return wrapper
    raise NotImplementedError

# from common import some_func

# @counter
# def some_func():
#     pass
#
# some_func()
# some_func()
# some_func()
# print(some_func())