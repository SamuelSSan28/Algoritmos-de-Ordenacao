
def recursiva (A, inicio, fim, contador_de_comparacoes):
    if fim - inicio <= 1:
        return
 
    meio = (inicio + fim)//2
    recursiva(A, inicio, meio, contador_de_comparacoes)
    recursiva(A, meio, fim, contador_de_comparacoes)
    #unir as partes:
    auxE = A[inicio:meio]
    auxD = A[meio:fim]
    i, j = 0, 0
    for k in range(inicio, fim):
        #print(i, j)
        contador_de_comparacoes += 1
        if i >= len(auxE):
            A[k] = auxD[j]
            j+=1
        elif j >= len(auxD):
            A[k] = auxE[i]
            i+=1
        elif auxE[i] < auxD[j]:
            A[k] = auxE[i]
            i+=1
        else:
            A[k] = auxD[j]
            j+=1
        k+=1
    return contador_de_comparacoes

def mergeSort (A,):
    contador_de_comparacoes = 0
    return recursiva (A, 0, len(A), contador_de_comparacoes)