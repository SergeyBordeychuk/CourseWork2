def filter_vacancies(list_vacancies, filter_words):
    """
    Функция для фильтрации вакансий по ключевому слову
    """
    filter_list = []
    for vacancies in list_vacancies:
        if vacancies.description and filter_words in vacancies.description:
            filter_list.append(vacancies)
    return filter_list

def get_top_vacancies(list_vacancies, top_n):
    """
    Метод для получения топ n вакансий по зарплате
    """
    return sorted(list_vacancies)[:top_n]
