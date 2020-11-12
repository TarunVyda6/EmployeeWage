import random

print("Welcome to Employee Wage Computation")

IS_ABSENT = 0
IS_PRESENT = 1
WAGE_PER_HOUR = 20

full_day_hour = 0
attendance_check = random.randint(0, 1)
if attendance_check == IS_PRESENT:
    full_day_hour = 8

elif attendance_check == IS_ABSENT:
    pass

employee_wage = WAGE_PER_HOUR * full_day_hour
print("employee wage is : ", employee_wage)
