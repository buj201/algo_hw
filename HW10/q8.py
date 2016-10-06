#Manacher
import numpy as np

def longest_palindrome(S):
    S2 = '$#' + '#'.join(list(S)) + '#@'
    P = np.zeros(len(S2))
    C = 1 #Current center
    R = 1 #Right-most boundry of current palindrome

# Big idea- for every i we are either"
    # a. inside our current palindrome, or
    # b. outside.
# If we are a. inside, then
    # 1. if len[mirror] goes beyond L, initially set P[i] to (R - i)
    # 2. if len[mirror] is within L, initially set P[i] = P[mirror]
# 3. Expand beyond the minimum length from 1 & 2

    num_comparisons = 0

    for i in range(2, len(S2)-1):
        print
        print
        print "---------------------------------------------------------"
        print "Current i = {}".format(i)

        print 'C = {}'.format(C)
        print 'R = {}'.format(R)

        m = 2*C - i #Mirror position across current palindrome center

        print "m = {}".format(m)

        if i < R: #Case 1
            #Then i is inside the current palindrome
            #We then have two subcases:

            if R - i > P[m]: #Case 1a
                #Then, by symmetry, P[i] = P[m] since
                #the panindromes centered on mirr (and on i)
                #are both fully contained within the palindrome
                #centered on c
                P[i] = P[m]
            else: #R - i <= P[m], i.e. the palindrome centered
            # on mirr goes all the way to the left edge of the
            # current palindrome. Hence the palindrome centered on
            # i may continue past R, and thus need to continue
            # making comparisons.
                P[i] = R - i
                num_comparisons += 1
                while (S2[i-(1 + int(P[i]))] == S2[i + (1 + int(P[i]))]):
                    P[i] += 1
                    num_comparisons += 1

            #Since we've now looked right, if we found a palindrome that
            #Extends pass R should update.
                if (i + P[i] > R):
                    C = i
                    R = i + P[i]

        #Case 2:
            #i is outside the current palindrom and don't know anything about
            #P[i]. Then need to make comparisons from our base of P[i] = 0
        else:
            num_comparisons += 1
            while (S2[i-(1 + int(P[i]))] == S2[i + (1 + int(P[i]))]):
                P[i] += 1
                num_comparisons += 1

            #Since we've now looked right, if we found a palindrom that
            #Extends pass R should update.
            if (i + P[i] > R):
                C = i
                R = i + P[i]

        print 'P = {}'.format(P)

    print "Made {} comparisons".format(num_comparisons)

    max_span = int(np.max(P))
    max_center = int(np.argmax(P))
    start = max_center - max_span + 1
    stop = max_center + max_span
    max_subpal = ''.join(S2[start:stop:2])
    print max_subpal

    return P

print longest_palindrome('evenness')
