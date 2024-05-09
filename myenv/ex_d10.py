t1=[80,90]
t2=[50,60]

#t3=[80,90,50,60]

t3=[*t1,*t2]
print(t3)

#unpacking -> ** dictionary

movie ={
    "name":"john wick",
    "year": 2014
}

mv1={**movie,"actor":"kea"}
mv3={"actor":"kea","year":2015,**movie}
print(mv3)