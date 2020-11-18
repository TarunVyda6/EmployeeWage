import json
from employeewage.CompanyDetails import CompanyDetails
from employeewage.EmployeeExceptions import *


class ReadingJsonFile:
    @staticmethod
    def read_json_file(url):
        """
        reads the json file and checks for exceptions and then convert it into list of CompanyDetails Type
        :param url: takes url of the file as input
        :return: list of companies and their details present in json file of CompanyDetails type
        """
        if not url.endswith('.json'):
            raise WrongFileTypeException("wrong file type")

        try:
            my_json_file = open(url, 'r')
            json_data = my_json_file.read()
        except FileNotFoundError:
            raise FileNotFoundException("invalid file path")
        try:
            my_json_file.close()
            json_object = json.loads(json_data)
        except ValueError:
            raise InvalidFileDataException("invalid file data")

        json_list = json_object["Companies"]
        companies_list = []
        for i in range(len(json_list)):
            companies_list.append(
                CompanyDetails(json_list[i].get("name"), json_list[i].get("wage"), json_list[i].get("days"),
                               json_list[i].get("hours")))
        return companies_list
