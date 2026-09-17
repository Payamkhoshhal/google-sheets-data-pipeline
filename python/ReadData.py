from googleapiclient.discovery import build
from google.oauth2 import service_account
import pandas as pd
import json
import datetime
from sqlalchemy import create_engine
import os 

def main():
    # created a gcp account and got credential for google sheet, stored keys in a json file in the same folder  
    SERVICE_ACCOUNT_FILE = 'Keys.json'
    # define the scope
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    creds  = None
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE , scopes= SCOPES)
    # assign shared spread sheet id 
    spreadsheet_id = '1jsHbDNyv92_EbIHK5sLkMcuNidiQpJUkUKQ1KAZeHj4'
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    # define the range of data in the google sheet
    result = sheet.values().get(spreadsheetId = spreadsheet_id ,range ="Calls!A2:C1861").execute()
    values = result.get('values', [])
    #create a connection to Aws rds postgres
    DATABASE_URL = os.getenv("DATABASE_URL")
    engine = create_engine(DATABASE_URL)    
    
    for i in range(len(values)):
        # in each loop a json file will be created 

        # convert start date to time stamp
        date = values[i][0].replace(',','')
        start_timestamp= str(datetime.datetime.strptime(date ,'%b %d %Y %H:%M'))
        # get the duration 
        main_duration = int(values[i][1].replace(',',''))

        # load the chanels data as json
        js = json.loads(values[i][2])
        # add the start_date and duration to the json
        for j in range(len(js)):
            js[j]['start_timestamp']=start_timestamp
            js[j]['main_duration']= str(main_duration)
            # create a id as identity
            js[j]['record_id'] = i
        # add data to a pandas data frame
        df = pd.DataFrame(js)
        #convert events and party data 
        df['events'] = list(map(lambda x: json.dumps(x), df['events']))
        df['party'] = list(map(lambda x: json.dumps(x), df['party'])) 
        # insert data to Aws rds postgres
        df.to_sql('calls', engine , if_exists='append')



if __name__ == '__main__':
    main()

   
