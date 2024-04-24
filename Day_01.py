print("Hello World")
#Concatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)


#len
text = "Python is awesome"
length = len(text)
print("Length of the string:", length)

text = "Python is awesome"
new_text = text.replace("awesome", "great")
print("Modified text:", new_text)

# String Strip
text = "   Some spaces around   "
stripped_text = text.strip()
print(f"text:{text}")
print("Stripped text:", stripped_text)


text = "Python is awesome"
substring = "is"
if substring in text:
    print(substring, "found in the text")