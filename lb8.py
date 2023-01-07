def Numberpyramid():
  print("Want to see a number Pyramid well check this out try starting with the number #5 and work your way down from there")
  print()
  height = input("Enter an integer between 1 and 5: ")
  if height.isdigit() and  0<int(height)<=5:
    height =int(height)
    for i in range(height):
      row= i+1
      print(" "*2*(height-row),end="")
      for j in range(row,2*row):
        print(str(j)+" ", end="")
      print()
  else:
    print("That's not an integer between 1 and 5.")