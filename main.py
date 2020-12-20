from heapsort import heapSort

vetoresAleatorios = open("vetoresAleatorios.txt", "r")
vetores = []

def toInt(n):
      return int(n)

for i in vetoresAleatorios.readlines():
    vetores.append(list(map(toInt,i.split(","))))

#teste heap
i = -1
heapSort(vetores[i])
print(len(vetores[i]))
    