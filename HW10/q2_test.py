shift_list = []

def substrings_with_gaps(P_list, T, i = 0, j = 0):
    global shift_list
    print "i = {}, j = {}".format(i, j)
    for s in range((len(T) - 1) - (len(P_list[j])-1) - (i - 1) + 1):
        if P_list[j] == T[s + i : s + i + len(P_list[j])]:
            if j < len(P_list) - 1:
                shift_list.append(s + i)
                return substrings_with_gaps(P_list, T, i + s + len(P_list[j]), j + 1)
            else:
                shift_list.append(s + i)
                return "Pattern matched"
    #Only reach if falls outside for loop
    return "Pattern not matched"

P = "ab,ba,c"
T = "cabccbabacab"
P_list = P.split(',')

print substrings_with_gaps(P_list, T)
print 'Shift list = ', shift_list
