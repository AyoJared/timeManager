import gspread
import pandas as pd
import os 
from dotenv import load_dotenv

load_dotenv()

# Load credentials from the JSON file

gc = gspread.service_account(os.getenv("FILE_NAME"))  # Replace with your JSON file path# Open the Google Sheet by its name
sh = gc.open(os.getenv("WORKSHEET_NAME"))  # Replace with your sheet’s exact name# Select a worksheet (e.g., "Sheet1")
worksheet = sh.worksheet(os.getenv("SHEET_NAME"))  # Replace with your worksheet name# Fetch all data from the worksheet*
data = worksheet.get_all_records()

#  Convert the data into a pandas DataFrame*
df = pd.DataFrame(data)

# Display the DataFrame*
print(df)