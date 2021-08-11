import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

Cafes=pd.read_csv("https://raw.githubusercontent.com/yasphy/Data-Science-project-Deployement/main/Data%20Test%20-%20Sheet1.csv")
st.title("Nearest cafes and salons")
st.image("https://media-cdn.tripadvisor.com/media/photo-s/15/ba/b1/f4/2-18-largejpg.jpg")
st.write("Given you chose a cafe/salon from given cafe and salon list, you can get 12 nearest cafes as well as salons")
#Displaying data
st.write("# Displaying Data")
#display dataframe
#add column selector
col_names = Cafes.columns.tolist()
st.dataframe(Cafes[st.multiselect("Columns to display",col_names, default = col_names)])
###Plotting
st.write("# Plotting ratings")
##display figures
fig,ax = plt.subplots() #must create a subplot
ax = sns.countplot(Cafes["Rating"], palette ="tab20")
sns.despine()
st.pyplot(fig)
st.map(Cafes)
from math import radians,sin,cos,asin,sqrt
def distance(lat1, lat2, lon1, lon2):
    # The math module contains a function named
    # radians which converts from degrees to radians.
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
      
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
 
    c = 2 * asin(sqrt(a))
    
    # Radius of earth in kilometers. Use 3956 for miles
    r = 6371
      
    # calculate the result
    return(c * r)

#option=st.selectbox('Choose company',Cafes['Company Name'])
#i=Cafes.loc[(Cafes['Company Name']==option)].index
lat=st.number_input('Enter your latitude')
long=st.number_input('Enter your longitude')
k=[]
for m in range(0,340):
    #if (m!=i[0]):
        k.append(distance(Cafes["Latitude"][m],lat,Cafes["Longitude"][m],long))
k.sort()
p=[]
for w in range(0,340):
    for q in range(0,13):
        if (k[q]==distance(Cafes["Latitude"][w],lat,Cafes["Longitude"][w],long)):
            p.append(Cafes["Company Name"][w])
res = []
[res.append(x) for x in p if x not in res]
st.markdown('**__The twelve nearest cafes and salons are__**')
if (len(res)>13):
	for ik in range(1,13):
		st.write(res[ik])
else:	
	for ik in range(1,len(res)):
		st.write(res[ik])

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
