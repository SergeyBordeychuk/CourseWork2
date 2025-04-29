class Vacancy():
    """
    Класс для работы с вакансиями
    """
    name:str
    url:str
    salary_from:int
    salary_to:int
    description:str


    def __init__(self, name='', url='', salary_from=0, salary_to=0, description=''):
        self.url = url
        self.__validation_salary(salary_from, salary_to)
        self.name = name
        self.description = description

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

    def __validation_salary(self, salary_from, salary_to):
        if salary_to and salary_from:
            self.salary_from = salary_from
            self.salary_to = salary_to
        else:
            self.salary_from = 0
            self.salary_to = 0

    def __lt__(self, other):
        return self.salary_from < other.salary_from