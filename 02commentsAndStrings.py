# Commenting using a single quote
"hello world"

# Commenting using a double quote
'Python'

# Commenting using triple quotes
'''Kodnest BTM 2nd Stage Bengaluru'''

# String using a single quote
Str = 'hello world'

# String using a double quote
str1 = "Hello world"

s = "python"

print(s[0])
print(s[3])
print(s[5])
print(s[-1])           # Last character
print(s[-3])           # 3rd last character


'''String slicing in Python
  
   stringname[starting index : ending index]'''

word = "python is fun"

print(word[0:6])
print(word[7:9])
print(word[10:13])

# Only using the starting index --> it will start from the 7th index until the end of the string
print(word[7:])

# Only using the ending index --> it will start from the 0 index until the 9th index of the string 
print(word[:9])

# len() function is used to find the length of the string
print(len(word))

# upper() function is used to convert the string to uppercase
print(word.upper())

# find() function will return the starting index of the specified substring
print(word.find("fun"))

# replace(find string, replacing string) --> it will first find the string, then replace it with the specified string
print(word.replace("python", "Java"))

# split() will split the string into substrings based on the delimiter 
tech = "java,python,golang"

string = tech.split(",")
print(string)

# join() will insert the delimiter between the strings
print("-".join(string))
