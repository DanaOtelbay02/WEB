def sleep_in(weekday, vacation):
  if(weekday == True and vacation == False):
    return False
  elif(weekday == False and vacation == True):
    return True
  elif(weekday == False and vacation == False):
    return True
  elif(weekday == True and vacation == True):
    return True