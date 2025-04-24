# Создание экземпляра класса для работы с API сайтов с вакансиями
from src.classes import HeadHunterAPI, Vacancy, JSONSaver

hh_api = HeadHunterAPI()

# Получение вакансий с hh.ru в формате JSON
hh_vacancies = hh_api.get_vacancies("Python")

# Преобразование набора данных из JSON в список объектов
vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

# Пример работы конструктора класса с одной вакансией
vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")

# Сохранение информации о вакансиях в файл
json_saver = JSONSaver()
json_saver.add_vacancy(vacancy)
json_saver.delete_vacancy(vacancy)

# Функция для взаимодействия с пользователем
def user_interaction():
    platforms = ["HeadHunter"]
    # print("""Доступные функции:
    # 1. Найти вакансии по названию
    # 2. Получить топ N вакансий по зарплате
    # 3. Получить вакансии с ключевым словом в описании
    # """)
    # work = int(input("Введите действие: "))
    #
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_word = input("Введите ключевое слово для фильтрации вакансий: ")
    salary_range = input("Введите диапазон зарплат: ") # Пример: 100000 - 150000

    filtered_vacancies = vacancies_list.filter_vacancies(filter_word)

    ranged_vacancies = filtered_vacancies.get_vacancies_by_salary(salary_range)

    sorted_vacancies = ranged_vacancies.sort_vacancies()
    top_vacancies = sorted_vacancies.get_top_vacancies(top_n)
    print(top_vacancies)


if __name__ == "__main__":
    user_interaction()