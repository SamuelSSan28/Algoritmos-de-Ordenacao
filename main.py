from heapsort import heapSort
from bubblesort import bubbleSort
from insertionsort import insertionSort
from mergesort import mergeSort
from quicksort import quicksort
from mistosort import mistoSort
import time

def lerArquivo(nome):
    arquivo = nome
    vetoresAleatorios = open((arquivo+".txt"), "r")
    vetores = []
    for i in vetoresAleatorios.readlines():
        vetores.append(list(map(toInt,i.split(","))))
    return vetores

def toInt(n):
      return int(n)


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

resultado_mistoSort = "resultado_mistosort.txt"
arquivo = open(resultado_mistoSort, "w")
arquivo.close()

print('Executando Misto Sort')
vetores = lerArquivo("vetoresAleatorios")
for vet in vetores:
    print('Rodando para vetor de tamanho '+str(len(vet)))
    start_time = time.time()
    quantidade_de_comparacoes = mistoSort(vet)
    try: quantidade_de_comparacoes = mistoSort(vet)
    except: print('Erro')
    else:
        tempo_de_execucao = (time.time() - start_time)
        #Arquivo de Resposta
        arquivo = open(resultado_mistoSort, "a")
        arquivo.write("Quantidade de Elementos: {} \nQuantidade de comparacoes: {} \nTempo de execucao: {}".format(len(vet),quantidade_de_comparacoes,tempo_de_execucao))
        arquivo.write("\n \n")
        arquivo.close()

'''
print('Executando Heap Sort')
vetores = lerArquivo("vetoresAleatorios")
for vet in vetores:
    print('Rodando para vetor de tamanho '+str(len(vet)))
    start_time = time.time()
    try: quantidade_de_comparacoes = heapSort(vet)
    except: print('Erro')
    else:
        tempo_de_execucao = (time.time() - start_time)
        #Arquivo de Resposta
        arquivo = open(resultado_heapSort, "a")
        arquivo.write("Quantidade de Elementos: {} \nQuantidade de comparacoes: {} \nTempo de execucao: {}".format(len(vet),quantidade_de_comparacoes,tempo_de_execucao))
        arquivo.write("\n \n")
        arquivo.close()

print('Executando Merge Sort')
vetores = lerArquivo("vetoresAleatorios")
for vet in vetores:
    print('Rodando para vetor de tamanho '+str(len(vet)))
    start_time = time.time()
    try: quantidade_de_comparacoes = mergeSort(vet)
    except: print('Erro')
    else:
        tempo_de_execucao = (time.time() - start_time)
        #Arquivo de Resposta
        arquivo = open(resultado_mergeSort, "a")
        arquivo.write("Quantidade de Elementos: {} \nQuantidade de comparacoes: {} \nTempo de execucao: {}".format(len(vet),quantidade_de_comparacoes,tempo_de_execucao))
        arquivo.write("\n \n")
        arquivo.close()

print('Executando Bubble Sort')
vetores = lerArquivo("vetoresAleatorios")
for vet in vetores:
    print('Rodando para vetor de tamanho '+str(len(vet)))
    start_time = time.time()
    try: quantidade_de_comparacoes = bubbleSort(vet)
    except: print('Erro')
    else:
        tempo_de_execucao = (time.time() - start_time)
        #Arquivo de Resposta
        arquivo = open(resultado_bubbleSort, "a")
        arquivo.write("Quantidade de Elementos: {} \nQuantidade de comparacoes: {} \nTempo de execucao: {}".format(len(vet),quantidade_de_comparacoes,tempo_de_execucao))
        arquivo.write("\n \n")
        arquivo.close()

print('Executando Insertion Sort')
vetores = lerArquivo("vetoresAleatorios")
for vet in vetores:
    print('Rodando para vetor de tamanho '+str(len(vet)))
    start_time = time.time()
    try: quantidade_de_comparacoes = insertionSort(vet)
    except:
        print('Erro')
    else:
        tempo_de_execucao = (time.time() - start_time)
        #Arquivo de Resposta
        arquivo = open(resultado_insertionSort, "a")
        arquivo.write("Quantidade de Elementos: {} \nQuantidade de comparacoes: {} \nTempo de execucao: {}".format(len(vet),quantidade_de_comparacoes,tempo_de_execucao))
        arquivo.write("\n \n")
        arquivo.close()

print('Executando Quick Sort')
vetores = lerArquivo("vetoresAleatorios")
for vet in vetores:
    print('Rodando para vetor de tamanho '+str(len(vet)))
    start_time = time.time()
    try: quantidade_de_comparacoes = quicksort(vet)
    except: print('Erro')
    else:
        tempo_de_execucao = (time.time() - start_time)
        #Arquivo de Resposta
        arquivo = open(resultado_quicksort, "a")
        arquivo.write("Quantidade de Elementos: {} \nQuantidade de comparacoes: {} \nTempo de execucao: {}".format(len(vet),quantidade_de_comparacoes,tempo_de_execucao))
        arquivo.write("\n \n")
        arquivo.close()
'''