#For Loop
#Program to print 1 2 ... N
#Program to print N (N-1) ... 1

n = int(input("Enter any number:"))

#1 to N
print("Ascending Order:")
for i in range(0,n):
  print(i+1)
  
#N to 1
print("Descending Order:")
for i in range(n,0,-1):
  print(i)
