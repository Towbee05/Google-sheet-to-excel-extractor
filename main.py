import gspread
from pathlib import Path
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()

CREDENTIALS = {
    "installed": 
        {
            "client_id":os.getenv("CLIENT_ID"),
            "project_id":os.getenv("PROJECT_ID"), 
            "auth_uri":"https://accounts.google.com/o/oauth2/auth",
            "token_uri":"https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs",
            "client_secret":os.getenv("CLIENT_SECRET"),
            "redirect_uris":["http://localhost"]
        }
}

def main(spreadsheet_name: str) -> str:
    # Authenticate user 
    gc, user = gspread.oauth_from_dict(CREDENTIALS)

    # Open spreadsheet
    spreadsheet = gc.open(spreadsheet_name)

    worksheet = spreadsheet.worksheet("Sheet1")
    data =worksheet.get_all_records()
    dataframe= pd.DataFrame(data)
    
    dataframe = dataframe.set_axis(["room number", "meter above", "meter below"], axis='columns')
    dataframe = dataframe.astype(str)
    dataframe["meter above"] = dataframe["meter above"].apply(lambda x: f"0{x}")
    dataframe.to_excel("output.xlsx", index=False)

    return "hello, world"

main("high_house_meters")