import random

print("Welcome to Employee Wage Computation")
"constant variables"
WAGE_PER_HOUR = 20
FULL_TIME_HOURS = 8
PART_TIME_HOURS = 4
DAYS_FOR_MONTH = 20
HOURS_FOR_MONTH = 100
current_working_hours = 0
current_working_days = 0
total_employee_wage = 0


def is_absent():
    """
executes when employee is absent
    :return: day hour as 0 when employee is absent
    """
    return 0


def is_full_time():
    """
executes when employee type is full time
    :return: day hours as 8
    """
    return FULL_TIME_HOURS


def is_part_time():
    """
executes when employee type is part time
    :return: day hours as 4
    """
    return PART_TIME_HOURS


def wage_calculation():
    """
function for calculating the daily wage of an employee
    :return: day hours and daily employee wage
    """
    employee_status = {0: is_absent, 1: is_full_time, 2: is_part_time}
    attendance_check = random.randint(0, 2)
    day_hour = employee_status.get(attendance_check)()
    daily_employee_wage = WAGE_PER_HOUR * day_hour
    return day_hour, daily_employee_wage


"""
loop gets executed till current working days reach 20 or total working hours reach 100
"""
while current_working_days <= DAYS_FOR_MONTH and current_working_hours <= HOURS_FOR_MONTH:
    day_hour, daily_employee_wage = wage_calculation()
    total_employee_wage = total_employee_wage + daily_employee_wage
    current_working_hours = current_working_hours + day_hour
    current_working_days = current_working_days + 1

"""
prints the total employee wage for that month
"""
print(total_employee_wage)
