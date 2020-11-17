from abc import ABC, abstractmethod


class IEmployeeWage(ABC):
    @abstractmethod
    def compute_employee_wage(self, companies):
        pass

    @abstractmethod
    def wage_calculation(self, wage_per_hour):
        pass

    @abstractmethod
    def get_employee_wage_sort_by_least_paid(self, companies):
        pass

    @abstractmethod
    def get_employee_wage_sort_by_highest_paid(self, companies):
        pass
