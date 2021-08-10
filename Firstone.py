import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

Cafes=pd.read_csv("https://raw.githubusercontent.com/yasphy/Data-Science-project-Deployement/main/Data%20Test%20-%20Sheet1.csv")
st.title("Least travelled cafes")
st.image("https://media-cdn.tripadvisor.com/media/photo-s/15/ba/b1/f4/2-18-largejpg.jpg")
st.write("Given you chose a cafe from given cafe list, you can get 12 nearest cafes")
#Displaying data
st.write("# Displaying Data")
#display dataframe
#add column selector
col_names = Cafes.columns.tolist()
st.dataframe(Cafes[st.multiselect("Columns to display",col_names, default = col_names)])
###Plotting
st.write("# Plotting")
##display figures
fig,ax = plt.subplots() #must create a subplot
ax = sns.countplot(Cafes["Rating"], palette ="tab20")
sns.despine()
st.pyplot(ax)
import math
def distance(lat1, lat2, lon1, lon2):
    # The math module contains a function named
    # radians which converts from degrees to radians.
    lon1 = math.radians(lon1)
    lon2 = math.radians(lon2)
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
      
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
 
    c = 2 * math.asin(math.sqrt(a))
    
    # Radius of earth in kilometers. Use 3956 for miles
    r = 6371
      
    # calculate the result
    return(c * r)

option=st.selectbox('Choose company',Cafes['Company Name'])
i=Cafes.loc[(Cafes['Company Name']==option)].index
k=[]
for m in range(0,339):
    if (m!=i[0]):
        k.append(distance(Cafes["Latitude"][m],Cafes["Latitude"][i[0]],Cafes["Longitude"][m],Cafes["Longitude"][i[0]]))
k.sort()
p=[]
for w in range(0,339):
    for q in range(0,12):
        if (k[q]==distance(Cafes["Latitude"][w],Cafes["Latitude"][i[0]],Cafes["Longitude"][w],Cafes["Longitude"][i[0]])):
            p.append(Cafes["Company Name"][w])
res = []
[res.append(x) for x in p if x not in res]
st.markdown('**__The twelve nearest cafes are__**')
for ik in range(1,13):
	st.write(res[ik])

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
