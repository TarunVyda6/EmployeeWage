import random

print("Welcome to Employee Wage Computation")

WAGE_PER_HOUR = 20
FULL_TIME_HOURS = 8
PART_TIME_HOURS = 4
DAYS_FOR_MONTH = 20
day_hour = 0


def is_absent():
    return day_hour


def is_full_time():
    return FULL_TIME_HOURS


def is_part_time():
    return PART_TIME_HOURS


employee_status = {0: is_absent, 1: is_full_time, 2: is_part_time}
attendance_check = random.randint(0, 2)
day_hour = employee_status.get(attendance_check)()

daily_employee_wage = WAGE_PER_HOUR * day_hour
employee_wage = daily_employee_wage * DAYS_FOR_MONTH
print("employee wage is : ", employee_wage)
