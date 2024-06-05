
def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left_half=arr[:mid]
        right_half=arr[mid:]
        mergesort(left_half)
        mergesort(right_half)

        i=0
        j=0
        k=0

        while i<len(left_half) and j<len(right_half):
            if left_half<right_half:
                arr[k]=left_half[i]
                i+=1
            else:
                arr[k]=right_half[j]
                j+=1
            k+=1        

        while i<len(left_half):
            arr[k]=left_half[i]
            i+=1
            k+=1
        while j<len(right_half):
            arr[k]=right_half[j]
            j+=1
            k+=1        


arr=[9,8,7,6,5,4,3,2,1]
print(arr)
mergesort(arr)
print(arr)
