# break -> stop loop
# continue -> skip one iteration
def print_nums():
    for num in range(1,10):
        if num == 0:
            break

        print(num)
    print("execution continues")

print_nums()

def skip_even():
    for num in range(1,10):
        if num % 2==0:
            continue

        print(num)
    print("execution continues")

if __name__=="__main__":
    skip_even()

# task 1:find the first negative value
numbers = [3,5,7,-1,9,-3]

def first_negative(numbers):
    for i in numbers:
        if i<0:
         break
    print(i)

if __name__=="__main__":
    print(first_negative([3,5,7,-1,9,-3]))

#clue:membership operator(in)
def process_until_duplicate(fruits):
    fruit_set=set()
    for fruit in fruits:
        if(fruit in fruit_set):
            print("duplicate found,processing stopped.")
            break
        fruit_set.add(fruit)
        print(f"processed {fruit}")
    print("Operation done ✅")


# if __name__=="__main__":
process_until_duplicate(["apple","banana","carrot","apple","date","banana"])



# task 3:

def censor_bot(messages,banned_words):
    for message in messages:
        banned_words_found=False
        
            
messages=[
    "hello everyone",
    "this is a bad example!",
    "lets keep our chat clean",
    "oops another bad content!",
    "have a nice day!"
]

banned_words=["bad","oops"]

censor_bot(messages,banned_words)

# expected output
#approved message:hello everyone!
#approved message:lets keep our chat clean!
#approved message:have a nice day