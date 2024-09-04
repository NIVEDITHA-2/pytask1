string1=input("Enter the string:")
#print(sorted(string1))
string2=input("Enter the string:")
#print(sorted(string2))
if len(string1)==len(string2):

    if sorted(string1) == sorted(string2):


        print("string is anagram")
    else:
        print("string is not anagram")

