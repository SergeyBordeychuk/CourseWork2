def test_vacancy(python_developer):
    assert python_developer.name == "Python Developer"
    assert python_developer.url == "<https://hh.ru/vacancy/123456>"
    assert python_developer.salary_from == 150000
    assert python_developer.salary_to == 100000
    assert python_developer.description == "Требования: опыт работы от 3 лет... Python"

def test_get_vacancies_by_salary(python_developer, java_developer):
    assert len(python_developer.get_vacancies_by_salary([java_developer, python_developer], "100000-150000 руб.")) == 1

