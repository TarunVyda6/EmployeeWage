import random

print("Welcome to Employee Wage Computation")

IS_ABSENT = 0
IS_PRESENT = 1

attendance_check = random.randint(0, 1)
if attendance_check == IS_PRESENT:
    print("Employee is present")
elif attendance_check == IS_ABSENT:
    print("Employee is absent")
