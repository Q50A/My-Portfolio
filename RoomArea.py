def RoomArea():
  print("Need to calculate your room area? Here is a calculator you can use for your measurments like with that 85 inch tv you want to hang.")
  print()
  side1 = float(input("Enter side A: "))
  
  side2 = float(input("Enter side B: "))
  
  side3 = float(input("Enter side C: "))
  
  side4 = float(input("Enter side D: "))
  
  side5 = float(input("Enter side E: "))
  
  rect1 = (side1 * side2)
  
  rect2 = (side4 - side2 - side5) * (side1 - side3)
  
  tri = (side1 - side3) * side5 * 0.5
  
  print("Room Area: " + str(rect1+ rect2+tri))