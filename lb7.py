def Age():
  print("Want to know if you can drive vote or watch movies just enter your age and see if your over 100 I hope your alive to proove me wrong ")
  print()
  age =int(input("What is your age?"))
  #drive
  if age >=100:
    print("You are " + str(age) +" and probably dead")
  elif age >=85:
    print("You are " + str(age) +" and are to old to drive")
  elif age >=18:
    print("You are " + str(age) + " and can drive on your own")
  elif age >=16:
    print("You are " + str(age) +" and need a permit to drive")
  elif age <16:
    print("You are " + str(age) +" and are to young to drive")
    #Vote
  if age >=18:
    print("You are " + str(age) + " and can vote")
  elif age <18:
    print("You are " + str(age) + " and can not vote")
    #Movie rights
  if age >=18:
    print("You are " + str(age) + " watch any rated movie")
  elif age ==17:
    print("You are " + str(age) + " you can watch any movie except X rated")
  elif age >=13 and age<17:
    print("You are " + str(age) + " and can watch any movie that is except for X or R rated")
  elif age<13:
    print("You are " + str(age) + " and can only watch Pg and G movies")