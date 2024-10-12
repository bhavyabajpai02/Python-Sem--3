#WAP to check in a patient name Adi is 30 years old and is  a new patient

patient_name = input(" Enter patient's name: ")
age = 30
existance = input(" Enter if the patient is already admitted : ")
if (existance == "yes"):
    print (" No "+ patient_name + " is an old patient")
else:
    print("Yes "+patient_name+ " is a new patient")
