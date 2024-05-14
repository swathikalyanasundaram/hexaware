# a=8
# b=10

# print("the sum is:",a+b)


# a1=60
# b1=70

# print("the sum is:",a1+b1)

# a2=600
# b2=70

# print("the sum is:",a2+b2)

# #function
# # 1. Declaration/ definition
# # 2. function name
# # 3. parameters - 2
# # 4.function body

# def add(a,b):
#     return round(a+b,2)

# # function call
# print("the sum is:" ,add(80.987899,10.76765))

# default values
def driving_test(name,age,car="dezire"):
    if age >=18:
        return f"{name} eligible for driving.you will be tested in {car}"
    else:
        return "try again after few years 👶🍼"
    
print(driving_test("swathi",13))


# types of argument

# 1. position arguement
# 2. keyword argument

print(driving_test(   ))