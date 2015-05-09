#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_01"""


def xfibo(count):
    """Function creates Fibonacci sequence using generator
    Args:
        count(int):
    Return:
        returns the numbers in Fibonacci sequence starting with 0
    Examples:
        >>> 
        >>> for i in xfibo(5):
	print i

	
        0
        1
        1
        2
        3
    """
    firstnum, lastnum = 0, 1
    iterations = 0
    while iterations < count:
        yield firstnum
        firstnum, lastnum = lastnum, firstnum + lastnum
        iterations += 1
