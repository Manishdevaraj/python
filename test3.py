


def cal_pow(b,e):
    if e==0:
        return 1;
    return b*cal_pow(b,(e-1));

b=int(input("enter the base number"))
e=int(input("enter the exponent number"))

print(cal_pow(b,e))
