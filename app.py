from win32api import keybd_event

class Scraply: 
  def getVariable(prompt):
    inputX = raw_input(prompt) #  "Please enter something: ")
    print "You entered:" +  inputX
    
    if(inputX.length <= 0):
      print "Try again"
      return getVariable(prompt)
  
    return inputX
  
  def getInputs():
    username = getVariable("Enter Username:")
    password  = getVariable("Enter Password:")
    
    



if __name__ == "__main__":
  main()
