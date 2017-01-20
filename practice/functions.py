#function is defined here
def printme (str):
        "This prints a passed strng into this function"
        print (str)
        return
        
#calling a function

printme("1st call")
printme("2nd call")
printme(str = 'My String')
        
#Pass by reference vs value

def changeme(mylist):
        "This changes a passed list into this function"
        print ("Values inside the function before change:",mylist)
        mylist[2]=50
        print ("Values inside the function after change:",mylist)
        return
        
        
#Calling change me function
mylist=[10,20,30]
changeme(mylist)
print ("Values outside the function:",mylist)

#Anonymous Functions
sum = lambda arg1,arg2:arg1+arg2

print ('Value of total : ',sum(10,20))
print ('Value of total : ',sum(20,30))

#Global vs local variable
total =0 #This is global Variable
def sum(arg1 , arg2):
        "Add both the parameters and return them"
        total = arg1+arg2;
        print("Inside the function local total:",total)
        return total
sum(10,20)
print("Outside the function global total:",total)                
