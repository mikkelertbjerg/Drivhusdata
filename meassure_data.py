import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

#Read the dataset and store it in 'df'
df = pd.read_csv(r'C:\Users\mwe\Desktop\Github\Drivhusdata\messure_data.csv')
df = df[['date_time', 'temperature']]

#Find the warmest 'date_time'
warmest = df.loc[df['temperature'].idxmax()]
#Print the warmest 'date_time' and its 'temperature'
print(warmest[['date_time', 'temperature']])

#Find the coldest 'date_time'
coldest = df.loc[df['temperature'].idxmin()]
#Print the clodest 'date_time' and its 'temperature'
print(coldest[['date_time', 'temperature']])

#Store the date_time column in its own series
dates = df['date_time']
#Convert the series of 'python objects' to date objects
dates = pd.to_datetime(dates)

#Store the temperature column in its own series
temp = df['temperature']
#Convert the series of 'python objects' to floats
temp = temp.astype(float)

#Naive way of getting min/max temp and corresponding dates.
#min_temp = min(temp)
#min_temp_date = dates[temp.argmin()]
#max_temp = max(temp)
#max_temp_date = dates[temp.argmax()]

#Format and plot the graph with the two preprocessed series
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.plot(dates,temp)
plt.gcf().autofmt_xdate()

#Sudo kode
#===================================================
#/def function getGraph(Date startDate, Date endDate):
#/    query = 'SELECT date_time, temperature FROM messure_data WHERE date_time > @startDate AND date_time < @endDate ORDER BY date_time desc'
#/    dal.getData(query)
#===================================================
