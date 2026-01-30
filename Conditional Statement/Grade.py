p = float(input("Enter your percentage:"))
if(p>=80 and p<=100):
  print("First class with distinction")
elif(p>=60 and p<80):
  print("First class")
elif(p>=40 and p<60):
  print("Second class")
elif(p>=0 and p<40):
  print("Fail!")
else:
  print("Invalid Input!")
