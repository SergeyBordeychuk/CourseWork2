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
    new_list = []
    for i in range(len(list_vacancies)):
        a = list_vacancies[i](list_vacancies[i+1])
        if a:
            new_list.extend(list_vacancies)
    top_vacancies = sorted(new_list)[:top_n]
    return top_vacancies
