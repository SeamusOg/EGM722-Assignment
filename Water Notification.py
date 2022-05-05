"""This section loads all the modules required for the script"""
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import os

#imports the required data from data folder and checks the CRS of each shapefile
DMAs = gpd.read_file("C:\EGM722-Assignment\Data\Derg Strabane DMAs.shp")
Address = gpd.read_file("C:\EGM722-Assignment\Data\Address Points.shp")
print("DMAs", DMAs.crs)
print("Address", Address.crs)

#displays area being investigated for a visual reference
fig, ax = plt.subplots(figsize=(12, 8))
DMAs.plot(alpha=.5, ax=ax, cmap ='rainbow' , column ='CARID')
Address.plot(ax=ax)
plt.show()

#displays columns on address list shapefile and renames columns to standardised name
Address.columns
Address = Address.rename(columns={'BUILDING00': 'BUILDING NUMBER' , 'PRIMARY_TH': 'ROAD NAME'})
Address.columns

#joins the Address List shapefile with the District Metered Area Shapefile
Address_List=gpd.sjoin(Address, DMAs, how='left',op='within')

#drops uneccesary table columns, displays excel view amd sorts final output by road and house number
Address_List.drop(columns=['UPRN', 'BUILDING_N', 'SUB_BUILDI',  'LOCALITY', 'UDPRN', 'POSTTOWN', 'LOCAL_COUN', 'USRN', 'ADDRESS_ST', 'BUILDING_S',
       'CLASSIFICA', 'ORGANISATI', 'TEMP_COORD',
       'UNIQUE_BUI', 'DTM_HEIGHT', 'MI_PRINX', 'YEAR_BUILT', 'geometry',
       'index_right', 'DATASOURCE', 'STATUS', 'DMATYPE',
       'CONFIDENCE', 'RESOURCEZO', 'RESOURCE00', 'SUPPLYZONE', 'SUPPLYZO00',
       'LENGTHOFMA', 'POINTERRES', 'POINTERNON', 'VERIFIEDDA', 'NWDISTFM_A',
       'NWB2BRMFM_', 'NWB2CRMFM_', 'LDETFM_ARE', 'AUDITDATE', 'AUDITNAME'], inplace=True)

Address_List.tail(5)

Address_List.sort_values(['ROAD NAME', 'BUILDING NUMBER', 'CARID'], ascending=True, inplace=True)

#exports complete address list to excel
Address_List.to_excel('C:\EGM722-Assignment\Water Notification.xlsx', sheet_name='sheet1', index=False)

#defines Address List path and splits each address into its corrsponding District Metered Area
excel_file_path = 'C:\EGM722-Assignment\Water Notification.xlsx'

df = pd.read_excel(excel_file_path)
print(df)

split_values = df['CARID'].unique()

for value in split_values:
       df1 = df[df['CARID'] == value]
       output_file_name = "CARID " + str(value) + " Address List.xlsx"
       df1.to_excel(output_file_name, index=False)

save_to_path = 'C:\EGM7222\WaterNotification'



