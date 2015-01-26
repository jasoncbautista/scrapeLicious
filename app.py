
def getVariable(prompt):

  input = raw_input(prompt) #  "Please enter something: ")
  print "you entered", input
  return input



def getInputs():
  
  username = getVariable("Enter Username:")
  
  if(username.length <= 0):
    print "Try again"
    getInputs()
    
  password  = getVariable("Enter Password:")
    
  if(password.length <= 0):
    print "Try again"
    getInputs()
    
