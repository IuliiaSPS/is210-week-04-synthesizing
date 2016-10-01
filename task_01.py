#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01."""


import decimal


ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


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
    decimal_degrees = decimal.Decimal(str(degrees))
    decimal_32 = decimal.Decimal('32')
    decimal_5 = decimal.Decimal('5')
    decimal_9 = decimal.Decimal('9')
    return (decimal_degrees - decimal_32) * decimal_5 / decimal_9


def celsius_to_kelvin(degrees):
    """This formula to convert the degrees Celsius to Kelvin"

    Args:
        degrees(str): Just a random number.

    Returns:
        str: sum of degrees and ABSOLUTE_DIFFERENCE.

    Examples:
        >>>celsius_to_kelvin(100)
        Decimal('373.15')
        >>>celsius_to_kelvin(1)
        Decimal('274.15')
    """
    return decimal.Decimal(str(degrees)) + ABSOLUTE_DIFFERENCE
