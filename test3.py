##testing only...

def newTopic:
    print("test3...")
    sample = input("what is your type?")

while True:
  
  try:
    number = float(input("please enter decimal: "))
    break
  #value error handler
  except ValueError:
    print("you didn't enter a decimal")
  #unknown error handler  
  except: 
    print("unknown error occured")

print("thank you for entering a decimal")
