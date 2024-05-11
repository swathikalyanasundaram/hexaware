price_l=[1000,1500,400]
price_l_copy=price_l
price_l1=[1000,1500,400]

price_l_copy.append(600)
price_l.append(700)
price_l1.append(800)

print (id(price_l),id(price_l1),id(price_l_copy) ) # copy by refrence same address

#copy by value
p1=[1000,1500,400]
# p2=p1.copy()
p2 = p1[:]
print(p1,p2) # different address

#copy by reference
#p2=p1
#copy by value
#p2=p1.copy()
#p3=p1[:]

#remove -> .pop(),.remove()
#add -> .append(),.insert()
#copy -> :(slice),copy

h1=[198,175,140,1777]
#h1.pop(1)
h1.remove(1777) #pop-index|remove-value
print(h1)

#repetition
clo=["gold coin"]*3
print(clo)

#split and join

#split(str-list) vs join(list - str)
shop_stock = "vanilla,lime,chocolate"
shop_list=shop_stock.split(",")

#join(list - str)
avatar=['fire','water','earth','air']
print(",".join(avatar))
print("|".join(avatar))