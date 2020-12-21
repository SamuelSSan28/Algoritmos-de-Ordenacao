def maximiza_heap(A, n, i):
	maior = i
	left = 2*i+1	 
	right = 2*i+2
	contador_de_comparacoes = 0

	if left < n and A[maior] < A[left]:
		maior = left
		contador_de_comparacoes += 1

	if right < n and A[maior] < A[right]:
		contador_de_comparacoes += 1
		maior = right

	if maior != i:
		contador_de_comparacoes += 1
		A[i], A[maior] = A[maior], A[i] 
		contador_de_comparacoes += maximiza_heap(A, n, maior)
	
	return contador_de_comparacoes


def heapSort(A):
	n = len(A)
	contador_de_comparacoes = 0

	for i in range(n//2 - 1, -1, -1):
		contador_de_comparacoes += maximiza_heap(A, n, i)

	for i in range(n-1, 0, -1):
		A[i], A[0] = A[0], A[i] 
		contador_de_comparacoes +=maximiza_heap(A, i, 0)
	
	return contador_de_comparacoes