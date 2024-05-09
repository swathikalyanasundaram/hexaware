quote="dream"
#print(quote[<start>:<end>])
print(quote[1:3]) #re
print(quote[-1])
print(quote[-4:-1])
quote = "Dream is something"
print(quote[1:10:2])  # ra ss
print(quote[::-1])  # gnihtemos si maerD
print(quote[-1:-4:-1]) # gni

#task 1:
# after the 
message = "secret_code"
code="secret_code"

key_index = message.find("key")
output=message[key_index + 1 :].upper()

if output == code:
    print("you are an hacker")
else:
    print("try again")

#output = # your code

#if(ouput == code):
  #  print("you are an hacker")
#else:
 #   print("try again")

# output
# "you are an hacker"
# "try again"

#task 2: remove junk[*,(] to find the secret
#message1 = "****secret_code((("