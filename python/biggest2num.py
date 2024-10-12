#wap to find biggest of given 2 numbers from the command prompt 
a= int(input("The first: ")) 
b= int(input("The second: ")) 
if a<b :
  print( str(a) + " is smaller than " + str(b))
elif b<a :
  print( str(b) + " is smaller than " + str(a))
else :
  print( str(a) + " is equal to " + str(b))