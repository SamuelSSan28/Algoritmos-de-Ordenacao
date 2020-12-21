def bubbleSort(A):
    contador_de_comparacoes = 0
    while True:
        flag = False
        for i in range(len(A)-1):
            contador_de_comparacoes += 1
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                flag = True
        if not flag: return contador_de_comparacoes