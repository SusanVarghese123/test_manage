def insertionsort(array):
    for step in range(1,len(array)):
        key = array[step]
        j=step -1
        while j>=0 and key<array[j]:
            array[j+1]=array[j]
            j=j-1
            array[j+1]=key

data=[9,5,1,4,3]
data=[89,23,3,4,54]
insertionsort(data)
print('sorted arry in ascending order')
print(data)
print(data)
