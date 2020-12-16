def maximiza_heap(A, n, i):
	maior = i
	left = 2*i+1	 
	right = 2*i+2

	if left < n and A[maior] < A[left]:
		maior = left

	if right < n and A[maior] < A[right]:
		maior = right

	if maior != i:
		A[i], A[maior] = A[maior], A[i] 
		maximiza_heap(A, n, maior)


def heapSort(A):
	n = len(A)

	for i in range(n//2 - 1, -1, -1):
		maximiza_heap(A, n, i)

	for i in range(n-1, 0, -1):
		A[i], A[0] = A[0], A[i] 
		maximiza_heap(A, i, 0)