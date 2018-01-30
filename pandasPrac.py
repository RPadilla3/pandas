import pandas as pd

data = pd.read_csv('/Users/Rodolfo/Desktop/pydata_pandas-master/data/coffees.csv')
data.coffees = pd.to_numeric(data.coffees, errors='coerce')
data = data.dropna()
data.coffees = data.coffees.astype(int)
data.timestamp = pd.to_datetime(data.timestamp)
# print(data.describe(include='all'))
data[:5]

data.coffees.plot()
data.plot(x=data.timestamp, style='.-')

# data.tail(n=1-)
#data[data.timestamp < '2013-03-01']

data = data[data.timestamp < '2013-03-01']
data.tail()

data.plot(x=data.timestamp, style='.-', figsize=(15, 4))
data.contributor.value_counts()
data.contributor.value_counts().plot(kind='bar')

weekdays = data.timestamp.dt.weekday
data = data.assign(weekdays=weekdays)
data.head()

weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_dict = {key: weekday_names[key] for key in range(7)}


def day_of_week(idx):
    return weekday_dict[idx]


data.weekdays = data.weekdays.apply(day_of_week)
data.head()

weekday_counts = data.groupby('weekdays').count()
weekday_counts = weekday_counts.loc[weekday_names]
weekday_counts
weekday_counts.coffees.plot(kind='bar')

data.index = data.timestamp
data.index
data.head()

data.drop(['timestamp'], axis=1, inplace=True)
data.head()

data.index
midnights = pd.date_range(data.index[0], data.index[-1], freq='D', normalize=True)
midnights

new_index = midnights.union(data.index)
new_index

upsampled_data = data.reindex(new_index)
upsampled_data.head(10)
upsampled_data = upsampled_data.interpolate(method='time')
upsampled_data.head(10)
