def Odd3():
  print("I suggest looking back at the code for this one as it will tell you if you did it correctly or not through True and False")
  print()
  def is_odd_pow3(number):
    """Determines whether a number is an odd power of three."""
    """power =3
    while power < number:
      power*=9
    return number==power"""
    #solution 1
    if number <3:
      return False
    while number %9==0:
      number //=9
    return number ==3
    #solution 2
  """for x in range (7):
    if number <3 and number % 9==0:
      print(True)
    else:
      print (False)"""
  # You can modify these to test whether your function works
  print(is_odd_pow3(0)) # should print False
  print(is_odd_pow3(0.5)) # should print False
  print(is_odd_pow3(1)) # should print False
  print(is_odd_pow3(3)) # should print True
  print(is_odd_pow3(9)) # should print False
  print(is_odd_pow3(27)) # should print True
  print(is_odd_pow3(243)) # should print True
  print(is_odd_pow3(300)) # should print False
