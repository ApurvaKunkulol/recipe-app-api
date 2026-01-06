from django.shortcuts import render

# Create your views here.
def division(dividend, divisor):
    """Divide given numbers"""
    if divisor == 0:
        raise ZeroDivisionError("Error: Division by zero attempted.")

    return dividend // divisor