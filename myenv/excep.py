#try
#except
#else
#finally

# def math_divide(n1, n2):
#     try:
#         result = n1 / n2
#         return result

#     # Generic message
#     except ZeroDivisionError:
#         return "Oops. 🤭 An Error happened"
#     else:
#         return "div was succ"
#     finally:
#         print("done")

from datetime import datetime

print(datetime.now().weekday())
print(datetime.now().day)

def calculate_age():
    birth_year = input("please provide your birth year")
    age=2024 - int(birth_year)
    print(f"your age is {age}")

    