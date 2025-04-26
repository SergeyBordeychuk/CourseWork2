import pytest

from src.Vacancy import Vacancy


@pytest.fixture
def Python_Developer() -> Vacancy:
    return Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет... Python")

@pytest.fixture
def Java_Developer() -> Vacancy:
    return Vacancy("Java Developer", "<https://hh.ru/vacancy/123456>", "80 000-150 000 руб.", "Требования: опыт работы от 1 года... Java")