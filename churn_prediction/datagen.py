from mimesis import Address, Finance, Datetime, Person
from mimesis.locales import Locale
from mimesis.enums import Gender

import random, math, string
import pycountry
import phonenumbers
from geopy.geocoders import Nominatim
import numpy as np
import pandas as pd
import secrets

person = Person()
 

def random_code(a,b):
    char = string.ascii_letters.upper()
    num = string.digits
    return (''.join(random.choice(char) for _ in range(a)) + ''.join(random.choice(num) for _ in range(b)) )

def get_phone(country_name):
    try:
        country = pycountry.countries.lookup(country_name)
        sign = country.alpha_2
        country_code = phonenumbers.country_code_for_region(sign)
        if country_code!=+0:
            return f"+{country_code}"+ str(random.randint(6, 9)) + (''.join([str(random.randint(0, 9)) for _ in range(9)]))
        else:
            return str(random.randint(6, 9)) + (''.join([str(random.randint(0, 9)) for _ in range(9)]))

    except LookupError:
        return str(random.randint(6, 9)) + (''.join([str(random.randint(0, 9)) for _ in range(9)]))

# add_dict = {
#     "India": ['New Delhi', 'Bangalore', 'Kolkata', 'Mumbai', 'Indore', 'Patna','Pune', 'Agra','Varanasi', 'Jaipur','Lucknow', 'Bhopal'],
#     "USA" : ["New York City", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Fargo", "Boise","Billings", "Topeka", "Dover", "Burlington", "Cheyenne", "Juneau", "Augusta", "Santa Fe", "Pierre", "Concord"],
#     "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide", "Hobart", "Darwin", "Canberra", "Gold Coast", "Newcastle"],
#     "Argentina": ["Buenos Aires", "Cordoba", "Rosario", "Mendoza", "La Plata", "Mar del Plata", "San Miguel de Tucumán", "Salta", "Santa Fe", "Resistencia"],
#     "Brazil": ["Sao Paulo", "Rio de Janeiro", "Brasilia", "Salvador", "Fortaleza", "Belo Horizonte", "Manaus", "Curitiba", "Recife", "Porto Alegre"],
#     "Japan": ["Tokyo", "Yokohama", "Osaka", "Nagoya", "Sapporo", "Kyoto", "Kawasaki", "Hiroshima"],
#     "Germany": ["Berlin", "Hamburg", "Munich", "Cologne", "Frankfurt", "Stuttgart", "Düsseldorf", "Dortmund", "Leipzig"],
#     "South Korea": ["Seoul", "Busan", "Incheon", "Daegu", "Daejeon", "Suwon", "Ulsan", "Changwon", "Seongnam"]
# }


# metro = ['New Delhi', 'Bangalore', 'Kolkata', 'Mumbai',"New York City", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego","Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide","Buenos Aires", "Cordoba", "Rosario", "Mendoza", "La Plata","Sao Paulo", "Rio de Janeiro", "Brasilia", "Salvador", "Fortaleza","Tokyo", "Yokohama", "Osaka", "Nagoya", "Sapporo","Berlin", "Hamburg", "Munich", "Cologne", "Frankfurt","Seoul", "Busan", "Incheon", "Daegu", "Daejeon"]

# non_metro = ["Fargo", "Boise","Billings", "Topeka", "Dover", "Burlington", "Cheyenne", "Juneau", "Augusta", "Santa Fe",
#                "Pierre", "Concord",'Indore', 'Patna','Pune', 'Agra','Varanasi', 'Jaipur','Lucknow', 'Bhopal',"Hobart", "Darwin", "Canberra", "Gold Coast", "Newcastle","Mar del Plata", "San Miguel de Tucumán", "Salta", "Santa Fe", "Resistencia","Belo Horizonte", "Manaus", "Curitiba", "Recife", "Porto Alegre", "Kyoto", "Kawasaki", "Hiroshima","Stuttgart", "Düsseldorf", "Dortmund", "Leipzig", "Suwon", "Ulsan", "Changwon", "Seongnam"]

# country_list=["India","USA","Australia","Argentina","Brazil","Japan","Germany","South Korea"]

# for city and country column

city_df = pd.read_csv('worldcities.csv')
city_df = city_df.loc[:,["city","country"]]
lstc = ['New Delhi','Delhi', 'Bangalore','Chennai','Kolkata', 'Mumbai', 'Indore', 'Patna','Pune', 'Agra','Varanasi', 'Jaipur','Lucknow', 'Bhopal']

# adding cities
for i in range(10000):
    print(61)
    city = np.random.choice(lstc)
    row = {'city':city,'country':'India'}
    city_df = pd.concat([city_df,pd.DataFrame([row])],ignore_index = True)
    
city_df = city_df.sample(frac=1).reset_index(drop=True)

# Making spell error

df_city = city_df.sample(6000)
df_country = city_df.sample(9421)

