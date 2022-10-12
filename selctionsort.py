def selectionsort(array,size):
    for step in range(size):
        min_idx=step
        for i in range(step+1,size):
            if array[i]<array[min_idx]:
                min_idx=i
                (array[step],array[min_idx])=(array[min_idx],array[step])
data=[-2,45,0,-9,56,4,78,-92]
size=len(data)
selectionsort(data,size)
print('sorted array in ascending order')
print(data)