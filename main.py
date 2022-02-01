# -*- coding: iso-8859-1 -*-

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
import pprint

data_m = DataManager()
f_search = FlightSearch()
f_data = FlightData()
n_manager = NotificationManager()

sheet_data = data_m.get_records()

# para cada row em sheet data, se IATA code estiver vazio, busca iata code na API.
for row in sheet_data:
    if row["IATA Code"] == "":
        code = f_search.get_destination_code(row["City"])
        row_num = len(data_m.get_col(2)) +1
        data_m.update_iata_code(row_num,2, code)
        print(code)

#funcao save_data puxa funcao flight_search para cada fileira da planilha
#funcao format_data salva retorna informacoes importantes formatadas
print("Beggining search according to parameters...\n\n")
for row in sheet_data:
    data = f_search.search_flight(row["IATA Code"], row["Lowest Price"])
    flights_list = []
    try:
        flight = f_data.format_data(data)
        if flight == None:
            pass
        else:
            f_flight = flight.encode("utf-8")
            flights_list.append(f_flight)


    except KeyError:
        print("No parameter found for search")
    if flights_list == []:
            pass
    else:
        # n_manager.send_email(flights_list)   #send email if flight list is not empty
        # n_manager.send_sms(flights_list)
        pass


