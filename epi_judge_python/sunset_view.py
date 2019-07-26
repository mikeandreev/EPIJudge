from test_framework import generic_test
import collections

# DONE

def examine_buildings_with_sunset(sequence):
    IdHeightPair = collections.namedtuple ('IdHeightPair', ('id' , 'height') )
    res = []
    for i, a in enumerate(sequence):
        while res and res[-1].height <= a:
            res.pop()
        res.append( IdHeightPair(i, a) )
    return [x.id for x in reversed(res)]


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sunset_view.py", 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
