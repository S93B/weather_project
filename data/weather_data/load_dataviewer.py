import pandas as pd

#voor bekijken dataviewer
df_live_weer = pd.read_csv(r'C:\Python homedirectory\weather_project\data\weather_data\weather_data_liveweer.csv')
df_uur_weer = pd.read_csv(r'C:\Python homedirectory\weather_project\data\weather_data\weather_data_uur_verw.csv')
df_wk_weer = pd.read_csv(r'C:\Python homedirectory\weather_project\data\weather_data\weather_data_wk_verw.csv')
df_wk_weer.info()

df_wk_weer['dag'] = pd.to_datetime(df_wk_weer['dag'])
df_wk_weer.set_index('dag', inplace=True)

#timestamp niet unique per rij, per specifiek uur dezelfde
print(df_uur_weer['timestamp'].unique())

#Merge drie bestanden voor poging import
# df_live_weer['key'] = 1
# df_uur_weer['key'] = 1
# df_wk_weer['key'] = 1

df_merge = pd.merge(df_live_weer, df_uur_weer,  how='outer')
df_merge = pd.merge(df_merge, df_wk_weer, how='outer')
print(df_merge.columns)
print(df_merge.info())
df_merge.to_csv(r'C:\Python homedirectory\weather_project\data\weather_data\weather_data_merge.csv')