from src.Functions import filter_vacancies


def test_sort_vacancies(Python_Developer, Java_Developer):
    assert filter_vacancies([Python_Developer, Java_Developer], "Python") == [("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет... Python")]