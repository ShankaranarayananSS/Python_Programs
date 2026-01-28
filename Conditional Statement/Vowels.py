vowels = ('a','e','i','o','u','A','E','I','O','U')
letter = input("Enter any letter:")
if letter[0] in vowels:
    print("\'",letter[0],"\' is a Vowel!")
else:
    print("\'",letter[0],"\' is a Consonant or Other character")
