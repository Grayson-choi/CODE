# https://fredaccount.stlouisfed.org/ 사이트에서 크롤링 후 excel에 데이터 저장
['DGS1MO',
 'DGS1MO.1',
 'DGS3MO',
 'DGS3MO.1',
 'DGS6MO',
 'DGS6MO.1',
 'DGS1',
 'DGS1.1',
 'DGS2',
 'DGS2.1',
 'DGS3',
 'DGS3.1',
 'DGS5',
 'DGS5.1',
 'DGS7',
 'DGS7.1',
 'DGS10',
 'DGS10.1',
 'DGS20',
 'DGS20.1',
 'DGS30',
 'DGS30.1',
 'DAAA',
 'DAAA.1',
 'DBAA',
 'DBAA.1',
 'TEDRATE',
 'TEDRATE.1',
 'BAMLH0A0HYM2',
 'BAMLH0A0HYM2.1',
 'TWEXMMTH',
 'TWEXMMTH.1',
 'SP500',
 'SP500.1',
 'WILL5000IND',
 'WILL5000IND.1',
 'FF',
 'FF.1',
 'T5YIE',
 'T5YIE.1',
 'T10YIE',
 'T10YIE.1',
 'TEDRATE.2',
 'TEDRATE.3',
 'VIXCLS',
 'VIXCLS.1',
 'PCEPI',
 'PCEPI.1',
 'M1SL',
 'M1SL.1',
 'M2SL',
 'M2SL.1',
 'INDPRO',
 'INDPRO.1',
 'ALTSALES',
 'ALTSALES.1',
 'NEWORDER',
 'NEWORDER.1',
 'HOUST',
 'HOUST.1',
 'PMSAVE',
 'PMSAVE.1',
 'PI',
 'PI.1',
 'CPIAUCSL',
 'CPIAUCSL.1',
 'CPILFESL',
 'CPILFESL.1',
 'WPSFD4131',
 'WPSFD4131.1',
 'DPRIME',
 'DPRIME.1',
 'DCOILWTICO',
 'DCOILWTICO.1',
 'UMCSENT',
 'UMCSENT.1',
 'RRSFS',
 'RRSFS.1',
 'UNRATE',
 'UNRATE.1']

# https://api.stlouisfed.org/fred/series/search?api_key=abcdefghijklmnopqrstuvwxyz123456&search_text=canada
import requests
from pprint import pprint
import pandas as pd
import openpyxl

# API 또는 웹 페이지에서 데이터를 가져옵니다.
# 이 예에서는 JSON 형식의 데이터를 사용하겠습니다.
API_KEY = "6e724faa9cebe8b2662e4e0f5f832fc3"
# response = requests.get(f"https://api.stlouisfed.org/fred/releases/dates?api_key={API_KEY}&file_type=json")
# data = response.json()



# series_list 
# series_list = []

series_id = "GNPCA"
data_url = f"https://api.stlouisfed.org/fred/series/observations? + \
series_id={series_id}&api_key={API_KEY}&file_type=json"
# "&observation_start={start}&observation_end={end}&units={units}"

series_response = requests.get(data_url)
series_data = series_response.json()
print(series_data)
