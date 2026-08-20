# **Google Sheets Time Sheet Manager**

## About
This project was made to update our timesheets with a click of the button.

It has a python backend with a html basic UI. I really had fun creating this. 

I hope you enjoy.

## Install Packages 
`pip install -r requirements.txt`

## Google Account Setup

### Enable the Required APIs

    In your Google Cloud project:

    Go to APIs & Services → Library

    Search for Google Sheets API and click Enable.

    Search for Google Drive API and click Enable.

    The Google Drive API is required so the service account can access the Google Sheet.


### Create a Service Account
    Go to APIs & Services → Credentials

    Select Create Credentials

    Choose Service Account

    Give the service account a name and finish creating it.

    You can manage your credentials here:

### Create a JSON Key
    After creating the service account:

    Open the service account.

    Go to the Keys tab.

    Select Add Key → Create new key.

    Choose JSON.

    Click Create to download the JSON file.

## Example Env
`FILE_NAME=example.json`

`WORKSHEET_NAME=GOOGLE_WORKSHEET_NAME`

`SHEET_NAME=GOOGLE_SHEET_NAME`
