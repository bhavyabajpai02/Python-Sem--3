# Program to display all position of substring in a given main string
s = input("Enter main string")
sub=input("Enetrsub string")
flag =False
pos= -1
n= len(s)
while True:
    pos =s.find(sub.pos+1,n)
    if pos == -1:
        break
    print("Found at position",pos)
    flag= True
if flag == False:
    print("Not found")