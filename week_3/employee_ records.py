#employee records
#Date: 27/02/2024
#Name : Jane

name =input("Enter employee's name")
age =input("Enter employee's age")
salary =float(input("Enter employee's salary"))

if salary <= 100000:
    salary =salary * 0.3+ salary
    print (salary)
if salary > 100000 and salary <= 150000 :
    salary =salary * 0.15+ salary
    print (salary)   
if salary > 150000:
    salary =salary * 0.05+ salary
    print (salary)   
