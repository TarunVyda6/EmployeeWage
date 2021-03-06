import random
import collections


class EmployeeWage:

    FULL_TIME_HOURS = 8
    PART_TIME_HOURS = 4
    """
    Constants
    """
    def compute_employee_wage(self, companies):
        """
        function for checking the condition of total days or total hours
        :param companies: takes all companies details as input
        :return: dictionary values of companies where key is company name and value is employee's monthly wage
        """
        salary_details = {}
        for company in companies:
            current_working_hours = 0
            current_working_days = 0
            total_employee_wage = 0

            while current_working_days <= company.get_days_for_month() and current_working_hours <= company.get_hours_for_month():
                """
                loop gets executed till current working days reach 20 or total working hours reach 100
                """
                day_hour, daily_employee_wage = self.wage_calculation(company.get_wage())
                total_employee_wage = total_employee_wage + daily_employee_wage
                current_working_hours = current_working_hours + day_hour
                current_working_days = current_working_days + 1
            salary_details[company.get_company_name()] = total_employee_wage

        return salary_details

    employee_status = {0: 0, 1: FULL_TIME_HOURS, 2: PART_TIME_HOURS}

    def wage_calculation(self, wage_per_hour):
        """
        function for calculating the daily wage of an employee
            :return: day hours and daily employee wage
        """

        attendance_check = random.randint(0, 2)
        day_hour = self.employee_status.get(attendance_check)
        daily_employee_wage = wage_per_hour * day_hour
        return day_hour, daily_employee_wage

    def get_employee_wage_sort_by_least_paid(self, companies):
        """
        function will collect all the companies name and wages as dictionary input and sort wages in ascending order
        :param companies: take all companies name and their monthly employee wages
        :return: returns the dictionary of companies and their wages in ascending order as per wages
        """
        companies_wage_list = self.compute_employee_wage(companies)
        companies_wage_list_sorted = collections.OrderedDict(sorted(companies_wage_list.items(), key=lambda x: x[1]))
        return companies_wage_list_sorted

    def get_employee_wage_sort_by_highest_paid(self, companies):
        """
        function will collect all the companies name and wages as dictionary input and sort wages in descending order
        :param companies: take all companies name and their monthly employee wages
        :return: returns the dictionary of companies and their wages in descending order as per wages
        """
        companies_wage_list = self.compute_employee_wage(companies)
        companies_wage_list_sorted = collections.OrderedDict(
            sorted(companies_wage_list.items(), key=lambda x: x[1], reverse=True))
        return companies_wage_list_sorted
