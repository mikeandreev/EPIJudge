from test_framework import generic_test
from test_framework.test_failure import TestFailure

# DONE

import functools

def int_to_string(x):
    
    s, sign = [], ''
    if x < 0: x *= -1; sign = '-'
    
    dig_zero = ord('0')
    while True:
        dig = x%10
        x = x // 10
        s.append( chr( dig_zero + dig ) )
        if x == 0: break
        
    if sign: s.append(sign)
    return ''.join(reversed( s ))


def string_to_int(s):
    if len(s) == 0: return 0
    dig_zero = ord('0')
    negative = (s[0] == '-')
    
    ####
    num = 0
    for dig in s[1 if negative else 0:]:
        num = num*10 + ( ord(dig)-dig_zero )
    ####
    
    ###
    #num = functools.reduce(lambda sum, dig: sum*10 + (ord(dig)-dig_zero) , s[1 if negative else 0:], 0)
    ###
        
    if negative: num *= -1
    return num


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
                                       
import unittest

class TestSolution(unittest.TestCase):
        
    def test1(self):
        self.assertEqual( int_to_string( 5 ), "5" )
        self.assertEqual( int_to_string( -5021 ), "-5021")
    def test2(self):
        self.assertEqual( string_to_int( "-5024"), -5024)
