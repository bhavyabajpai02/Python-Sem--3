# WAP program that accepts an integer (n) and computes the value of n+nn+nnn
n=int (input( "Enter the integer :"))
sum=0
i=1
for i in range (1,4): 
    sum += int(str(n) * i)
print("The sum of integer is: ",sum)
