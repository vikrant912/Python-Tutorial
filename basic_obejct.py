a=[5,4,7,9,11,12,9] #list will start from 0,1,2,3,4,5 value
a[2]=a[3] #this is assignment of obejct 3 in place of 2 
a[1]=100 #this is assignment of obejct 100 in place of 1
print(a)
result=a[1:3] #this is sclice 
print(result)


#####tuple has ( ) brackets values cannot be change like list 
c=(10,20,30,40) #this is tuple 
#c[2]=300  # this we tried for testing will give error 

print(c)

#set which does not hold any duplicate value 

d={1,2,3,4,55,55} #this is set {}

print(d)

# Dictionary containing key and value pairs separated by :
e = {'a': '1', 'q': '2', 'c': '3', 'd': '4'} 

# Accessing the value using the key 'q'
print(e['q'])

