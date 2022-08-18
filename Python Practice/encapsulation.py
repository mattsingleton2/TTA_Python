#   Create a class that uses encapsulation.
#   Requirements:
#       Class should make use of a private attribute or function.
#       Class should make use of a protected attribute or function.
#       Create an object that makes use of protected and private.
#       Add comments through your Python script explaining your code.

class Customer:
    def __init__(self):
        #   Unprotected variable as a name. Easy enough
        self.name = "Matt"
        #   Now for a protected variable. Accessible, but a little harder.
        self._age = 33
        #   Now for the juicy stuff. We only want the method controlling access to this info.
        self.__socialSecurity = "111-11-1111"

#   Since we've got this set to private, we need a get;set; way to handle them.
#   First we get        
    def getSSN(self):
        return self.__socialSecurity
    
#   Then we set    
    def setSSN(self,SSN):
        self.__socialSecurity = SSN


if __name__ == "__main__":
    obj = Customer()
    print(obj.getSSN())
    obj.setSSN("222-22-2222")
    print(obj.getSSN())


