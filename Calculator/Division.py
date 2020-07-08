def division(a, b):
    try:
        a = float(a)
        b = float(b)
        return round(b / a, 9)
    except ZeroDivisionError:
        return "Division by zero"
