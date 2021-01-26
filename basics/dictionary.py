derek_dict = {"f_name": "Derek", "l_name": "Banas","address": "123 main st"}

print("name: ",derek_dict["f_name"])

derek_dict["address"] = "214 north st"
print("address", derek_dict["address"])
print(derek_dict.values())
print(derek_dict.keys())
for k,v in derek_dict.items():
    print(k, v)
print(derek_dict.get("m_name", "Not here"))
print(derek_dict.values())
del derek_dict["l_name"]
for i in derek_dict:
    print(i)
derek_dict.clear()
for i in derek_dict:
    print(i)

# employees = []
# f_name, l_name = input("Enter Employee Name : ").split()
# employees.append({"f_name": f_name, "l_name": l_name})
# print(employees)

customer = True
customer_names = []
while True:
    is_customer = input("Enter Customer (y/n) : ")
    if is_customer.lower() == "y":
        f_name, l_name = input("Enter Customer Name : ").split()
        customer_names.append({"f_name": f_name, "l_name": l_name})
    else:
        break


for cust in customer_names:
    print(cust["f_name"], cust["l_name"])

