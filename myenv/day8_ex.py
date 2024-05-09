# getting value from user
name =input ( "enter") 
print("hello "+ name)

# task -> farenhite to celsius
# formula -> (F-32)*5/9

f = input("enter temperature")
print(type(f))
c=(float(f)-32)*5/9
print(c,type(c))
print("The equivalent of " + f + "°F" + " is " + str(c) + "°C")
print(f"the equivalent of {f}°F is{c}°C")
# {} - interpolation/substitution
# task 2:find the age of the person given the birth year 2000

birth_year = int(input("enter birth year"))
print(f"your age is {2024-birth_year}")

# task 3: print area of the circle 
#given the radius of circle

  #radius = float(input("enter the radius"))
#area= 3.14*radius*radius
  #print(f"the area of circle is {3.14*radius*radius}")

#task 4:build a loader
# input: 70
#output: [======= ] 70%
#input: 23
#output: [==      ] 23%

  #nice= (9*8)>(100/2)
#condition with also expression


#ternary operator
  #g2='cool' if 5>7 else 'super'

  #print(g2)
