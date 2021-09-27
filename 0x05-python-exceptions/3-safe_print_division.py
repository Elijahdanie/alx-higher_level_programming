#!/usr/bin/python3
def safe_print_division(a, b):
    val = 0
    try:
        val = a/b
    except ZeroDivisionError:
        val = None
    finally:
        print("Inside Value {}".format(val))
    return val
