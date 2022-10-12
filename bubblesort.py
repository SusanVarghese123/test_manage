def bubblesort(array):
    for i in range(len(array)):
        swapped=False
        for j in range(0,len(array)-i-1):
            if array[j]>array[j+1]:
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp
                swapped=True
        if not swapped:
            break
data=[-100,0,12,14,13,7.4,-54,-45,34,56]
bubblesort(data)
print(data)