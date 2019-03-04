from test_framework import generic_test

# DONE

def next_num(num):
    buf = []; i = 0
    while i < len(num):
        counter = 1
        while (i+1 < len(num)) and (num[i] == num[i+1]):
            i += 1; counter +=1
        buf.append(str(counter)); buf.append(num[i]);
        i += 1

    return ''.join(buf)

def look_and_say(n):
    num = '1'
    for _ in range(n-1):
        num = next_num(num)
   
    return str(num)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("look_and_say.py", "look_and_say.tsv",
                                       look_and_say))


import unittest

class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual( look_and_say(1), '1')
        self.assertEqual( look_and_say(2), '11')
        self.assertEqual( look_and_say(3), '21')

        
    def test2(self):
        self.assertEqual( next_num( '21'), '1211')
