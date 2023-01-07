
def Leapyear():
  #leap year is a year that has an extra day in february.
  #If you were born on February 29th, then you can only celebrate your birthday every 4 years on that date.
  # A tropical year is 365 days 5 hours 48 minutes 45 seconds and 138 milliseconds
  #Every 4 years make a leap year and that is the Julian Calendar
  # If the year is a multiple of 4 then its a leap year
  # If the year is a multiple of 100 then its not a leap year
  # If the year is a multiple of 400 then its a leap year
  # If the year is a mutliple of 10,000 or 10,000 + 2800 then its not a leap year
  #1752 is the start of the Gregoriann Calendar
  # If the year end in 2800 or 5600 or 8400 then thats not a leap year
  print("Want to know if your year is a leap year try inputting a random year if youn cant find one try using the year 2000")
  print()
  year = int(input('Enter year : '))
  if (year <= 1752):
    print("Leap years didn't exist back then!")
  
  elif year>10000 and (year-2800)%10000==0 and (year%100)==0:
    print("was NOT a leap year.")
  
  elif year<10000 and (year-2800)%10000==0:
    print(year, "was NOT a leap year.")
  
  elif year<10000 and (year-5600)%10000==0:
    print(year, "was NOT a leap year.")
  
  elif year<10000 and (year-8400)%10000==0:
    print(year, "was NOT a leap year.")
  
  else: #to tell what's a leap year
    if year % 400==0:
      print(year, "was a leap year.")
    elif year % 100!=0 and year % 4==0:
      print(year, "was a leap year.")
    else:
      print(year, "was NOT a leap year.")