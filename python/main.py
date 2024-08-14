def fact(A, n=0):
    return A[0] + fact(A, n+1) if n != len(A) else A[0]


print(fact([1, 2, 3, 4, 5, 6]))
