list=[4,95,2,5,66,87,8,1]


def bubblesort(array):
	for i in range(len(array)):
		for j in range(len(array)-1):
			if array[j]> array[j+1]:
				array[j], array[j+1] = array[j+1], array[j]


bubblesort(list)

for i in range(len(list)):
	print(list[i])

