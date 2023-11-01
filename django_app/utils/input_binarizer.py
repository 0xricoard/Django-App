def transmission_binarizer(input):
  if (input == "Automatic"):
    return [1, 0, 0]
  elif (input == "Manual"):
    return [0, 1, 0]
  else:
    return [0, 0, 1]
  
def fueltype_binarizer(input):
  if (input == "Diesel"):
    return [1, 0, 0]
  elif (input == "Hybrid"):
    return [0, 1, 0]
  else:
    return [0, 0, 1]