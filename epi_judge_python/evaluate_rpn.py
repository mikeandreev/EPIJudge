from test_framework import generic_test

# DONE

def evaluate(expression):
    stack = []
    ops = {
        '+': lambda x, y: x+y,
        '-': lambda x, y: x-y,
        '*': lambda x, y: x*y,
        '/': lambda x, y: x//y
    }
    for token in expression.split(','):
        if token in ops:
            y = stack.pop(); x = stack.pop()
            stack.append(  ops[token](x, y) )
        else:
            stack.append(int(token))
    return stack.pop()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))
