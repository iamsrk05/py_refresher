employee = {
    "name": "Alex",
    "role": "Data Analyst",
    "salary": 65000
}

# print(employee.get("department","Not Assigned"))
employee.update({
    "salary": 70000,
    # "department": "Analytics"
})
employee["Department"] = "Analytics"

print(employee)