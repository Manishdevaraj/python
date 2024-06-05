

def gcd(a,b):
    
    while b:
        a,b=b,a%b

    return a;

n1=int(input("enter the no:"))    
n2=int(input("enter the no:"))    

print(gcd(n1,n2))