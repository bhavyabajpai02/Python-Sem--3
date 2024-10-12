# Two numbers are input through the keyboard into two locations C & D. WAP to ineterchange the content of C & D.
C= int (input ("Enter the first number: "))
D= int (input ("Enter the second number: "))
print("Numbers before interchanging: ",C,D)
temp = C
C=D
D=temp
print("Numbers after interchanging: ",C,D)