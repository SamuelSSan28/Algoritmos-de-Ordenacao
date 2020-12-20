from heapsort import heapSort
from bubblesort import bubbleSort
from insertionsort import insertionSort
from mergesort import mergeSort
from quicksort import quicksort

vetoresAleatorios = open("vetoresAleatorios.txt", "r")
vetores = []

def toInt(n):
      return int(n)

for i in vetoresAleatorios.readlines():
    vetores.append(list(map(toInt,i.split(","))))

#teste heap
i = 1

#heapSort(vetores[i])
#bubbleSort(vetores[i])
insertionSort(vetores[i])
#mergeSort(vetores[i])
#quicksort(vetores[i])
print(vetores[i])
    