from flight_search import FlightSearch
import json

f_search = FlightSearch()


class FlightData:

    def format_data(self,flight_data):
        try:
            from_city = flight_data["data"][0]["cityFrom"]
            to_city = flight_data["data"][0]["cityTo"]
            price = flight_data["data"][0]["price"]
            airline = flight_data["data"][0]["airlines"]
            link = flight_data["data"][0]["deep_link"]
            # out_date= flight_data["route"][0]["local_departure"].split("T")[0],
            # return_date= flight_data["route"][1]["local_departure"].split("T")[0]

            return f"{from_city} para {to_city} por {price} reais. De Companhia:{airline}.  Link:{link}"
        except TypeError:
            return None




