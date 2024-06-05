

def largest(lst):
    if len(lst)<3:
        return "array size is less than 3"

    first=second=third=float('-inf') 

    for num in lst:
        if num>first:
            third=second
            second=first
            first=num
        elif num>second:
            second=first
            first=num
        elif num>third:
            third=num;
    return [first,second,third]    

lst=[20,50,30,300,200,100]    

print(largest(lst))