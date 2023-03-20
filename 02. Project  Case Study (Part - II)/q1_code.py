import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

y=pd.read_csv("startup_funding.csv")
x=y.copy()

x['CityLocation'].replace('Delhi','New Delhi',inplace=True)
x['CityLocation'].replace('bangalore','Bangalore',inplace=True)
x['CityLocation'].dropna(inplace=True)

def name(cityname):
    return cityname.split('/')[0].strip()

x['CityLocation']=x['CityLocation'].apply(name)

ans = x[(x.CityLocation == 'Bangalore') | (x.CityLocation == 'Mumbai') |
        (x.CityLocation == 'New Delhi') |(x.CityLocation == 'Gurgaon')
       | (x.CityLocation == 'Noida') ].CityLocation.value_counts()

startups=ans.values
cities=ans.index

plt.bar(cities,startups,width= 0.6,color = 'green')
plt.title("CITIES WITH MOST NUMBER OF STARTUPS")
plt.xlabel("CITIES")
plt.ylabel("FUNDING  RECEIVED")
plt.grid()
plt.show()

for i in range(5):
    print(cities[i], startups[i])
print("The location at which the most number of funding is done is " , cities[0])
            

