def time_execution(func):
    """
    Обертка, печатающая время выполнения функции.
    """
    from datetime import datetime
    def wrapper(*args):
        start_time = datetime.now()
        result = func(*args)
        print(datetime.now() - start_time)
        return result

    return wrapper

    raise NotImplementedError

from common import factorial

# print(factorial(10))

decorate = time_execution(factorial)

print(type(decorate(10000)))

#
#
# from datetime import datetime
# def wrapper():
#     start_time = datetime.now()
#     x=0
#     for el in range(1000000):
#         x += 1
#     return (datetime.now() - start_time)
