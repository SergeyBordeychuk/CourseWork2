from abc import ABC, abstractmethod


class Api_Vacancies(ABC):
    """
    Абстрактный класс для работы с api
    """

    @abstractmethod
    def get_vacancies(self, keyword):
        """
        Метод для получения вакансий в формате json строки
        """
        pass

class FileWorker(ABC):
    """
    Класс для работы с файлами
    """

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancy(self, name_criteria, vacancy_criteria):
        pass