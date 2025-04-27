import json


class Vacancy():
    """
    Класс для работы с вакансиями
    """
    name:str
    url:str
    salary:str
    description:str


    def __init__(self, name, url, salary, description):
        self.url = url
        self.__validation_salary(salary)
        self.name = name
        self.description = description

    def cast_to_object_list(self, json_data):
        """
        Метод для получения вакансий из формата json строки в формат список объектов
        """
        self.json_data = json_data
        vacancies_list = []
        for json_string in self.json_data:
            vacancies_list.append(json.loads(json_string))
        return vacancies_list

    def get_vacancies_by_salary(self, list_vacancies, salary_range):
        """
        Метод для сравнения вакансий по зарплате
        """
        range = salary_range.split('-')
        range[0] = int(range[0])
        range[1] = int(range[1][:-4])
        filter_list = []
        for vacancies in list_vacancies:
            range_vacancies_top = vacancies.salary_from
            range_vacancies_bot = vacancies.salary_to
            if (range_vacancies_top <= range[1]) and (range_vacancies_bot >= range[0]):
                filter_list.append(vacancies)
        return filter_list

    def __validation_salary(self, salary):
        if salary:
            salary_new = salary.split('-')
            if len(salary) == 20:
                salary_new[0] = int(salary_new[0][:3] + salary_new[0][4:])
                salary_new[1] = int(salary_new[1][:3] + salary_new[1][4:8])
            elif len(salary) == 19:
                salary_new[0] = int(salary_new[0][:2] + salary_new[0][3:])
                salary_new[1] = int(salary_new[1][:3] + salary_new[1][4:8])
            salary = {}
            salary["from"] = salary_new[1]
            salary["to"] = salary_new[0]
            self.salary_from = salary["from"] if salary["from"] else 0
            self.salary_to = salary["to"] if salary["to"] else 0
        else:
            self.salary_from = 0
            self.salary_to = 0

    def __lt__(self, other):
        return self.salary_from < other.salary_from