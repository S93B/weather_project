import pandas as pd
# TRANSFORM NA DATA VERZAMELING

DATA_WEER_TYPE = ('wk_verw', 'uur_verw', 'liveweer')

class Transform:
    def __init__(self, data_type):
        self.path = fr'C:\Python homedirectory\weather_project\data\weather_data\weather_data_{data_type}.csv'
        self.df = pd.read_csv(self.path)

drop_list_live = [
    'timestamp', 'time','lv', 'ldmmhg', 'dauwp', 'verw', 'alarm', 'lkop', 'ltekst',
    'wrschklr', 'wrsch_g', 'wrsch_gts', 'wrsch_gc','plaats']

for data_type in DATA_WEER_TYPE:
    clss = Transform(data_type)
    if data_type == 'liveweer':
        clss.df = clss.df.drop(columns=drop_list_live)
    clss.df.info()
    clss.df.to_csv(clss.path, index=False)
