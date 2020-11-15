import random


class EmployeeWageComputation:
    FULL_TIME_HOURS = 8
    PART_TIME_HOURS = 4

    def __init__(self, company_name, wage_per_hour, days_for_month, hours_for_month):
        self.company_name = company_name
        self.wage_per_hour = wage_per_hour
        self.days_for_month = days_for_month
        self.hours_for_month = hours_for_month

    def compute_employee_wage(self):
        """
        loop gets executed till current working days reach 20 or total working hours reach 100
        """
        current_working_hours = 0
        current_working_days = 0
        total_employee_wage = 0
        while current_working_days <= self.days_for_month and current_working_hours <= self.hours_for_month:
            day_hour, daily_employee_wage = self.wage_calculation()
            total_employee_wage = total_employee_wage + daily_employee_wage
            current_working_hours = current_working_hours + day_hour
            current_working_days = current_working_days + 1
        """
        prints the total employee wage of a company for that month
        """
        print("total employee wage of {} is : {}".format(self.company_name, total_employee_wage))

    employee_status = {0: 0, 1: FULL_TIME_HOURS, 2: PART_TIME_HOURS}

    def wage_calculation(self):
        """
        function for calculating the daily wage of an employee
            :return: day hours and daily employee wage
        """

        attendance_check = random.randint(0, 2)
        day_hour = self.employee_status.get(attendance_check)
        daily_employee_wage = self.wage_per_hour * day_hour
        return day_hour, daily_employee_wage


print("Welcome to Employee Wage Computation")

amazon = EmployeeWageComputation('Amazon', 20, 20, 100)
microsoft = EmployeeWageComputation('Microsoft', 30, 20, 100)
amazon.compute_employee_wage()
microsoft.compute_employee_wage()
