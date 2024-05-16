
import json


bank_data = """

[

    {

        "id": 1,

        "name": "John Doe",

        "email": "johndoe@example.com",

        "isActive": true,

        "balance": 150.75

    },

    {

        "id": 2,

        "name": "Jane Smith",

        "email": "janesmith@example.com",

        "isActive": false,

        "balance": 500.50

    },

    {

        "id": 3,

        "name": "Emily Jones",

        "email": "emilyjones@example.com",

        "isActive": true,

        "balance": 0.00

    }

]

"""
 
data = json.loads(bank_data)
 
for user in data:

    if user["isActive"]:

        user["balance"] *= 1.10  
 
updated_bank_data = json.dumps(data, indent=4)
 
print(updated_bank_data)

