# after the 🔑
# message =  "⚠️📱🔐🔑secret_code👍"
# code = "secret_code👍"

# key_index = message.find("🔑")
# #print(message[key_index+1:])  #: slicing operator
# output = message[key_index + 1:].upper()
# # #output = #your code

# if (output==code): # type: ignore
#     print("hacker")
# else:
#     print("try again")

# # task 2: remove junk[*,(] to find the secret
# message="⚠️📱🔐🔑******secret_code👍((("
# code = "secret_code👍"

# key_index = message.find("🔑")
# print(message[key_index+1:])  #: slicing operator
# output = message[key_index + 1:].upper().strip('*').strip('(').lower()  
# # #output = #your code

# if (output==code): # type: ignore
#     print("hacker")
# else:
#     print(output)


# journey = "--->to the stars--->"
# clean = journey.strip("->")  # to the stars
# launch = journey.lstrip("-")  # >to the stars--->
# return_home = journey.rstrip("-")  # --->to the stars>
# print(clean, "|", launch, "|", return_home)
# Output: to the stars | >to the stars---> | --->to the stars>


a = " hi hello bye"
b=a.replace("hello","welcome")
print(b)