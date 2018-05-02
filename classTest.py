# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# Hints:
# Use __init__ method to construct some parameters

class Test:
    """
        First ever class ever made in python - default output is I love apples
    """
    def __init__(self, string="apples"):
        self.string = string
    
    def getString(self,s):
        """
            Get string input from user
        """
        self.string = s

    def printString(self):
        """ 
            Print string
        """
        print("I love %s" % self.string)    

test = Test()
test.getString("cheese")
test.printString()