books=[
    {
        "title":"infinite jest",
        "rating":4.5,
        "genre":"fiction"
    },
    {
        "title":"the catcher inn the rye",
        "rating":3.9,
        "genre":"fiction"
    },
    {
        "title":"sapiens",
        "rating":4.9,
        "genre":"history"
    },
    {
        "title":"a brief history of time",
        "rating":4.8,
        "genre":"science"
    },
    {
        "title":"clean code",
        "rating":4.7,
        "genre":"technology"
    },
]

# task 1:highly rated books|4.7 or more
for book in books:
    if book["rating"] >= 4.7:
        print(book)
