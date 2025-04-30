import json

from src.abstract_classes import FileWorker


class JSONSaver(FileWorker):
    """
    Класс для сохранения данных в json файл и работы с ними
    """

    def __init__(self, name_file="vacancy.json"):
        self.__name_file = name_file

    def add_vacancy(self, vacancy):
        """
        Метод для добавления вакансии в файл
        """
        with open(self.__name_file, 'w', encoding="utf-8") as file:
            json.dump(vacancy, file, ensure_ascii=False, indent=4)

    def delete_vacancy(self, vacancy):
        """
        Метод для удаления вакансии в файле
        """
        with open(self.__name_file, 'r') as file:
            vacancies = json.load(file)
        i = 0
        for vacancy_file in vacancies:
            if vacancy_file == vacancy:
                vacancies.pop(i)
            i += 1
        with open(self.__name_file, 'a') as file:
            json.dump(vacancies, file)


    def get_vacancy(self, name_criteria, vacancy_criteria):
        """
        Метод для получения вакансии по критерию
        """
        with open(self.__name_file, 'r') as file:
            vacancies = json.load(file)
        for vacancy_file in vacancies:
            if vacancy_file[f"{name_criteria}"] == vacancy_criteria:
                return vacancy_file
