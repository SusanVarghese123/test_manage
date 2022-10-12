def linersearch(array,n,x):
    for i in range(0,9):
        if(array[i]==x):
            return i
        return -1
array=[2,4,0,1,9]
x=4
n=len(array)
result=linersearch(array,n,x)
if(result==1):
    print("element not found")
else:
    print ("element found at index:",result)

