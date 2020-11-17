import unittest
from employeewage.EmployeeWage import EmployeeWage
from employeewage.ReadingJsonFile import ReadingJsonFile


class MyTestCase(unittest.TestCase):
    def test_given_companies_details_should_return_least_paid_company(self):
        employee_wage = EmployeeWage()
        companies_list = ReadingJsonFile.read_json_file('CompaniesList.json')
        companies_wage = employee_wage.get_employee_wage_sort_by_least_paid(companies_list)
        self.assertEqual('TCS', list(companies_wage.keys())[0])

    def test_given_companies_details_should_return_highest_paid_company(self):
        employee_wage = EmployeeWage()
        companies_list = ReadingJsonFile.read_json_file('CompaniesList.json')
        companies_wage = employee_wage.get_employee_wage_sort_by_highest_paid(companies_list)
        self.assertEqual('Google', list(companies_wage.keys())[0])


if __name__ == '__main__':
    unittest.main()
