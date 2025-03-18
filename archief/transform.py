import pandas as pd
import json
import os
from database.utilities.functions import transform_data
from database.weather_api.api_call import STAD


PATH_LIVE = r'/data\weather_data\liveweer.csv'
PATH_VERW = r'/data\weather_data\wk_verw.csv'

data_set_type = ['wk_verw', 'uur_verw', 'liveweer']

# Open and read the JSON file
data = json.load(open(r'/data\json_data\weather_data.json'))

#Even eerste sets maken
# for i in data_set_type:
#     if not os.path.exists(f'/data/weather_data/{i}.csv'):
#         df = pd.DataFrame(data[i])
#         df.to_csv(f'C:/Python homedirectory/Weather_project/data/weather_data/{i}.csv',index=False)
#         print(f"{i} csv aangemaakt")
#     else:
#         print(f"{i} csv bestaat al")

#TODO column maken in uur en wk verwachting met plaats
for i in STAD:
    transform_data('liveweer', i, PATH_LIVE)
    transform_data('wk_verw', i, PATH_VERW)