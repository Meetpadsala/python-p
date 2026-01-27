#Regular Expressions (re module)
import re

# text = "My number is 9876665"
# result = re.search(r"\d+", text)

# print(result.group())



#re.sub
# text = "My number is 98765"
# new = re.sub(r"\d+","AAA", text)

# print(new)



#re.search
# text = "Hello Meet, welcome to Python."
# pattern = "Meet"

# result = re.search(pattern,text)

# if result:
#     print("Found pattern")
# else:
#     print("Pattern not found")





#re.findall
# text = " have 2 cats and 3 dogs."
# pattern = r"\d"

# result = re.findall(pattern,text)

# print(result)




#re.match
# text = "Hello Meet"
# pattern = "Hello"

# result = re.match(pattern,text)
# if result:
#     print("Match at start!")


#re.split()
text = "apple,banana,orange"
pattern = ","

result = re.split(pattern, text)
print(result)



