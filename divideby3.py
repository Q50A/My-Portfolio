def divideby3():
  print("Want to see if a number is divisble by 3 well you came to the right place enter any integer value and see what comes with it.")
  print()
  n = int(input("How many numbers do you need to check? "))
  
  divisible  = 0
  
  notdivisible  = 0
  
  for x in range(n):
  
   num = int(input("Enter number: "))
  
   if num % 3== 0:
  
       divisible += 1
  
       print(str(num)+" is divisible by 3.")
  
   else:
  
       notdivisible += 1
  
       print(str(num)+" is not divisible by 3.")
  
  print("You entered "+str(divisible )+" number(s) that are divisible by 3.")
  
  print("You entered "+str(notdivisible )+" number(s) that are not divisible by 3.")