def InputChecker():
    print("answer these extremally hard questions carefully they are going to be on Mrs Ramirez's test")
    print()
    input_1 = input("Enter a 4-digit whole number: ")
    if len(input_1)==4 and input_1.isdecimal() and input_1[0]!="0":
     print("Thanks!")
    else:
     print("That's not a 4-digit number.")
    
    input_2 = int(input("Enter an integer less than 50: "))
    if input_2 < 50:
     print("Thanks")
    else :
     print("That's not a number less than 50.")
    
    input_3 = str(input("Enter a string that begins with a vowel: "))
    vowel = 'a','e','i','o','u'
    if input_3.startswith(vowel):
      print("Thanks!")
    else:
     print("That does not begin with a vowel.")
    
    input_4 = input("Enter a string that ends with a consonant: ")
    if input_4.endswith(vowel):
     print("That does not end with a consonant")
    else:
     print("Thanks!")
