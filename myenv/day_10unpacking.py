#a=10
#b=10
#c=10

#multiple variable assignment

a = b = c = 10
print(a,b,c)

swathi,sowmi,samar="chocolate","choco chip","strawberry" #tuple

print(swathi)
print(sowmi)
print(samar)

#t1,t2,t3=[100,200,300,400]
#print(t1,t2,t3)  #error

t1,t2,t3,_=[100,200,300,400]
print(t1,t2,t3) # _ -> skip

# ? skip 200 
t1,_,t2,t3=[100,200,300,400]
print(t1,t2,t3)

# * -> unpacking operator
t1,t2,*t3=[100,200,300,400,60,40,30]
print(t1,t2,t3)

# * -> unpacking operator(still a list)
t1,t2,*t3=(100,200,300,400,60,40,30)
print(t1,t2,t3)

t1, t2,*_,t3 = (100, 200, 300, 400, 60, 40, 30)
print(t1, t2,t3)

marks1=[70,80,60]
marks2=[*marks1]#copy - 1.slice 2. .copy()
marks2=[*marks1,75,68]#add more values
print(marks2)



#task 1
coordinates = [(5,4),(1,1),(6,10),(9,10)]

#for each point find the distance from origin
#task 1.1- for loop
distances = []
for cord in coordinates:
    x = cord[0]
    y = cord[1]
    d= (x**2+y**2)**0.5
    distances.append(d)
print(distances)


#task 1.2 - for loop + unpacking

distances = []
for cord in coordinates:
    x,y = cord
    d= (x**2+y**2)**0.5
    distances.append(d)
print(distances)

distances = []
for x,y in coordinates:
    d= (x**2+y**2)**0.5
    distances.append(d)
print(distances)




# task 1.3 - unpacking + list comprehension 
distances = [round((x**2+y**2)**0.5,2)for x,y in coordinates]
print(distances)

person = {
    "name": "Lionel Messi",
    "age": 36,
    "address": {
        "city": "rosario",
        "country": "Argentina",
    },
    #"stats": {"goals":300,"assists":500},
    "sport": "football",
}
print(person["address"]["city"])
#access nested dictionary

#print(person["stats"]) keyerror : 'stats'

#safer way:access value
print(person.get("stats")) #none
print(person.get("name")) #lionel messi

#.get--default value--person.get(key,default value)
print(person.get("stats", {}).get("goals")) #or
print(person.get("stats",{"goals":0}).get("goals"))
