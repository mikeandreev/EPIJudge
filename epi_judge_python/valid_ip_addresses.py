from test_framework import generic_test

# DONE

def is_valid_num(substr):
    #return len(substr) == 1 or (substr[0] != "0" and int(substr) < 256)
    length = len(substr)
    return (length==1 or (substr[0] !="0" and (length==2 or (length==3 and substr < "256")  )))
    
def get_valid_ip_address(s):
    valid_ips = []
    LEN = 4
    parts = [None] * LEN
    def hlp(substr, part):
        if part == LEN and not substr:
            valid_ips.append('.'.join(parts))
        if part == LEN or len(substr) < LEN - part:
            return
        for i in range(1,min(3,len(substr))+1):
            if is_valid_num(substr[:i]):
                parts[part] = substr[:i]
                hlp(substr[i:], part+1)
    hlp(s, 0)
    return valid_ips

def get_valid_ip_address_v2(s):
    valid_ips = []
    def hlp(pref, substr, dots_missing):
        if dots_missing == 0 and substr and is_valid_num(substr):
            valid_ips.append(pref+substr)
            
        if dots_missing == 0 or len(substr) < dots_missing + 1:
            return
        for i in range(1,min(4,len(substr))):
            if is_valid_num(substr[:i]):
                hlp(pref+substr[:i]+".", substr[i:], dots_missing-1)
    hlp("", s, 3)
    return valid_ips

def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "valid_ip_addresses.py",
            'valid_ip_addresses.tsv',
            get_valid_ip_address,
            comparator=comp))
