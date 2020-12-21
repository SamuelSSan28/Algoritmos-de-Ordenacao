from heapsort import heapSort
from bubblesort import bubbleSort
from insertionsort import insertionSort
from mergesort import mergeSort
from quicksort import quicksort
import time

arquivo = "vetoresAleatorios"
vetoresAleatorios = open((arquivo+".txt"), "r")
vetores = []

def toInt(n):
      return int(n)

for i in vetoresAleatorios.readlines():
    vetores.append(list(map(toInt,i.split(","))))

resultado_heapSort = "resultado_heapSort.txt"
arquivo = open(resultado_heapSort, "w")
arquivo.close()

resultado_bubbleSort = "resultado_bubbleSort.txt"
arquivo = open(resultado_bubbleSort, "w")
arquivo.close()

resultado_insertionSort = "resultado_insertionSort.txt"
arquivo = open(resultado_insertionSort, "w")
arquivo.close()

resultado_mergeSort = "resultado_mergeSort.txt"
arquivo = open(resultado_mergeSort, "w")
arquivo.close()

resultado_quicksort = "resultado_quicksort.txt"
arquivo = open(resultado_quicksort, "w")
arquivo.close()

for vet in vetores:
    start_time = time.time()
    quantidade_de_comparacoes = heapSort(vet)
    tempo_de_execucao = (time.time() - start_time)
    #Arquivo de Resposta
    arquivo = open(resultado_heapSort, "a")
    arquivo.write("Quantidade de Elementos: {} \nQuantidade de comparacoes: {} \nTempo de execucao: {}".format(len(vet),quantidade_de_comparacoes,tempo_de_execucao))
    arquivo.write("\n \n")
    arquivo.close()

    start_time = time.time()
    quantidade_de_comparacoes = mergeSort(vet)
    tempo_de_execucao = (time.time() - start_time)
    #Arquivo de Resposta
    arquivo = open(resultado_mergeSort, "a")
    arquivo.write("Quantidade de Elementos: {} \nQuantidade de comparacoes: {} \nTempo de execucao: {}".format(len(vet),quantidade_de_comparacoes,tempo_de_execucao))
    arquivo.write("\n \n")
    arquivo.close()

    start_time = time.time()
    quantidade_de_comparacoes = bubbleSort(vet)
    tempo_de_execucao = (time.time() - start_time)
    #Arquivo de Resposta
    arquivo = open(resultado_bubbleSort, "a")
    arquivo.write("Quantidade de Elementos: {} \nQuantidade de comparacoes: {} \nTempo de execucao: {}".format(len(vet),quantidade_de_comparacoes,tempo_de_execucao))
    arquivo.write("\n \n")
    arquivo.close()

    start_time = time.time()
    quantidade_de_comparacoes = insertionSort(vet)
    tempo_de_execucao = (time.time() - start_time)
    #Arquivo de Resposta
    arquivo = open(resultado_insertionSort, "a")
    arquivo.write("Quantidade de Elementos: {} \nQuantidade de comparacoes: {} \nTempo de execucao: {}".format(len(vet),quantidade_de_comparacoes,tempo_de_execucao))
    arquivo.write("\n \n")
    arquivo.close()

    start_time = time.time()
    quantidade_de_comparacoes = quicksort(vet)
    tempo_de_execucao = (time.time() - start_time)
    #Arquivo de Resposta
    arquivo = open(resultado_quicksort, "a")
    arquivo.write("Quantidade de Elementos: {} \nQuantidade de comparacoes: {} \nTempo de execucao: {}".format(len(vet),quantidade_de_comparacoes,tempo_de_execucao))
    arquivo.write("\n \n")
    arquivo.close()
