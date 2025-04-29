import pytest

from src.head_hunter_api import HeadHunterAPI
from src.json_saver import JSONSaver
from src.vacancy import Vacancy


@pytest.fixture
def python_developer() -> Vacancy:
    return Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", 150000, 100000, "Требования: опыт работы от 3 лет... Python")

@pytest.fixture
def java_developer() -> Vacancy:
    return Vacancy("Java Developer", "<https://hh.ru/vacancy/123456>", 150000, 80000, "Требования: опыт работы от 1 года... Java")

@pytest.fixture
def head_hunter_api() -> HeadHunterAPI:
    return HeadHunterAPI()

@pytest.fixture
def json_saver() -> JSONSaver:
    return JSONSaver("vacancies.json")