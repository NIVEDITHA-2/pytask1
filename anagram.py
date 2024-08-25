string1=input("Enter the string:")
string2=input("Enter the string:")
if len(string1)!=len(string2):
    print("string is not anagram")
else:
 if sorted(string1)==sorted(string2):
     print("string is anagram")