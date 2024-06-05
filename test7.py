

# def creatematrix(r,c):
#     matrix=[]
#     print("enter thr elemnt in row wise");
#     for i in range(r):
#         row=[]
#         for j in range(c):
#             row.append(int(input(f"enter the input row{i+1}, column {j+1} : ")))
#         matrix.append(row)
#     return matrix

     
# r1=int(input("enter the row"))      
# c1=int(input("enter the col1"))      
# r2=int(input("enter the row2"))      
# c2=int(input("enter the col2"))      
# matrix1=creatematrix(r1,c1);
# matrix2=creatematrix(r2,c2);

# if r1!=c2 or r2!=c2:
#     print("not identical matrix")

# else:
#     result=[ [0 for _ in range(c1)] for _ in range(r1)  ]

#     for i in range(r1):
#         for j in range(c1):
#            result[i][j]=matrix1[i][j]*matrix2[i][j]  


# print(result);


def creatematrix(r,c):
    matrix=[]
    for i in range(r):
        row=[]
        for j in range(c):
            row.append(int(input(f"enter thr no row {i+1}, column {j+1}")))
        matrix.append(row)

    return matrix
r1=int(input("enter the row"))      
c1=int(input("enter the col1"))      
r2=int(input("enter the row2"))      
c2=int(input("enter the col2"))      
matrix1=creatematrix(r1,c1);
matrix2=creatematrix(r2,c2);

if r1!=c1 or r2!=c2:
    print("not identical")
else:
    result=[[0 for _ in range(c1)] for _ in range(r1)]    

    for i in range(r1):
        for j in range(c1):
            result[i][j]=matrix1[i][j]+matrix2[i][j]


print(result)            