# matrix multiplication
def matmul(mat1,mat2):
    prod = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            row.append(0)
        prod.append(row)

    for i in range (len(mat1)):             # i  is row of mat1
        for j in range (len(mat1[0])):      #j is column of mat1 = row of mat2
            for k in range (len(mat2)):     #k is column of mat2 
                prod[i][k]+= mat1[i][j]*mat2[j][k]   # res[i][k] = sum (mat1[i][j]*mat2[j][k])

    print(prod)



mat1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

mat2 = [
    [1,4,7],
    [2,5,8],
    [3,6,9]
]

matmul(mat1,mat2)