name = input("name:")
age = int(input("age:"))
job = input("job:")
salary = input("salary:")


info = """
-------------info of %s------
Name:%s
Age:%d
Job:%s
Salary:%s
"""  % (name, name, age, job, salary)
#print(info)

info2 = """
-------------info2 of {name}------
Name:{name}
Age:{age}
Job:{job}
Salary:{salary}
"""
#print(info)

info3 = """
-------------info3 of {_name}------
Name:{_name}
Age:{_age}
Job:{_job}
Salary:{_salary}
""".format(_name=name,_job=job,_age=age,_salary=salary)
print(info)
