# for countdown in range(1,6,2):
#     print(countdown)
#range(3)|range(end)
#range(1,3)|range(start,end)


# task 3: double the stats

#player stats double

# idx = 0
# while idx < len(player_stats):
#     player_stats[idx]=player_stats[idx]*2
#     idx=idx+1
# print(player_stats)


#output
#[20,40,60]

# for idx in range(len(player_stats)):
#     powered_up.append(player_stats[idx]*2)
# print(powered_up)
# print(player_stats)


# player_stats=[10,20,30]
# powered_up=[]
# for x in player_stats:
#     powered_up.append(x*2)
# print(powered_up)
# print(player_stats)

# #list comprehension - copy of the result
# powered_up 
# # powered_up1=[for stat in player_stats]


avengers=[
    "hulk",
    "iron man",
    "black widow",
    "captain america",
    "spider man",
    "thor"
]

#output
#[4,8,11,15,10,4]
#task 4.1-for loop
# avengers_name_length=[]
# for avenger in avengers:
#     avengers_name_length.append(len(avenger))
# print(avengers_name_length)

# task 4.2 - list comprehension

# avenger_n1=[len(avenger) for avenger in avengers]
# print(avenger_n1)

# letter_count = [4,8,11,15,10,4]
# large_count=[]
# for count in letter_count:
#     if(count>10):
#         large_count.append(count)
# print(large_count)


# large_count_1=[count for count in letter_count if(count>10)]
# print(large_count_1)

#task 1-for loop

avengers=[
    "hulk",
    "iron man",
    "black widow",
    "captain america",
    "spider man",
    "thor"
]

#ouput
# ["black widow",
#  "captain america"]

#task 1-for loop

l1=[]
for avenger in avengers:
    if (len(avenger) > 10):
        l1.append(avenger)
print(l1)

# task2-list comprehension

l2=([avenger.upper() for avenger in avengers if (len(avenger) > 10)])
print(l2)
