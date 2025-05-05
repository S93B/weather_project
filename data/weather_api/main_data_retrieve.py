import json
import pandas as pd
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

steden = ('Rotterdam', 'Amsterdam', 'Utrecht', 'Den Haag', 'Maastricht',
        'Vlissingen', 'Leeuwarden', 'Groningen')

DATA_WEER_TYPE = ('wk_verw', 'uur_verw', 'liveweer')

class WeatherCall:
    """Call API voor data, input api key en stad naam of list met indexnr"""

    def __init__(self, API_KEY, stad, data_set_type):
        self.stad = stad
        self.API_KEY = API_KEY
        self.base_url = (
            f"https://weerlive.nl/api/weerlive_api_v2.php?"
            f"key={self.API_KEY}"
            f"&locatie={self.stad}"
        )
        self.data_set_type = data_set_type
        self.save_path = (
            fr'C:\Python homedirectory\weather_project\data\weather_data\weather_data_{self.data_set_type}.csv'
        )

    def call_api(self):
        """Call API and returns data """
        response = requests.get(self.base_url)
        response.raise_for_status()
        print(response.json())
        #get and save response data
        data = response.json()
        return data

    def transform_data(self, data, path ):
        df = pd.DataFrame(data[self.data_set_type])
        df['stad'] = self.stad
        df['timestamp_api'] = pd.Timestamp.now().strftime('%d-%m-%y %H:%M')


        #check if CSV already exist to determine whethe to write the header
        if not os.path.exists(path):
            header=True
        else:
            header=False

        df.to_csv(path,mode="a", index=False, header=header)
        return print(f"{self.data_set_type} successvol naar {path} .csv")

#Loop through each chosen city and the different data types/choices
for data_type in DATA_WEER_TYPE:
    for stad in steden:
        weather = WeatherCall(API_KEY, stad, data_type)
        api_data = weather.call_api()
        weather.transform_data(api_data,weather.save_path)

# Hierna transform runnen