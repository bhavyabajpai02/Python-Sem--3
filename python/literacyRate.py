# In town the % of men is 52. The % of total literacy is 48. If total % of literate men is 35 of the total population ,WAP to find the total number of  illitrate men and women if the total population of the town is 80,000
total_Men_inper=52
total_Literacy_inper=48
total_Literate_meninper=35
total_population=80000

total_men = total_population*total_Men_inper/100
total_women = total_population-(total_men)

total_Literate_womeninper=total_Literacy_inper -total_Literate_meninper
total_Iliterate_men = (total_men) - (total_population * total_Literate_meninper/100)
total_Iliterate_women = (total_women) - (total_population * total_Literate_womeninper/100)
print("Total ileterate men and women are",total_Iliterate_men,total_Iliterate_women)

