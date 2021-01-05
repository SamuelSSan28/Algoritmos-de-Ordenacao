from random import randint
def quicksort2(A):
    if len(A)<=1: return A
    menor, igual, maior = [], [], []
    pivot = A[randint(0, len(A)-1)]

    for x in A:
        if x < pivot: menor.append(x)
        if x == pivot: igual.append(x)
        if x > pivot: maior.append(x)

    return quicksort2(menor) + igual + quicksort2(maior)
