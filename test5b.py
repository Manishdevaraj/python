

def binery(arr,l,h,k):
    if l<=h:
        mid=l+(h-l)//2
        if arr[mid]==k:
            return mid
        elif arr[mid]<k:
            return binery(arr,mid+1,h,k)
        elif arr[mid]>k:
            return binery(arr,l,mid-1,k)    
    else:
        return -1    

arr=[1,2,3,4,5,6,7]
n=len(arr)-1
print(binery(arr,0,n,6))