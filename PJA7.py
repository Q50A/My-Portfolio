def calender():
#define the leap_yearfunction
  def leap_year(y):
      if y % 4 == 0 and(y % 100 != 0 or y % 400 == 0):
          return 1
      else :
          return 0
  
  # define the number_of_daysfunction
  def number_of_days(m, y):
      if m in [1, 3, 5, 7, 8, 10, 12]:
          return 31
      elif m in [4, 6, 9, 11]:
          return 30
      elif m == 2:
          return 28 + leap_year(y)
  
  # define the days_passedfunction
  def days_passed(d, m, y):
      days = 0
      for month in range(1, m):
          days += number_of_days(month, y)
      return days + d - 1
  
  # main program
  
  # get input from the user
  print("This is perfect for you if you want to calculate days in months or years like how much time we have until school ends")
  print()
  day = int(input("Please enter a day in numbers "))
  month = int(input("Please enter a month in numbers: "))
  year = int(input("Please enter a year in numbers: "))
  
  # display the menu and get the user 's choice
  print("Menu:")
  print("1) Calculate the number of days in the given month.")
  print("2) Calculate the number of days passed in the given year.")
  choice = int(input())
  
  # perform the selected action
  if choice == 1:
      print(number_of_days(month, year))
  elif choice == 2:
      print(days_passed(day, month, year))