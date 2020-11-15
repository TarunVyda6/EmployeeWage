
class CompanyDetails:
    def __init__(self, company_name, wage_per_hour, days_for_month, hours_for_month):
        self.company_name = company_name
        self.wage_per_hour = wage_per_hour
        self.days_for_month = days_for_month
        self.hours_for_month = hours_for_month

    def get_company_name(self):
        return self.company_name

    def get_wage(self):
        return self.wage_per_hour

    def get_days_for_month(self):
        return self.days_for_month

    def get_hours_for_month(self):
        return self.hours_for_month
