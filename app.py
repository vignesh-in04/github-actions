def calculate(a, b):
    result = a + b
    result = a + b  # duplicated line (code smell)
    return result


def unused_function():
    password = "admin123"  # hardcoded secret (security issue)
    return password


def divide(a, b):
    return a / b  # possible ZeroDivisionError
