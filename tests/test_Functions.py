from src.functions import filter_vacancies


def test_filter_vacancies(python_developer, java_developer):
     assert len(filter_vacancies([python_developer, java_developer], "Python")) == 1
