from src.functions import filter_vacancies, get_top_vacancies
from src.head_hunter_api import HeadHunterAPI
from src.json_saver import JSONSaver
from src.vacancy import Vacancy

# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = HeadHunterAPI()

# Функция для взаимодействия с пользователем
def user_interaction():
    vacancies_list = []
    print("""Доступные функции:
    1. Найти вакансии по названию
    2. Получить топ N вакансий по зарплате
    3. Получить вакансии с ключевым словом в описании
    """)
    while True:
        work = int(input("Введите действие: "))
        if work == 1:
            search_query = input("Введите поисковый запрос: ")
            hh_vacancies_json = hh_api.get_vacancies(search_query)
            for i in range(len(hh_vacancies_json)):
                vacancy = Vacancy(hh_vacancies_json[i]["name"], hh_vacancies_json[i]["url"], hh_vacancies_json[i]["salary_from"], hh_vacancies_json[i]["salary_to"], hh_vacancies_json[i]["description"])
                vacancies_list.append(vacancy)
            ans = input('Хотите записать данные в файл? Y/N: ')
            if ans.upper() == 'Y':
                file_name = input('Введите название файла для добавления в него вакансий: ') + '.json'
                vacancies_list_json = []
                for vacancy in vacancies_list:
                    deta = {}
                    deta["name"] = vacancy.name
                    deta["url"] = vacancy.url
                    deta["salary_from"] = vacancy.salary_from
                    deta["salary_to"] = vacancy.salary_to
                    deta["description"] = vacancy.description
                    vacancies_list_json.append(deta)
                json_saver = JSONSaver(file_name)
                for i in range(len(vacancies_list_json)):
                    json_saver.add_vacancy(vacancies_list_json[i])
            ans = input('Хотите остановить программу? Y/N: ')
            if ans.upper() == 'Y':
                break
        elif work == 2:
            if vacancies_list:
                top_n = int(input("Введите количество вакансий для вывода в топ N: "))
                top_vacancies = get_top_vacancies(vacancies_list, top_n)
                ans = input('Хотите записать данные в файл? Y/N: ')
                if ans.upper() == 'Y':
                    file_name = input('Введите название файла для добавления в него вакансий: ') + '.json'
                    vacancies_list_json = []
                    for vacancy in top_vacancies:
                        deta = {}
                        deta["name"] = vacancy.name
                        deta["url"] = vacancy.url
                        deta["salary_from"] = vacancy.salary_from
                        deta["salary_to"] = vacancy.salary_to
                        deta["description"] = vacancy.description
                        vacancies_list_json.append(deta)
                    json_saver = JSONSaver(file_name)
                    for i in range(len(vacancies_list_json)):
                        json_saver.add_vacancy(vacancies_list_json[i])
                if ans.upper() == 'Y':
                    break
            else:
                print('Сначала введите номер 1, для поиска вакансий')
        elif work == 3:
            if vacancies_list:
                filter_word = input("Введите ключевое слово для фильтрации вакансий: ")
                filtered_vacancies = filter_vacancies(vacancies_list, filter_word)
                ans = input('Хотите записать данные в файл? Y/N: ')
                if ans.upper() == 'Y':
                    file_name = input('Введите название файла для добавления в него вакансий: ') + '.json'
                    vacancies_list_json = []
                    for vacancy in filtered_vacancies:
                        deta = {}
                        deta["name"] = vacancy.name
                        deta["url"] = vacancy.url
                        deta["salary_from"] = vacancy.salary_from
                        deta["salary_to"] = vacancy.salary_to
                        deta["description"] = vacancy.description
                        vacancies_list_json.append(deta)
                    json_saver = JSONSaver(file_name)
                    for i in range(len(vacancies_list_json)):
                        json_saver.add_vacancy(vacancies_list_json[i])
                ans = input('Хотите остановить программу? Y/N: ')
                if ans.upper() == 'Y':
                    break
            else:
                print('Сначала введите номер 1, для поиска вакансий')




if __name__ == "__main__":
    user_interaction()