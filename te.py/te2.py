scrambled_message="world the save to time no is there"

#list or array method
#output
#there is no time to save the world
i=scrambled_message.split()[::-1]
print(" ".join(i))


#replacing values
avatar=["fire","water","earth","air"]
avatar[1:3]=["diamond","platinum","gold"]
print(avatar)