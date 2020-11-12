import random

print("Welcome to Employee Wage Computation")

IS_ABSENT = 0
IS_PRESENT = 1
WAGE_PER_HOUR = 20

day_hour = 0
attendance_check = random.randint(0, 1)
if attendance_check == IS_PRESENT:
    day_hour = 8

elif attendance_check == IS_ABSENT:
    day_hour = 4

employee_wage = WAGE_PER_HOUR * day_hour
print("employee wage is : ", employee_wage)
