#  WAP to calculate and display the interest on a loan amount (Rupees)
#  You would need 3 variables to hold 'principal',Rate_of_ineterest (%) and time in years and can use the formula 
#  Interest =(principal*Rate_of_ineterest*time)/100
#  Note :User input 
principal = int (input("Enter the principal amount :")) 
Rate_of_ineterest = int (input("Enter the Rate_of_ineterest  :"))
time = int (input ("Enter the time :"))
interest = (principal*Rate_of_ineterest*time)/100
print ("This is the following interest:",interest)