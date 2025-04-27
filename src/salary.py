from src.vacancy import Vacancy

filter_words = 'Python'

list_vacancies = [Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет... Python"), Vacancy("Java Developer", "<https://hh.ru/vacancy/123456>", "80 000-150 000 руб.", "Требования: опыт работы от 1 года... Java")]
filter_list = []
for vacancies in list_vacancies:
    if filter_words in vacancies.description:
        filter_list.append(vacancies)
print(filter_list)