
import pandas as pd
import numpy as np

df = pd.read_csv('state_data_csv.csv')

loc_dict = {'Alabama': ['AL', 32.806671, -86.79113],
 'Alaska': ['AK', 61.370716, -152.404419],
 'Arizona': ['AZ', 33.729759, -111.431221],
 'Arkansas': ['AR', 34.969704, -92.373123],
 'California': ['CA', 36.116203, -119.681564],
 'Colorado': ['CO', 39.059811, -105.311104],
 'Connecticut': ['CT', 41.597782, -72.755371],
 'Delaware': ['DE', 39.318523, -75.507141],
 'District of Columbia': ['DC', 38.897438, -77.026817],
 'Florida': ['FL', 27.766279, -81.686783],
 'Georgia': ['GA', 33.040619, -83.643074],
 'Hawaii': ['HI', 21.094318, -157.498337],
 'Idaho': ['ID', 44.240459, -114.478828],
 'Illinois': ['IL', 40.349457, -88.986137],
 'Indiana': ['IN', 39.849426, -86.258278],
 'Iowa': ['IA', 42.011539, -93.210526],
 'Kansas': ['KS', 38.5266, -96.726486],
 'Kentucky': ['KY', 37.66814, -84.670067],
 'Louisiana': ['LA', 31.169546, -91.867805],
 'Maine': ['ME', 44.693947, -69.381927],
 'Maryland': ['MD', 39.063946, -76.802101],
 'Massachusetts': ['MA', 42.230171, -71.530106],
 'Michigan': ['MI', 43.326618, -84.536095],
 'Minnesota': ['MN', 45.694454, -93.900192],
 'Mississippi': ['MS', 32.741646, -89.678696],
 'Missouri': ['MO', 38.456085, -92.288368],
 'Montana': ['MT', 46.921925, -110.454353],
 'Nebraska': ['NE', 41.12537, -98.268082],
 'Nevada': ['NV', 38.313515, -117.055374],
 'New Hampshire': ['NH', 43.452492, -71.563896],
 'New Jersey': ['NJ', 40.298904, -74.521011],
 'New Mexico': ['NM', 34.840515, -106.248482],
 'New York': ['NY', 42.165726, -74.948051],
 'North Carolina': ['NC', 35.630066, -79.806419],
 'North Dakota': ['ND', 47.528912, -99.784012],
 'Ohio': ['OH', 40.388783, -82.764915],
 'Oklahoma': ['OK', 35.565342, -96.928917],
 'Oregon': ['OR', 44.572021, -122.070938],
 'Pennsylvania': ['PA', 40.590752, -77.209755],
 'Rhode Island': ['RI', 41.680893, -71.51178],
 'South Carolina': ['SC', 33.856892, -80.945007],
 'South Dakota': ['SD', 44.299782, -99.438828],
 'Tennessee': ['TN', 35.747845, -86.692345],
 'Texas': ['TX', 31.054487, -97.563461],
 'Utah': ['UT', 40.150032, -111.862434],
 'Vermont': ['VT', 44.045876, -72.710686],
 'Virginia': ['VA', 37.769337, -78.169968],
 'Washington': ['WA', 47.400902, -121.490494],
 'West Virginia': ['WV', 38.491226, -80.954453],
 'Wisconsin': ['WI', 44.268543, -89.616508],
 'Wyoming': ['WY', 42.755966, -107.30249]}

loc_code = {}
for i in loc_dict.keys():
    loc_code[i] = loc_dict[i][0]

state_list = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware',
                  'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana',
                 'Iowa','Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
                  'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico',
                  'New York', 'North Carolina', 'North Dakota', 'Ohio','Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island',
                  'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington',
                  'West Virginia', 'Wisconsin', 'Wyoming']

code_list = []
for i in loc_code:
    #print(loc_code.get(i))
    code_list.append(loc_code.get(i))

df_state = df[df['State'].isin(state_list)].copy()


month_dict = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
              7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct',11: 'Nov',12: 'Dec'}

df_state['month_year'] = df_state['Month'].map(month_dict) + ' '+ df_state['Year'].astype(str)
df_state['code'] = df_state['State'].map(loc_code)


for i in ['Civilian non-institutional population', 'Civilian labor force', 'Employed', 'Unemployed']:
    print(i)
    df_state[i] = df_state[i].str.replace(',', '').astype(int)

df_state['Unemployment rate'] = df_state['Unemployed']/df_state['Civilian labor force']

df_state['text'] = df_state['State'].astype(str) + '<br>' + \
	'Unemployment rate ' + round(df_state['Unemployment rate'], 2).astype(str) + '<br>' + \
    'Unemployed ' + df_state['Unemployed'].astype(str) + '<br>' + \
	'Employed ' + df_state['Employed'].astype(str) + '<br>' + \
	'Civilian labor force ' + df_state['Civilian labor force'].astype(str) + '<br>' + \
    'Civilian non-institutional population ' + df_state['Civilian non-institutional population'].astype(str)

print(df_state)
