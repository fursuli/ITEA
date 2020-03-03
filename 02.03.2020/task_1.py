"""
 Сворити декоратор з аргументами.
 Створений декоратор викликає функцію певну кількість разів,
 як результат - виводить кількість витраченого часу на
 виконання даної функції і її назву.
 """

import time


def decorator(repeats):

    def actual_decorator(func):

        def wrapper(*args, **kwargs):

            start_time = time.time()
            results = []

            for i in range(repeats):
                result = func(*args, **kwargs)
                func_time = round((time.time() - start_time), ndigits=5)
                results.append((result, func_time))
                print(f'Function {i} time: {func_time} (Function - {func.__name__})')

            return results, func.__name__
        return wrapper
    return actual_decorator


@decorator(55)
def func(x, y):
    return x ** y


func(5, 66)
