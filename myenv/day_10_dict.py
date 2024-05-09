employees = [
    {"name": "Sneha", "experience": 2},
    {"name": "Manju"},
    {"name": "Sai Subash", "experience": 4},
    {"name": "Manasa"},
]
 
 
# Task: After 1 experience

#update_employee=[]

#for employee in employees:
    #experience = employee.get("experience",0)+1
    #update_employee.append({"name":employee["name"],"experience":experience})
#print(update_employee)
 

for employee in employees:
    employee["experience"]=employee.get("experience",0)+1
print(employees)
        
   
# Output
[
    {"name": "Sneha", "experience": 3},
    {"name": "Manju",  "experience": 1},
    {"name": "Sai Subash", "experience": 5},
    {"name": "Manasa", "experience": 1},
]


# Task 2
#  Senior 5 or more, Mid-Level 3 to 5, Junior < 3

for employee in employees:
    employee["experience"]=employee.get("experience",0)+1
    if employee["experience"]>=5:
        employee["status"]="senior"
    elif 3<=employee["experience"]>5:
        employee["status"]="mid level"
    else:
        employee["status"]="junior"
print(employees)


# Output
[
    {"name": "Sneha", "experience": 3, "status": "Mid-Level"},
    {"name": "Manju", "experience": 1, "status": "Junior"},
    {"name": "Sai Subash", "experience": 5, "status": "Senior"},
    {"name": "Manasa", "experience": 1, "status": "Junior"},
]



