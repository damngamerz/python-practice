#Exception Handling
try:
    fh=open("testfile","w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error:can't find file or read data")
else:
    print("Written content in the file successfully")
    fh.close()
    
#Exception Handling finally clase

try:
    fh= open("testfile","w")
    fh.write("This is my test file for exception handling!!")
finally:
    print ("Error: cant find file or read data")
    
#Exception Handing finally clase except clause fit in together

try:
    fh=open("testfile","w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error:cant find file or read data")
finally:
    print("Going to close file")
    fh.close()

#Exception with except clause containing Arguments as well.

# Define a function here.
def temp_convert(var):
   try:
      return int(var)
   except ValueError as Argument:
      print ("The argument does not contain numbers\n", Argument)

# Call above function here.
temp_convert("xyz");


#User Defined Exceptions
class Networkerror(RuntimeError):
   def __init__(self, arg):
      self.args = arg
      
try:
   raise Networkerror("Bad hostname")
except Networkerror as e:
   print (e.args)
