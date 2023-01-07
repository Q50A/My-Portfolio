def Chatbot():
  import random
  yes = random.randint(90, 100)
  print("Answer these basic questions they will help you land any job I promise these are the hardest interview questions imaginable")
  print()
  shoe = input("What's your favorite shoes? ")
  if shoe == "sneakers":
      print("I like sneakers too!")
  elif shoe == "boots":
      print("Boots aren't for me.")
  else:
      print("Nice choice")
     
  color = input("What's your favorite color? ")
  if color == "blue":
      print("Blue is the best color.")
  elif color == "green":
      print("Green is the color of nature, I love it as well.")
  else:
      print("That's not my type of color.")
     
  food = input("What's your favorite food? ")
  if food == "chocolate":
      print("I love chocolate, and chocolate cake!")
  elif food == "chicken" or "rice":
      print("I LIVE FOR THOSE FOOD!!")
  else:
      print("Good food choice")
  
  age = int(input("What's your age "))
  if age == 16:
      print("I guess being a teen makes you like the night huh.")
  else:
      print("good times to be " + str(age))
  
  music = input("What's your favorite music genre? ")
  if music == "classical":
      print("Classical music are the best!")
  elif music == "hip-hop":
      print("I like those too!")
  else:
      print("That's not my type of music.")
  
  print("You are this awesome from the scale of 1-100! " + str(yes))