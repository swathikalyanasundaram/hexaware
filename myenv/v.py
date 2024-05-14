# arbitary position arguements

def own_max(*nums):
    curr_max= nums[0]
    for n in nums:
        if n > curr_max:
            curr_max = n
    return curr_max

print(own_max(5,6,7,8,10))
print(own_max(45,5,23,40,35))


# arbitary keyword arguements
def party(**people):
    # print(people.values())
    return ",".join(people.values())
party(p1="abi",p2="ami",p3="pooji",p4="sai")

# lambda functions


print(sum([2,3,4,5,6]))
print(max([2,3,4,5,6]))
print(min([2,3,4,5,6]))


print(max("abdca"))

