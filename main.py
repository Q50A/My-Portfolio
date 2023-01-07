from functions import greet
from IP import IP
from lb1 import funnyface
from lb2 import change
from SillySentences import SillySentences
from RoomArea import RoomArea
from lb5 import PasswordGenerator
from lb6 import InputChecker
from Chatbot import Chatbot
from divideby3 import divideby3
from ASCII import ASCII
from lb4 import Leapyear
from lb7 import Age
from lb8 import Numberpyramid
from lb9 import Odd3
from PJA6 import PJA6
from PJA7 import calender
print("Welcome to my portfolio")
print("===================================")
print("===================================")
portfolio_state =True

while portfolio_state ==True:
  print("Labs:")
  print("1.  funnyfaces")
  print("2.  change")
  print("3.  facetalk")
  print("4.  PasswordGenerator")
  print("5.  InputChecker")
  print("6,  Leapyear")
  print("7.  Age")
  print("8.  Numberpyramid")
  print("9.  Odd3")
  print("10. greet")
  print("                                ")
  print("==========================================")
  print("                                ")
  print()
  print("Text Drawing!/ASCII")
  print("                                ")
  print("Cat")
  print("                                ")
  print("==========================================")
  print("                                ")
  print("Project Stem Assignments (PJA)")
  print("                                ")
  print("PJA1: Assignment 1: Silly Sentences")
  print("PJA2: Assignment 2: Room Area")
  print("PJA3: Assignment 3: Chatbot")
  print("PJA4: Assignment 4: Divisible by Three")
  print("PJA6: Assignment 6: Animation")
  print("PJA6: Assignment 7: Calender")
  print("                                ")
  print("==========================================")
  print("                                ")
  print("Games To Play!")
  print("                                ")
  print("(G1) Pong")
  print("                                ")
  print("==========================================")
  print("                                ")
  name_choice = input("Which assignment would you like to explore first? \nPlease be mindful of spaces, capitalizations,\nand random letters.\n\nLabs: (1,2,3,4,5,6,7,8,9,10) \n\nText Drawing: (Cat) \n\nProject Stem: (PJA1,PJA2,PJA3,PJA4,PJA6,PJA7) \n\nCode Games:G1 \n\nEnter Assignment Code:")
  print("                                ")
  print("                                ")
  if name_choice =="PJA1":
    SillySentences()
  elif name_choice =="1":
    IP()
  elif name_choice =="2":
    change()
  elif name_choice =="3":
    IP()
  elif name_choice =="PJA2":
    RoomArea()
  elif name_choice =="4":
    PasswordGenerator()
  elif name_choice =="5":
    InputChecker()
  elif name_choice =="PJA3":
    Chatbot()
  elif name_choice =="PJA4":
    divideby3()
  elif name_choice =="Cat":
    ASCII()
  elif name_choice =="6":
    Leapyear()
  elif name_choice =="7":
    Age()
  elif name_choice =="8":
    Numberpyramid()
  elif name_choice =="9":
    Odd3()
  elif name_choice =="10":
    greet()
  elif name_choice =="G1":
    IP()
  elif name_choice =="PJA6":
    IP()
  elif name_choice =="PJA7":
    calender()
    #PJA6 is an animation that uses simplegui so it can not the run trhough the console sorry
  else:
    print("That is not a Lab, please use the numbers given")

  playagain = input("Do you want to keep exploring my Portfolio? (y/n):")

if playagain != "y":
  name_choice = False
print("")