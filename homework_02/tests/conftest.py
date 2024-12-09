import pytest


# from helpers.utils import add_homework_path
#
# add_homework_path(__file__)

@pytest.fixture(scope="session", autouse=True)
def get_book_for_tests() -> dict:
    return {
        "131": {
            "Name": "Андрианов Александр Даниилович",
            "Phone": "+7(993)785-20-82",
            "Company": "Мультиметры",
            "Comment": "harass situ Aubrey"
        },
        "132": {
            "Name": "Касьянова Александра Александровна",
            "Phone": "+7(495)758-82-47",
            "Company": "Стремглав",
            "Comment": "notify caveat scuff"
        },
        "133": {
            "Name": "Лукина Елизавета Никитична",
            "Phone": "+7(940)465-14-13",
            "Company": "Кожухи",
            "Comment": "planetaria lymph Jonathan"
        }
    }
