import requests
import pandas as pd

res = []
response = requests.get('https://find-a-location.decodedigital.co/fal-location-json').json()
data = response['features']

for i in data:
    res.append(i)


df = pd.json_normalize(res)
df = df[['properties.name','properties.street','properties.city','properties.state','properties.zip','properties.phone']]
df["address"] = df[['properties.street', 'properties.city','properties.state','properties.zip']].agg('-'.join, axis=1)
df.drop(['properties.street','properties.city','properties.state','properties.zip'], axis=1, inplace=True)
df.rename(columns={'properties.name': 'Name', 'address': 'Address','properties.phone':'Phone'}, inplace=True)
df = df[['Name', 'Address', 'Phone']]



# saving the data 
df.to_csv('stlukeshealth.csv', index = False, header = True)