def rabin_karp_matcher(T, P, d, q):
    spurious_hits = []
    T_s = []
    n = len(str(T))
    m = len(str(P))
    h = d**(m - 1) % q
    p = 0
    t_0 = 0
    for i in range(m):
        p = (d*p + int(str(P)[i])) % q
        t_0 = (d*t_0 + int(str(T)[i])) % q
    T_s.append(t_0)
    for s in range(n - m + 1):
        if p == T_s[-1]:
            if P == int(str(T)[s:s + m]):
                print "Pattern occurs at shift ", s
                print "with pattern ", str(T)[s:s + m]
            else:
                print 'Spurious hit at shift ', s
                spurious_hits.append(s)
                print 'with pattern ', str(T)[s:s + m]
                print
        if s < n - m:
            t_next = (d*(T_s[-1] - int(str(T)[s])*h) + int(str(T)[s + m])) % q
            T_s.append(t_next)
    return spurious_hits

T = 3141592653589793
d = 10
q = 11
P = 26

print 'Running rabin-karp-matcher with'
print 'T = {}, P = {}, and q = {}'.format(T, P, q)
print

rabin_karp_matcher(T, P, d, q)

