# library_list = [
#     {
#         "title": "Python Programming",
#         "author": "Eric Matthes",
#         "year": 2019,
#         "available": True,
#     },
#     {
#         "title": "Automate the Boring Stuff with Python",
#         "author": "Al Sweigart",
#         "year": 2020,
#         "available": True,
#     },
#     {
#         "title": "Learning Python I",
#         "author": "Mark Lutz",
#         "year": 2013,
#         "available": False,
#     },
#     {
#         "title": "Fluent Python",
#         "author": "Luciano Ramalho",
#         "year": 2015,
#         "available": True,
#     },
#     {
#         "title": "Adavance Python",
#         "author": "Mark Lutz",
#         "year": 2015,
#         "available": False,
#     },
# ]


# book = {"title": "Fluent Python II", "author": "Alex", "year": 2016, "available": True}


# # Task 1
# # Add Book Function: Write a function add_book(library, new_book)


# def add_book(library, new_book):
#     library.append(new_book)


# add_book(library_list, book)
# print(library_list)


# # Task 2
# # Search Books by Author Function: Write a function search_by_author(library, author_name)

# # v1
# def search_by_author(library, author_name):
#     author_books = []
#     for book in library:
#         if book["author"] == author_name:
#             author_books.append(book)
#     return author_books


# # v2 - Pythonic way
# # def search_by_author(library, author_name):
# #     return [book for book in library if book["author"] == author_name]


# print(search_by_author(library_list, "Mark Lutz"))

# # Task 3
# # Check Out Book Function: Write a function check_out_book(library, title) that marks a book as not available if it exists and is available in the library.
# # 1. Book available
# # 2. Book unavailable
# # 3. Book doesn't exists

# def check_out_book(library,title):
#     avail_book=[]
#     for book in library:
#         if book["available"]=="true":
#             return (print("book available"))
#         elif book["available"]=="false":
#             return (print("book not available"))
#         else:
#             return (print("book doesnt exist"))
        
# check_out_book(library_list,"advance python")


# movies = [
#     {"title": "Inception", "ratings": [5, 4, 5, 4, 5]},
#     {"title": "Interstellar", "ratings": [5, 5, 4, 5, 4]},
#     {"title": "Dunkirk", "ratings": [4, 4, 4, 3, 4]},
#     {"title": "The Dark Knight", "ratings": [5, 5, 5, 5, 5]},
#     {"title": "Memento", "ratings": [4, 5, 4, 5, 4]},
# ]

# # Function
# # Task 1
# # add_avg_ratings

# # from pprint import pprint
# # def add_avg_ratings(movies):
# #     for movie in movies:
# #         movie["avg_rating"]=sum(movie["ratings"])/len(movie["ratings"])
# #     return(movies)


# # pprint(add_avg_ratings(movies))

# # # Task 2 - break it into 2 functions

# # def calc_avg_ratings(movie):
# #     return sum(movie["ratings"])/len(movie["ratings"])

# # def avg_ratings(movies):
# #     for movie in movies:
# #         movie["avg_ratings"]=calc_avg_ratings(movie)
# #     return(movies)

# # pprint(avg_ratings(movies))


# print(max(5,6,10,7,80,60,70,9))


# arbitary arguements
def own_max(*nums):
    curr_max=nums[0]
    for n in nums:
        if n > curr_max:
            curr_max = n
    return curr_max
    
    

print(own_max(5,6,10))
print(own_max(5,6,10,7,80,60))



