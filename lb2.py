def change():
  print("Want to know how much change you have with American and Canadian currency well enter the amount of money you have in integer values and you will understand how change works. ")
  print()
  num_pennies = int(input("Enter the number of pennies: "))
  num_nickels = int(input("Enter the number of nickels: "))
  num_dimes = int(input("Enter the number of dimes: "))
  num_quarters = int(input("Enter the number of quarters: "))
  num_loonies = int(input("Enter the number of loonies: "))
  num_toonies = int(input("Enter the number of toonies: "))
  penny_cost =num_pennies * 0.01
  nickle_cost =num_nickels * 0.05
  dime_cost =num_dimes  * 0.10
  quarter_cost =num_quarters * 0.25
  lonnie_cost =num_loonies * 0.74
  toonie_cost =num_toonies * 1.48
  # total_value = ...
  total_value = penny_cost + nickle_cost + dime_cost + quarter_cost + lonnie_cost + toonie_cost
    # this prints a blank line
  print("Number of pennies:", num_pennies)
  print("Number of nickels:", num_nickels)
  print("Number of dimes:", num_dimes)
  print("Number of quarters:", num_quarters)
  print("Number of loonies:", num_loonies)
  print("Number of toonies:", num_toonies)
  print("Total value of coins: $" + str(total_value))
  # print("Total value of coins: $" + str(total_value))
2