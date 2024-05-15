# String, List, Tuple, Dictonary, Sets
# Sets - Like List Mutable but only unique

# Sets
# 1. Mutable
# 2. Unique
# 3. No order (cannot access with index)

# {}
empty_dict = {}
tech_gadgets = {"Smartphone", "Laptop", "Smartwatch", "Tablet", "Tablet"}
empty_set = set()
print(type(empty_set))
print(type(tech_gadgets))

print(tech_gadgets)
# print(tech_gadgets[0]) # ❌

tech_gadgets.add("E-reader")
tech_gadgets.add("Laptop")
print(tech_gadgets)


colors = ["red", "blue", "red", "green", "pink", "blue"]

# Find all unique colors
# Using .add()

a=set()
for color in colors:
    a.add(color)
print(a)



 # List to Set

# Comprehension
# 1. List
# 2. Dictionary
# 3. Set

# print("this is cool""\nwe will do it now""\nok bye")
# #multi line string

# print("""
# hi
# hello
#     ok 
#       bye
#       """)
# followers= 1000
# print(
#     f"""
# hi this is manju 
# i have {followers} followers"""
# )

def to_upper_case(text):
    """ this helps in converting the text into uppercase"""
    return text.upper()

print(to_upper_case("manju"))
print(help(to_upper_case))