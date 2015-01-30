from win32api import keybd_event

class Scraply: 
  
  
  def __init__(self, test):
      print "test: " + test 
      
  def getVariable(self, prompt):
    inputX = raw_input(prompt) #  "Please enter something: ")
    print "You entered:" +  inputX
    
    if(inputX.length <= 0):
      print "Try again"
      return getVariable(prompt)
  
    return inputX
  
  def getInputs(self ):
    username = getVariable("Enter Username:")
    password  = getVariable("Enter Password:")
    
    



if __name__ == "__main__":
  main()
