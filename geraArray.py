from random import randint

N = [100,500,1000,5000,30000,80000,100000,150000,200000]

#a. Vetor em ordem crescente;
vetoresCrecentes = []
for n in N:
    vet = list(range(0,n))
    vetoresCrecentes.append(vet)

#b. Vetor em ordem decrescente;
vetoresDecrecentes = []
for n in N:
    vet = list(range(n,0,-1))
    vetoresDecrecentes.append(vet)

#c. Vetor aleatório.
vetoresAleatorios = []
for n in N:
    vet = []
    for i in range(0,n):
        vet.append(randint(0,n))
    vetoresAleatorios.append(vet)

#salvando vetores em um arquivo
arquivo = open("vetoresCrecentes.txt", "w")
for i in vetoresCrecentes:
    arquivo.write((str(i)).replace("[","").replace("]",""))
    arquivo.write("\n")

#salvando vetores em um arquivo
arquivo = open("vetoresDecrecentes.txt", "w")
for i in vetoresDecrecentes:
    arquivo.write((str(i)).replace("[","").replace("]",""))
    arquivo.write("\n")

#salvando vetores em um arquivo
arquivo = open("vetoresAleatorios.txt", "w")
for i in vetoresAleatorios:
    arquivo.write((str(i)).replace("[","").replace("]",""))
    arquivo.write("\n")