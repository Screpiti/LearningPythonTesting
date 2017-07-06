def testable(x):
    r"""
    The 'testable' function returns the square root of its parameter, or 3, whicever is larger.

    >>> testable(7)
    3.0

    >>> testable(16)
    4.0

    >>> testable(9)
    3.0

    >>> testable(10) == 10 ** 0.5
    True
    """

    if x < 9:
        return 3.0
    else:
        return x ** 0.5