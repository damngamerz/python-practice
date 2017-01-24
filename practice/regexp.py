#Using Regular Expression in Python
import re

line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")
   
#Matching vs Searching

matchob=re.match(r'dogs',line,re.M|re.I)
if matchob:
    print("match-->matchob.group():",matchob.group())
else:
    print("No match Found")
    
searchob=re.search(r'dogs',line,re.M|re.I)
if searchob:
    print("search-->searchob.group():",searchob.group())
else:
    print("No match found")
