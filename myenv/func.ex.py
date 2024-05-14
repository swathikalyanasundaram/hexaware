library_list = [
    {
        "title": "Python Programming",
        "author": "Eric Matthes",
        "year": 2019,
        "available": True,
    },
    {
        "title": "Automate the Boring Stuff with Python",
        "author": "Al Sweigart",
        "year": 2020,
        "available": True,
    },
    {
        "title": "Learning Python I",
        "author": "Mark Lutz",
        "year": 2013,
        "available": False,
    },
    {
        "title": "Fluent Python",
        "author": "Luciano Ramalho",
        "year": 2015,
        "available": True,
    },
    {
        "title": "Adavance Python",
        "author": "Mark Lutz",
        "year": 2015,
        "available": False,
    },
]

book = {"title": "Fluent Python II", "author": "Alex", "year": 2016, "available": True}

# # Task 1
# # Add Book Function: Write a function add_book(library, new_book)

# def add_book (library,new_book):
#     pass
# add_book(library_list,book)
# print(library_list)

# task 2
# search book by author function: write a func search_by_author(library,author_name)

# def search_by_author(library,author_name):
#     author_books=[]
#     for book in library:
#         if book["author"]==author_name:
#             author_books.append(book)
#     return(author_books)

#py way

def search_by_author(library,author_name):
    return[book for book in library if book["author"]==author_name]

print(search_by_author(library_list,"mark lutz"))
