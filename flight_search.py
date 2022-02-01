import requests
from datetime import datetime, timedelta
from data_manager import DataManager

data_m = DataManager()

today = datetime.now().strftime("%d/%m/%Y")
tomorrow = (datetime.today() + timedelta(days=1)).strftime("%d/%m/%Y")     #timedelta para calcular datas futuras
seven_days_from_now = (datetime.today() + timedelta(days=7)).strftime("%d/%m/%Y")
six_months_from_now = (datetime.today() + timedelta(days=183)).strftime("%d/%m/%Y")
seven_months_from_now = (datetime.today() + timedelta(days=213)).strftime("%d/%m/%Y")



TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_ENDPOINT2 = "https://tequila-api.kiwi.com/v2"
TEQUILA_API_KEY = "Btf25KulKf92CSkduwtUTMe3iUGQORPP"


class FlightSearch:
    """Gets city IATA Code info from TEQUILA API"""

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city", "limit": 1}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def search_flight(self, fly_to, max_price ):
        """Searches for flights according to params: https://tequila.kiwi.com/portal/docs/tequila_api/search_api"""

        location_endpoint = f"{TEQUILA_ENDPOINT2}/search"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            #required params:
            "fly_from": "BSB",
            f"fly_to": f"{fly_to}",   #formatar corretamente from e to.
            "date_from": tomorrow,
            "date_to": six_months_from_now,
            #not required params:
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 0,   #returns cheapest flights for destination
            "adults": 1,
            "price_to": max_price,
            "curr": "BRL",
            "limit": 1,   #limits number of results
        }
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        response.raise_for_status()
        flight_data = response.json()

        if flight_data["data"] == []:     # se nao achar voo para uma localidade, nao dar erro
            print(f"No flights to {fly_to} from BSB for less than {max_price}BRL")
            return None
        else:
            print(f"\nFLIGHT FOUND!  {fly_to} from BSB for less than {max_price}BRL")
            print("Link at:")
            print(flight_data["data"][0]["deep_link"])
            return flight_data
















