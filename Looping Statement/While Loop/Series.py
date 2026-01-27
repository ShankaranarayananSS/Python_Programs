#While Loop
#Program to print 1 2 ... N
#Program to print N (N-1) ... 1

n = int(input("Enter any number:"))

#1 to N
print("Ascending Order:")
i=1
while(i<=n):
  print(i)
  i+=1
  
#N to 1
print("Descending Order:")
i=n
while(i>=1):
  print(i)
  i-=1
