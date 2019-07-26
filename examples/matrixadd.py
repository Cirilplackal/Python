
#addition of 2 matrix from user 
# Program to add two matrices using nested loop
m=int(input("enter rows"));
n=int(input("enter columns"));
 
#in python initilization is needed before indexing.
matrix1=[[0 for j in range(0,n)] for i in range(0,m)]   # matrix 1 initialization with 0s
matrix2=[[0 for j in range(0,n)] for i in range(0,m)]    #matrix 2 intialization with 0s
print("enter first matrix elements")
for i in range(0,m):
	for j in range(0,n):
		matrix1[i][j]= int(input("enter an element"))
print("enter second matrix elements ")	
for i in range(0,m):
	for j in range(0,n):
		matrix2[i][j]=int(input("enter an element"))
	
result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(matrix1)):
   # iterate through columns
   for j in range(len(matrix1[0])):
       result[i][j] = matrix1[i][j] + matrix2[i][j]

for r in result:
   print(r)
