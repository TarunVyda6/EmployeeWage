import unittest

from employeewage.EmployeeExceptions import *
from employeewage.EmployeeWage import EmployeeWage
from employeewage.ReadingJsonFile import ReadingJsonFile

json_file_url = './JsonFiles/CompaniesList.json'
wrong_file_extension = './JsonFiles/CompaniesList.txt'
invalid_data_url = './JsonFiles/Company.json'
invalid_file_url = 'CompaniesList.json'


class MyTestCase(unittest.TestCase):

    def test_given_companies_details_should_return_least_paid_company(self):
        employee_wage = EmployeeWage()
        companies_list = ReadingJsonFile.read_json_file(json_file_url)
        companies_wage = employee_wage.get_employee_wage_sort_by_least_paid(companies_list)
        self.assertEqual('TCS', list(companies_wage.keys())[0])

    def test_given_companies_details_should_return_highest_paid_company(self):
        employee_wage = EmployeeWage()
        companies_list = ReadingJsonFile.read_json_file(json_file_url)
        companies_wage = employee_wage.get_employee_wage_sort_by_highest_paid(companies_list)
        self.assertEqual('Google', list(companies_wage.keys())[0])

    def test_given_wrong_file_type_should_throw_wrong_file_type_exception(self):
        self.assertRaises(WrongFileTypeException, ReadingJsonFile.read_json_file, wrong_file_extension)

    def test_given_missing_file_data_should_throw_invalid_file_data_exception(self):
        self.assertRaises(InvalidFileDataException, ReadingJsonFile.read_json_file, invalid_data_url)

    def test_given_wrong_file_url_should_throw_file_not_found_exception(self):
        self.assertRaises(FileNotFoundException, ReadingJsonFile.read_json_file, invalid_file_url)


if __name__ == '__main__':
    unittest.main()
