import json
from abc import ABC, abstractmethod

import requests


class Api_Vacancies(ABC):
    api:str

class FileWorker(ABC):

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass


class JSONSaver(FileWorker):

    def add_vacancy(self, vacancy):
        with open('vacancies.json', 'a') as file:
            json.dump(vacancy, file)

    def delete_vacancy(self, vacancy):
        pass

class HeadHunterAPI(Api_Vacancies):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def get_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
        return self.vacancies


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
        vacancies_list = []
        for json_string in json_data:
            vacancies_list.append(json.loads(json_string))
        return vacancies_list

    def filter_vacancies(self, list_vacancies, filter_words):
        filter_list = []
        for vacancies in list_vacancies:
            if filter_words in vacancies["description"]:
                filter_list.append(vacancies)
        return filter_list

    def get_vacancies_by_salary(self, list_vacancies, salary_range):
        range = salary_range.split(' - ')
        filter_list = []
        for vacancies in list_vacancies:
            range_vacancies = vacancies['salary']['from']
            if (range[0] < range_vacancies) and (range[1] > range_vacancies):
                filter_list.append(vacancies)
        return filter_list

    def sort_vacancies(self):
        sort_list = sorted(self)
        return sort_list

    def get_top_vacancies(self,top_n):
        pass
