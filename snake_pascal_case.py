txt="gods_own_country"
print("The original string:",txt)
#convert snake to pascal
x=txt.replace("_"," ").title().replace("","")#title() to convert lower case to upper case
print("The string after converting snake to pascal case is:",x)# replace underscore with the space