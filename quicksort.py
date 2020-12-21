import sys
sys.setrecursionlimit(10**8)
def quicksort(A, inicio=0, fim=None):
    contador_de_comparacoes = 0
    if fim is None:
        fim = len(A) - 1
        contador_de_comparacoes += 1
    if inicio < fim:
        contador_de_comparacoes += 1
        p, contador_de_comparacoes = partir(A, inicio, fim)
        contador_de_comparacoes += quicksort(A, inicio, p-1)
        contador_de_comparacoes += quicksort(A, p+1, fim)
    return contador_de_comparacoes

def partir (A, inicio, fim):
    pivot = A[fim]
    i = inicio
    contador_de_comparacoes = 0
    for j in range(inicio, fim):
        if A[j] <= pivot:
            contador_de_comparacoes += 1
            A[j], A[i] = A[i], A[j]
            i = i + 1
    A[i], A[fim] = A[fim], A[i]
    return i, contador_de_comparacoes
