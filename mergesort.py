
def recursiva (A, inicio, fim):
    if fim - inicio <= 1:
        return
 
    meio = (inicio + fim)//2
    recursiva(A, inicio, meio)
    recursiva(A, meio, fim)
    #unir as partes:
    auxE = A[inicio:meio]
    auxD = A[meio:fim]
    i, j = 0, 0
    for k in range(inicio, fim):
        #print(i, j)
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

def mergeSort (A):
    recursiva (A, 0, len(A))