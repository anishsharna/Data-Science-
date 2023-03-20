import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("startup_funding.csv")
d = data.copy()
d.InvestorsName.dropna(inplace = True)

def dict(a):
    d = {}
    for i in a:
        if ',' not in i:
            d[i] = d.get(i,0) + 1
            
        else:
            c = i.strip().split(',');
            for j in c:
                d[j.strip()] = d.get(j.strip(),0)+1
    return d   
a = dict(d.InvestorsName)
dataset = pd.DataFrame(list(a.values()), list(a.keys()))
dataset = dataset.sort_values(by=[0] ,ascending = False)
investors = dataset.index[0:5]
times = dataset[0:5][0]
plt.bar(investors , times , color = 'blue' , width = 0.7)
plt.title("TOP INVESTORS" , color = 'red',fontsize = 15)
plt.xlabel('INVESTORS',fontsize = 10)
plt.ylabel('TIMES INVESTED',fontsize = 10)
plt.xticks(rotation = 30)
plt.grid()
plt.show()
for i in range(1):
    print(investors[i],times[i])