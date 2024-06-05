






def selectionsort(arr):
    for i in range(len(arr)):
        cur_indx=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[cur_indx]:
                cur_indx=j
        arr[i],arr[cur_indx]=arr[cur_indx],arr[i]        
def insertionsort(arr):
    for i in range(1,range(arr)):
        j=1
        while arr[j-1]<arr[j] and j>0:
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j-=1
def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left_half=arr[:mid]
        right_half=arr[mid:]
        mergesort(left_half)            
        mergesort(right_half)    
        i=k=j=0
        while i<len(left_half) and j<len(right_half):
            if left_half[i]<right_half[j]:
                arr[k]=left_half[i]
                i+=1
                k+=1
            else:
                arr[k]=right_half[j]
                j+=1
                k+=1
        while i<len(left_half)  :
                arr[k]=left_half[i]
                i+=1
                k+=1 
        while j<len(right_half)  :
            arr[k]=right_half[j]
            j+=1
            k+=1       

arr=[8,9,4,52,55,77,88]
mergesort(arr)
print(arr)           
