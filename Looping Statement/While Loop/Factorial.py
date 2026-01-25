#While Loop
#Factorial

i,fact = 1,1
num = int(input("Enter any number:"))
while(i<=num):
  fact = fact*i
  i=i+1
print("Factorial of",num,"is",fact)
