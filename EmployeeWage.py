import random

print("Welcome to Employee Wage Computation")

WAGE_PER_HOUR = 20

day_hour = 0

employee_attendance_type = ['is_absent', 'is_present']
attendance_check = random.choice(employee_attendance_type)

if attendance_check == employee_attendance_type[1]:
    total_employee_types = ['full_time', 'part_time']
    employee_type = random.choice(total_employee_types)

    if employee_type == total_employee_types[0]:
        day_hour = 8
    else:
        day_hour = 4

elif attendance_check == employee_attendance_type[0]:
    pass

employee_wage = WAGE_PER_HOUR * day_hour
print("employee wage is : ", employee_wage)
