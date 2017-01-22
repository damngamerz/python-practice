
# Input function
x=input("something:")

#open a file

fo = open("foo.txt","wb")
print("Name of the file :",fo.name)
print("Closed or not:",fo.closed)
print("Opening mode :",fo.mode)
fo.close()

#Write() method

fo= open("foo.txt","w")
fo.write("Python is a great language.\nYeah its great!!\n")
fo.close()

#open() method

fo=open("foo.txt","r+")
str=fo.read(10)
print("Read",str)
fo.close()

#using tell() and seek()
fo=open("foo.txt","r+")
str=fo.read(10)
print ("Read String is :",str)

position= fo.tell()
print("Current file posi: ",position)

position=fo.seek(0,0)
str=fo.read(10)
print("Read String afterwards is:",str)
fo.close()

