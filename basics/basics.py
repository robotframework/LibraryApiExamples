def keyword():
    pass

def argument(arg):
    pass

def two_arguments(arg1, arg2):
    pass

def default_values(arg1, arg2='default value', arg3='2nd default'):
    print '%s, %s, %s' % (arg1, arg2, arg3)

def varargs(*args):
    print args

def kwargs(**args):
    print args

def combined(arg1, arg2=2, *varargs, **kwargs):
    pass

def use_print():
    print 'Hello, world!'

import time

def print_with_levels():
    print '*INFO* Hello, world!'
    time.sleep(0.1)
    print '*INFO* Second message (<b>not bold</b>)'
    print '*HTML* <b>HTML</b> message'
    print '*DEBUG* Debug message'

import logging

def use_standard_logging():
    logging.info('Hello, world!')
    time.sleep(0.1)
    logging.debug('Debug, world!')
    

from robot.api import logger

def use_robot_logger():
    logger.info('Hello, world!')
    time.sleep(0.1)
    logger.debug('Debug, <b>world</b>!', html=True)


def buggy_keyword():
    not_defined


def should_be_positive(number):
    if float(number) <= 0:
        raise AssertionError('%s is not positive' % number)

def should_be_negative(number):
    if float(number) >= 0:
        error = AssertionError('%s is not negative' % number)
        error.ROBOT_CONTINUE_ON_FAILURE = True
        raise error


def add(*numbers):
    return sum(float(n) for n in numbers)


def get_unit(name):
    return Unit(3, name, 'foo')


class Unit(object):

    def __init__(self, id, name, type):
        self.id = str(id)
        self.name = name
        self.type = type


def _private():
   pass
