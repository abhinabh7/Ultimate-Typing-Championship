arn ="abhinab...duela/hello wordl"
print(arn.split("/")[0])

str1 = "heloo"
str2 = "world"
result = str1 +" "+ str2
print(result)

name = "abhinabh"
print(name.upper())

text = "Python is awesome"
length = len(text)
print("Length of the string is ", length)
print("lower cass is ", text.lower())
print("Upper case ", text.upper())

new_text = text.replace("awesome", "great")
print(new_text)

words = text.split()
print("Words:", words)

text2 = "   some space around       "
stripped_text2 = text2.strip()
print("Stripped text:",    stripped_text2)

text3 = "Python is awesome"
substring = "is"
if substring in text3:
    print(substring,"found in the text")