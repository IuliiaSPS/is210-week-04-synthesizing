#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01."""


import decimal


def fahrenheit_to_celsius(degree):
    """This is formula to convert the degrees Fahrenheit to Celsius.

    Args:
        degree(mixed): Just a random number.

    Returns:
        Mixed: Calculated decimal number.

    Examples:
        >>> fahrenheit_to_celsius(212)
        Decimal('100')
        >>> fahrenheit_to_celsius(90)
        Decimal('32.22222222222222222222222222')
    """
    decimal_degree = decimal.Decimal(degree)
    decimal_32 = decimal.Decimal('32')
    decimal_5 = decimal.Decimal('5')
    decimal_9 = decimal.Decimal('9')
    return (decimal_degree - decimal_32) * decimal_5 / decimal_9
