from common import MyException

def check_value(func):
    """
    Обертка, проверяющая валидность переданного значения(неотрицательный int).
    В случае валидного значения - передает дальше в функцию,
    в противном случае - выбрасывает исключение MyException.
    """
    def wrapper(*args):
        for el in args:
            if isinstance(el, int):
                if el >= 0:
                    continue
            else:
                raise MyException
        result = func(*args)
        return result
    return wrapper
    raise NotImplementedError

# decorated = check_value(print)
# # decorated(2, 3, 5, 6, 'jj')
# print(type(decorated(1, 2, 3)))
# # decorated(False)


