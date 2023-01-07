def PasswordGenerator():
  import random# imports the random library
  
  def passwordGenerator():#defines the function password generator
      print("need a password this will generate you a random password you can use.")
      print()
      listOfAnimal=["cat", "dog", "mouse", "dragon", "frog"]#varaiable that generates random wors in quotes
  
      ani = random.choice(listOfAnimal)#the variable ani picks a random word form the varaible list of animal
  
      beginningNum = random.randint(-122273687627226854 , 23737392947664383)# the variable for the beginning numbers that connets the range of random numbers
  
      endNum = random.randint(1 , 1723262720482920)#the variable for the range of end numbers
  
      listOfChar=["!", "#", "@", "?"]#list of the cgarcters 
  
      char = random.choice(listOfChar)#random characters of your choice connceted from char to list of char variables
  
      newPassword = str(beginningNum) + ani + char + str(endNum)
  #defines the variable of the passwordGenerator and all the variables connected to it
      print(newPassword)#prints the new password
  
  passwordGenerator()#a function that prints infinite passwords
  print()
  print("Found a new password here play a dice game for fun if you roll number #2 eight times in a row I will personally congratulate you.")
  print()
  import random # inmports the library random
  from random import randint #imports randint from the random libarary 
  repeat = True #makes the repeat true
  while repeat: #defines a fucntion while its repeating
      print("You rolled",randint(1,6))    #picks a  random num form 1-6 and prints you rolled
      print("Do you want to roll again?") #asks to roll again
      repeat = ("y" or "yes") in input().lower() #if y or yes is said on input than the dice will roll again you can say them infinete for infinete rolls
