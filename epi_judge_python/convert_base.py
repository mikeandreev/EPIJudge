from test_framework import generic_test

# DONE

def convert_base(num_as_string, b1, b2):
    #if len(num_as_string) == 0 : return num_as_string
    negative = (num_as_string[0] == '-')
    ord0, ordA = ord('0'), ord('A')
    #
    num = 0
    for c in num_as_string[negative: ]:
        dig = ord(c)
        dig -= (ord0 if dig < ordA else ordA-10)
        num = num*b1 + dig
    # 
    str = []
    while True:
        dig = num % b2
        num = num // b2
        if dig < 10: str.append( chr(ord0 + dig))
        else: str.append( chr(ordA + dig - 10))
        if num == 0: break
    #
    if negative: str.append('-')
    return ''.join( reversed(str))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("convert_base.py", "convert_base.tsv",
                                       convert_base))
