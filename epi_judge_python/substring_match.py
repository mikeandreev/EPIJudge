from test_framework import generic_test

# DONE : Boyer-Moore-Horspool
# DONE : Rabin-Karp

def boyer_moore_horspool(string, pat):
    patlen = len(pat)
    if patlen == 0: return 0
    #if patlen > len(string): return -1
    delta, def_delta = {}, patlen
    for j in range(patlen-1):
        delta[pat[j]] = patlen-1-j
    lastch = pat[patlen-1]
    i = patlen-1
    while i < len(string):
        ch = string[i]
        if ch == lastch:
            if string[i-patlen+1: i+1] == pat:
                return i-patlen+1
        i += delta.get(ch, def_delta)
    return -1

def rabin_karp(string, pat):
    patlen = len(pat)
    if patlen == 0: return 0
    if patlen > len(string): return -1
    N = 256 # 'size of the alphabet'
    P = 101 # prime number for rolling hash
    def _hash(s):
        slen, h = len(s), 0
        for i in range(slen):
            h = ( h * N + ord(s[i]) ) % P
        return h
    
    base = 1
    for i in range(len(pat)-1):
        base = (base*N)%P
    
    def roll_hash(h, old, new):
        return (N*(h-old*base) + new )%P
        
    hpat = _hash(pat)
    hstr = _hash(string[:patlen])
    for i in range(len(string)-patlen+1):
        if i > 0:
            hstr = roll_hash(hstr, ord(string[i-1]), ord(string[i+patlen-1]) )
        #if hstr != _hash(string[i:i+patlen]):
        #    print(f"\n*** {string} || {pat}")
        #    print(f"*** hpat={hpat}")
        #    print(f"*** hstr={hstr} // {_hash(string[i:i+patlen])} // {string[i:i+patlen]}")
        #    raise RuntimeError('has missmatch')
        if hpat == hstr and string[i:i+patlen] == pat:
            return i
    return -1

def search(t, s):
    return rabin_karp(t, s)
    #return t.find(s)
    #return boyer_moore_horspool(t, s)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("substring_match.py",
                                       'substring_match.tsv', search))
