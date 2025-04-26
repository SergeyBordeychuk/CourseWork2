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
        self.salary = salary
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
        range = salary_range.split(' - ')
        filter_list = []
        for vacancies in list_vacancies:
            range_vacancies_bot = vacancies['salary']['from']
            range_vacancies_top = vacancies['salary']['to']
            if (range_vacancies_top < range[1]) and (range_vacancies_bot > range[0]):
                filter_list.append(vacancies)
        return filter_list

