import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

# Shit to hook up to the Google drive and Google sheet with creds file from google

scope =["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Flight_Deals").sheet1


class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.scope = scope
        self.creds = creds
        self.client = client
        self.client = sheet
        self.destination_data = {}

    def get_records(self):
        data = sheet.get_all_records()
        return data

    def get_row(self, row_num):
       row = sheet.row_values(row_num)
       return row

    def get_col(self, col_num):
        col = sheet.col_values(col_num)
        return col


    def update_iata_code(self,row,col, code):

        return sheet.update_cell(row, col, code)


    def get_cell(self,row,col):
        cell = sheet.cell(row, col).value
        return cell

    def insert(self):
        row = ["I'm","inserting","a","row","into","a,","Spreadsheet","with","Python"]
        index = 13
        sheet.insert_row(row, index)
