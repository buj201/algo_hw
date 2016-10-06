def compute_prefix_function(P):
    m = len(P)
    pi = {}
    pi[1] = 0
    k = 0
    for q in range(2, m+1):
        while k > 0 and P[k] != P[q - 1]:
            k = pi[k]
        if P[k] == P[q - 1]:
            k = k + 1
        pi[q] = k
    return pi.values()

P = 'ababbabbabbababbabb'
prefix_length = compute_prefix_function(P)

for i in range(len(P)):
    print '${}$'.format(P[:i+1]), '&', i + 1, '&', prefix_length[i], '\\\\'
    print '\hline'
