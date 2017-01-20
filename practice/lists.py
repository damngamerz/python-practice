#Understanding Lists
list1 = ['physics','chemistry',1997,2000]
list2 = [1,2,3,4,5,6,7,8]

print ("list1[0]:",list1[0])
print ("list2[1:5]:",list2[1:5])

#Updating Lists
print ('Value of index 2 list1',list1[2])

list1[2]=2001

print ('New value of index 2 list1',list1[2])

#Deleting list elements

print (list1)

del list1[2]

print ('After Deletion of index 2:',list1)
