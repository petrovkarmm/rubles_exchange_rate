import requests


class CBRApi:
    def __init__(self) -> None:
        url = "https://www.cbr-xml-daily.ru/daily_json.js"

        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            usd_rub = data["Valute"]["USD"]["Value"]
            eur_rub = data["Valute"]["EUR"]["Value"]

            self.__result = {"USD_RUB": usd_rub, "EUR_RUB": eur_rub}

        else:
            self.__result = False

    @property
    def get_result(self) -> dict or bool:
        return self.__result