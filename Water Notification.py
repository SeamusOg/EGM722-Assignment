import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import os

DMAs = gpd.read_file("C:\EGM722-Assignment\Data\Derg Strabane DMAs.shp")
Address = gpd.read_file("C:\EGM722-Assignment\Data\Address Points.shp")
print("DMAs", DMAs.crs)
print("Address", Address.crs)

fig, ax = plt.subplots(figsize=(12, 8))
DMAs.plot(alpha=.5, ax=ax, cmap ='rainbow' , column ='CARID')
Address.plot(ax=ax)
plt.show()

Address.columns

Address = Address.rename(columns={'BUILDING00': 'BUILDING NUMBER' , 'PRIMARY_TH': 'ROAD NAME'})
Address.columns

Address_List=gpd.sjoin(Address, DMAs, how='left',op='within')

Address_List= Address_List.rename(columns={'BUILDING00': 'BUILDING NUMBER' , 'PRIMARY_TH': 'ROAD NAME'})

Address_List.columns


Address_List.drop(columns=['UPRN', 'BUILDING_N', 'SUB_BUILDI',  'LOCALITY', 'UDPRN', 'POSTTOWN', 'LOCAL_COUN', 'USRN', 'ADDRESS_ST', 'BUILDING_S',
       'CLASSIFICA', 'ORGANISATI', 'TEMP_COORD',
       'UNIQUE_BUI', 'DTM_HEIGHT', 'MI_PRINX', 'YEAR_BUILT', 'geometry',
       'index_right', 'DATASOURCE', 'STATUS', 'DMATYPE',
       'CONFIDENCE', 'RESOURCEZO', 'RESOURCE00', 'SUPPLYZONE', 'SUPPLYZO00',
       'LENGTHOFMA', 'POINTERRES', 'POINTERNON', 'VERIFIEDDA', 'NWDISTFM_A',
       'NWB2BRMFM_', 'NWB2CRMFM_', 'LDETFM_ARE', 'AUDITDATE', 'AUDITNAME'], inplace=True)

Address_List.tail(5)

Address_List.sort_values(['ROAD NAME', 'BUILDING NUMBER', 'CARID'], ascending=True, inplace=True)

Address_List.to_excel('C:\EGM722-Assignment\Water Notification.xlsx', sheet_name='sheet1', index=False)

excel_file_path = 'C:\EGM722-Assignment\Water Notification.xlsx'

df = pd.read_excel(excel_file_path)
print(df)

split_values = df['CARID'].unique()

for value in split_values:
       df1 = df[df['CARID'] == value]
       output_file_name = "CARID " + str(value) + " Address List.xlsx"
       df1.to_excel(output_file_name, index=False)

save_to_path = 'C:\EGM7222\WaterNotification'



