from random import randint
def quicksort2(A):
    contador_de_comparacoes = 0
    if len(A)<=1: 
        contador_de_comparacoes += 1
        return contador_de_comparacoes
    menor, igual, maior = [], [], []
    pivot = A[randint(0, len(A)-1)]

    for x in A:
        if x < pivot: 
            contador_de_comparacoes += 1
            menor.append(x)
        if x == pivot: 
            contador_de_comparacoes += 1
            igual.append(x)
        if x > pivot: 
            contador_de_comparacoes += 1
            maior.append(x)
    contador_de_comparacoes += quicksort2(menor)
    contador_de_comparacoes += 1
    contador_de_comparacoes += quicksort2(maior)
    return contador_de_comparacoes