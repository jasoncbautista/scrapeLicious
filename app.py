
def getVariable(prompt):

  input = raw_input(prompt) #  "Please enter something: ")
  print "you entered", input
  return input



def getInputs():
  
  username = getVariable("Enter Username:")
  
  if(username.length <= 0):
    print "Try again"
    getInputs()
    
  
