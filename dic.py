# Get multiple values from user and print it into dictionary
optional_list = []
for i in range(5):
    Name = input("Enter the name: ")
    Age = input("Enter the age: ")
    Address = input("Enter the address: ")
    Role = input("Enter the role: ")
    emp = {}
    emp['Name'] = Name
    emp['Age'] = Age
    emp['Address'] = Address
    emp['Role'] = Role
    optional_list.append(emp)

print(optional_list)
print(type(optional_list))