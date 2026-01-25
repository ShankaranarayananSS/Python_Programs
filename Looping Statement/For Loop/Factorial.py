#For Loop
#Factorial

fact = 1
num = int(input("Enter any number:"))
for i in range(1,num+1):
  fact = fact*i
print("Factorial of",num,"is",fact)
