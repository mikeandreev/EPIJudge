from test_framework import generic_test

# DONE

def minimum_total_waiting_time(service_times):
    res, n = 0, len(service_times)
    service_times.sort()
    for i, st in enumerate(service_times):
        res += st*(n-1-i)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("minimum_waiting_time.py",
                                       'minimum_waiting_time.tsv',
                                       minimum_total_waiting_time))
