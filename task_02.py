#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_02"""

import task_01


def fibo(count):
    """Function takes one argument count.
    Args:
        count(int): total no. of fibonacci numbers to return.
    Return:
        returns a list comprehension that uses task_01.xfibo() to generate count
        fibonacci no. and return them in a list.
    Examples:
        >>>fibo(5)
        [0, 1, 1, 2, 3]
    """
    return [f_num for f_num in task_01.xfibo(count)]
