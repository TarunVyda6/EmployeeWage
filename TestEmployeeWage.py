import unittest

from employeewage.CompanyDetails import CompanyDetails
from employeewage.EmployeeWage import EmployeeWage


class MyTestCase(unittest.TestCase):
    def test_given_companies_details_should_return_least_paid_company(self):
        employee_wage = EmployeeWage()
        companies_list = [CompanyDetails('Amazon', 20, 20, 100), CompanyDetails('Microsoft', 30, 20, 100), CompanyDetails('Google', 10, 20, 100)]
        companies_wage = employee_wage.get_employee_wage_sort_by_least_paid(companies_list)
        self.assertEqual('Google', list(companies_wage.keys())[0])

    def test_given_companies_details_should_return_highest_paid_company(self):
        employee_wage = EmployeeWage()
        companies_list = [CompanyDetails('Amazon', 20, 20, 100), CompanyDetails('Microsoft', 30, 20, 100), CompanyDetails('Google', 10, 20, 100)]
        companies_wage = employee_wage.get_employee_wage_sort_by_highest_paid(companies_list)
        self.assertEqual('Microsoft', list(companies_wage.keys())[0])


if __name__ == '__main__':
    unittest.main()
