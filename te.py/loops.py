# repeat a set of steps - loops

# while vs for


# DRY-dont repeat yourself
countdown = 1


# print(countdown)
# countdown = countdown+1
# print(countdown)
# countdown = countdown+1
# print(countdown)
# countdown = countdown+1
# print(countdown)
# countdown = countdown+1
# print(countdown)

# while (condition):

# while countdown < 6:
#     print(countdown)
#     countdown = countdown + 1

# # task1: build pattern
# no_of_stars = 5

# # ✨
# # ✨✨
# # ✨✨✨
# # ✨✨✨✨
# # ✨✨✨✨✨

# curr_star = 1
# while curr_star < no_of_stars:
#     print("✨" * curr_star)
#     curr_star = curr_star + 1


# range starts at 0
countdown = 1

# for countdown in range(6):
#     print(countdown) # 0-5
#range(<start>,<end>,<skip>)
for countdown in range(1,6,2):
    print(countdown)
