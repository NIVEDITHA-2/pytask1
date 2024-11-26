mat1=[[3,4],[5,2]]
mat2=[[1,5],[6,7]]
mat3=[[0,0],[0,0]]
for i in range(len(mat1)):
    for j in range(len(mat2)):
        mat3[i][j]=(mat1[i][0]*mat2[0][j]+mat1[i][1]*mat2[1][j])
for i in mat3:
    print(i)