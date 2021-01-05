def insertionSort(A):
    contador_de_comparacoes = 0
    for i in range(1, len(A)):
        pivo = A[i]
        j = i - 1
        while j >= 0 and pivo < A[j]:
            contador_de_comparacoes += 1
            A[j+1]=A[j]
            j-=1
        A[j+1] = pivo
    return contador_de_comparacoes