def random_typo(city_name):
    typo_type = random.choice(['replace', 'insert', 'delete'])
    if typo_type == 'replace':
        if not city_name:
            return city_name
        # Choose a random position
        pos = random.randint(0, len(city_name) - 1)
        # Choose a random character
        random_char = random.choice(string.ascii_letters)
        # Introduce the typo
        return city_name[:pos] + random_char + city_name[pos+1:]
    elif typo_type == 'insert':
        if not city_name:
            return city_name
        pos = random.randint(0, len(city_name))
        random_char = random.choice(string.ascii_letters)
        return city_name[:pos] + random_char + city_name[pos:]
    elif typo_type == 'delete':
        if len(city_name) <= 1:
            return city_name
        pos = random.randint(0, len(city_name) - 1)
        return city_name[:pos] + city_name[pos+1:]

df_city['city'] = df_city['city'].apply(random_typo)
df_country['country'] = df_country['country'].apply(random_typo)

# wrong spell data insertion
city_df = pd.concat([city_df,df_city,df_country],ignore_index=True)
city_df = city_df.sample(frac=1).reset_index(drop=True)


add=Address()  # country and city
fin=Finance() # bank, company, com_type, price
date=Datetime()  # date(start=2000, end=2024), day_of_week(abbr=False) ,date.formatted_time()
person = Person()  # birthdate(min_year, max_year), email(domains=None, unique=False), gender(), nationality(gender=None)
 # phone_number(mask='', placeholder='#')[source]
# person.email(['outlook.com','gmail.com','yahoo.com'])

# =====================================================================================================================

data=[]
for i in range(10000):
    print(115)
    # country=np.random.choice(country_list)
    city_index = np.random.choice(range(58968))
    city,country = city_df.loc[city_index,["city","country"]]
    data.append({
        "Customer ID" : random_code(2,6),
        "Name": person.name(),
        "Age" : random.randint(11,70),
        "Date of Birth": person.birthdate(1960, 2012),
        "Email": person.email(),
        "Income Status": random.choice(['>=50k', '<50k', 'unemployed','<50k','>=50k']),
        "Mobile No": str(get_phone(country)),
        "Country": country,
        "Mobile Active": random.choice([0, 1]),
        "Email Active": secrets.choice([0,1]),
        # "City": np.random.choice(add_dict[country]),
        "City": city,
        
    })

platform_data = pd.DataFrame(data)

# Email ids are not unique lets make them unique before over sampling 
# hence droping the rows with duplicate email values

platform_data = platform_data.drop_duplicates(subset=['Email'])

# .sample gets any of the n datapoints 
platform_data = pd.concat([platform_data]*32, ignore_index=True).sample(200000)
platform_data = platform_data.reset_index(drop=True)

# platform_data

# ========================================================================================================================
products = [random_code(4,4) for i in range(4517)]
data=[]
for i in range(200000):
    print(150)
    data.append({
        # "Transaction_Amount": np.random.choice([None,fin.price(1,100),fin.price(100,1000),fin.price(1000,100000)]),
        "Product Code": [np.random.choice(products) for i in range(random.randint(0,11))]
        
    })

product_df = pd.DataFrame(data)

def generate_transaction_amount(income_status):
    if income_status == '>=50k':
        return random.uniform(100, 5000)
    elif income_status == '<50k':
        return random.uniform(0, 1000)
    elif income_status == 'unemployed':
        return random.uniform(0, 5000)
    else:
        return 0

product_df = product_df.reset_index(drop=True)
product_df['Transaction_Amount'] = platform_data['Income Status'].apply(generate_transaction_amount)
# product_df


# ===========================================================================================================================
import datetime

data=[]
action = ['Login','Signup','Purchase','Home Page Visit','Save for later','Shared product', 'Add to cart','order cancel','Other']
for i in range(200000):
    data.append({
        "Action" : np.random.choice(action,size=random.randint(1,4),replace=False),
        "Time Spent": date.formatted_time(),
        "Date" : datetime.date.today() - datetime.timedelta(days=random.randint(1,165)),
        
    })

action_df = pd.DataFrame(data)
action_df = action_df.reset_index(drop=True)
# action_df

platform_df = pd.concat([platform_data,action_df,product_df], axis=1)
platform_df = platform_df.reset_index(drop=True)

# ================================================================================================================================================

# Adding noise to sythetic data

df=platform_df

for i in df.columns:
    percentage=(np.random.choice(range(10,60)))/1000
    num_none_values = int(len(df) * percentage)
    indices = np.random.choice(df.index, num_none_values, replace=False)
    df.loc[indices, i] = None

# Adding anomalies to data

# Calculate the mean and standard deviation of the 'transaction' column
mean = df['Transaction_Amount'].mean()
std = df['Transaction_Amount'].std()

# Define the percentage of anomalies
anomaly_percentage = 0.05

# Calculate the number of anomalies based on the DataFrame size
num_anomalies = int(len(df) * anomaly_percentage)

# Generate random indices for the anomalies
anomaly_indices = np.random.choice(df.index, size=num_anomalies, replace=False)

# Create anomalies by modifying the 'transaction' values at the selected indices
df.loc[anomaly_indices, 'Transaction_Amount'] = df.loc[anomaly_indices, 'Transaction_Amount'] + (std * np.random.randint(1, 11, size=num_anomalies))

# The anomalies will be added to the original values, creating outliers

df.to_csv('dirty_data.csv',index=False)








