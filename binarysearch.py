
'''test cases 
1) no input (null) both
2) empty matrix both
3) 1x1 both
4) rectangular matrix only 1st problem
5) square matrix
'''
'''
binary search on a matrix
'''

 
R = int(input("number of rows:"))
C = int(input("number of columns:"))

mat = []
print("Enter row wise:")


for i in range(R):          
    a =[]
    for j in range(C):      
        a.append(int(input()))
    mat.append(a)

for i in range(R):
    for j in range(C):
        print(mat[i][j], end = " ")
    print()


m = len(mat)
n = len(mat[0])
for i in range(n):
    mat[0][i],mat[2][i]=mat[2][i],mat[0][i]
for i in range(m):
    for j in range(0,i):
        if i!=j:
            mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
print(mat)