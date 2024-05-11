# dictionary -> hashmap -> key:value
#key should be unique

# dictionary
person={
    "name":"messi",
    "age": 36,
    "country":"argentina",
    "sport":"football",
}

print(person["name"])
print(type(person))

#update values

person["age"] += 1
print(person["age"])

#methods
print(person.keys())
print(person.values())

# loop the dict

for key in person:
    print(key,person[key])

for x,y in person.items():
    print(x,y)