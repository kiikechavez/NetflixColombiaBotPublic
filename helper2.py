import gspread
from gspread.exceptions import CellNotFound
from oauth2client.service_account import ServiceAccountCredentials
NETFLIX_PRUEBA_SHEET_KEY = 'YOUR_GOOGLE_SHEETS_CREDENCIALS'


#use creds to create a client to interact with Google Drive Api
scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('access-key.json', scope)
client = gspread.authorize(creds)

#Find a workbook by name and open the first sheet
#Make sure you use the right name here
sheet = client.open_by_key(NETFLIX_PRUEBA_SHEET_KEY).sheet1




list_of_hashes = sheet.get_all_records()
#print(list_of_hashes)