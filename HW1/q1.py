def max_index(A):
    max_val = A[0]
    max_index = 0
    for index in range(1, len(A)):
        candidate = A[index]
        if max_val < candidate:
            max_val = candidate
            max_index = index
    return max_index

test_A = [5,2,4,6,1,3]

print max_index(test_A)
