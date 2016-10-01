#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01."""


import decimal


def fahrenheit_to_celsius(degrees):
    """This is formula to convert the degrees Fahrenheit to Celsius.

    Args:
        degrees(str): Just a random number.

    Returns:
        str: Calculated decimal number.

    Examples:
        >>> fahrenheit_to_celsius(212)
        Decimal('100')
        >>> fahrenheit_to_celsius(90)
        Decimal('32.22222222222222222222222222')
    """
    decimal_degrees = decimal.Decimal(degrees)
    decimal_32 = decimal.Decimal('32')
    decimal_5 = decimal.Decimal('5')
    decimal_9 = decimal.Decimal('9')
    return (decimal_degrees - decimal_32) * decimal_5 / decimal_9
