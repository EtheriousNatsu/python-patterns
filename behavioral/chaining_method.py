#!/usr/bin/env python
# encoding: utf-8


"""
@version: 2.7
@author: 'john'
@time: 2017/10/10 下午10:24
@contact: zhouqiang847@gmail.com
"""

from __future__ import print_function


class Person(object):

    def __init__(self, name, action):
        self.name = name
        self.action = action

    def do_action(self):
        print(self.name, self.action.name, end=' ')
        return self.action


class Action(object):

    def __init__(self, name):
        self.name = name

    def amount(self, val):
        print(val, end=' ')
        return self

    def stop(self):
        print('then stop')

if __name__ == '__main__':

    move = Action('move')
    person = Person('Jack', move)
    person.do_action().amount('5m').stop()