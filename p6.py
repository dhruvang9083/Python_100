class InputOutString(object):
    def __init__(self,s1):
    	self.s1=s1
    def getString(self):
    	return self.s1
    def printString(self):
    	print(self.s1.upper())
Obj=InputOutString("milin")
Obj.getString()
Obj.printString()
