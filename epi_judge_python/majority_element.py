from test_framework import generic_test

# DONE

def majority_search(stream):
    count, maj_element = 0, None
    for el in stream:
        if count == 0:
            count, maj_element  = 1, el
        elif maj_element != el:
            count -= 1
        else:
            count += 1

    return maj_element


def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("majority_element.py",
                                       'majority_element.tsv',
                                       majority_search_wrapper))
