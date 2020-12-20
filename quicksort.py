def quicksort(A, inicio=0, fim=None):
    if fim is None:
        fim = len(A) - 1
    if inicio < fim:
        p = partir(A, inicio, fim)
        quicksort(A, inicio, p-1)
        quicksort(A, p+1, fim)

def partir (A, inicio, fim):
    pivot = A[fim]
    i = inicio
    for j in range(inicio, fim):
        if A[j] <= pivot:
            A[j], A[i] = A[i], A[j]
            i = i + 1
    A[i], A[fim] = A[fim], A[i]
    return i+1


