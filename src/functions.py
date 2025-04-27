def filter_vacancies(list_vacancies, filter_words):
    """
    Функция для фильтрации вакансий по ключевому слову
    """
    filter_list = []
    for vacancies in list_vacancies:
        if filter_words in vacancies.description:
            filter_list.append(vacancies)
    return filter_list

def get_top_vacancies(list_vacancies, top_n):
    """
    Метод для получения топ n вакансий по зарплате
    """
    top_vacancies = sorted(list_vacancies, key=lambda salary: list_vacancies["salary"]["from"])[:(top_n-1)]
    return top_vacancies
