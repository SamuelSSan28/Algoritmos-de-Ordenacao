from quicksort2 import quicksort2

#ordenamento misto baseado em bubble sort e quick sort

def mistoSort(A):
    vezes_bubble = 2
    #executa bubblesort n interacoes

    contador_de_comparacoes = 0
    for aux in range(vezes_bubble):
        flag = False
        for i in range(len(A)-1):
            contador_de_comparacoes += 1
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                flag = True
        if not flag: break

    #se nao tiver ordenado, faz o quicksort
    if flag:
        contador_de_comparacoes += quicksort2(A)

    return contador_de_comparacoes