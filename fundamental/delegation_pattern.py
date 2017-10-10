#!/usr/bin/env python
# encoding: utf-8


"""
@version: 2.7
@author: 'john'
@time: 2017/10/10 下午10:39
@contact: zhouqiang847@gmail.com
"""

"""
Reference: https://en.wikipedia.org/wiki/Delegation_pattern
Author: https://github.com/IuryAlves
"""


class Delegator(object):
    """
    >>> delegator = Delegator(Delegate())
    >>> delegator.do_something("nothing")
    'Doing nothing'
    >>> delegator.do_anything()
    """

    def __init__(self, delegate):
        self.delegate = delegate

    def __getattr__(self, name):
        def wrapper(*args, **kwargs):
            if hasattr(self.delegate, name):
                attr = getattr(self.delegate, name)
                if callable(attr):
                    return attr(*args, **kwargs)

        return wrapper


class Delegate(object):
    def do_something(self, something):
        return "Doing %s" % something


if __name__ == '__main__':
    delegator = Delegator(Delegate())
    print delegator.do_something("nothing")
    print delegator.do_anything()
