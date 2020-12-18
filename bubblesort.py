def bubbleSort(A):
    while True:
        flag = False
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                flag = True
        if not flag: return