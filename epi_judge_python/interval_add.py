import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import PropertyName
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple('Interval', ('left', 'right'))

# DONE

def add_interval(disjoint_intervals, new_interval):
    res = []
    ins, ins_done = None, False
    def append_ins_if_any():
        nonlocal res, ins, ins_done
        if not ins_done:
            if ins is None: ins = new_interval
            res.append(ins)
            ins_done = True
    
    for interval in disjoint_intervals:
        if interval.right < new_interval.left:
            res.append(interval)
        elif new_interval.right < interval.left:
            append_ins_if_any()
            res.append(interval)
        else:
            if ins is None:
                ins = Interval(
                    min(interval.left, new_interval.left),
                    max(interval.right, new_interval.right)
                    )
            else:
                ins = Interval(ins.left, max(interval.right, ins.right))
    append_ins_if_any()
    return res


@enable_executor_hook
def add_interval_wrapper(executor, disjoint_intervals, new_interval):
    disjoint_intervals = [Interval(*x) for x in disjoint_intervals]
    return executor.run(
        functools.partial(add_interval, disjoint_intervals,
                          Interval(*new_interval)))


def res_printer(prop, value):
    def fmt(x):
        return [[e[0], e[1]] for e in x] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "interval_add.py",
            'interval_add.tsv',
            add_interval_wrapper,
            res_printer=res_printer))
