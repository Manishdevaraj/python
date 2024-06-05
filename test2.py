





def nwtsqrt(n):
    approx=n*0.5;
    better= 0.5*(approx+n/approx)
    while approx!=better:
        approx=better
        better=0.5*(approx+n/approx)

    return approx
n=int(input("enter the no"))    

print(nwtsqrt(n))