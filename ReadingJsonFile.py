import json
from employeewage.CompanyDetails import CompanyDetails


class ReadingJsonFile:
    @staticmethod
    def read_json_file(url):
        my_json_file = open(url, 'r')
        json_data = my_json_file.read()
        my_json_file.close()
        json_object = json.loads(json_data)
        json_list = json_object["Companies"]
        companies_list = []
        for i in range(len(json_list)):
            companies_list.append(
                CompanyDetails(json_list[i].get("name"), json_list[i].get("wage"), json_list[i].get("days"), json_list[i].get("hours")))

        return companies_list
