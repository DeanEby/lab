import pandas as pd
from datetime import datetime
path = "../../../mango_tango_test_data/phemrumour.csv"

df = pd.read_csv(path)

month_convert_dict = {
        "Jan" : "01",
        "Feb" : "02",
        "Mar" : "03",
        "Apr" : "04",
        "May" : "05",
        "Jun" : "06",
        "Jul" : "07",
        "Aug" : "08",
        "Sep" : "09",
        "Oct" : "10",
        "Nov" : "11",
        "Dec" : "12"
        }


# print(df.head())
timestamp_list = df['timestamp']

new_timestamp_list = []
for i in timestamp_list:
    new_timestamp = []
    # The timestamp follows the following format:
    # day_of_week month day 24/hr_time ms year
    timestamp_components = i.split()
    # add converted month
    new_timestamp.append(month_convert_dict[timestamp_components[1]])
    # print(new_timestamp_list)
    # add day
    new_timestamp.append(timestamp_components[2])
    # add 24/hr_time
    new_timestamp.append(timestamp_components[3])
    # add year
    new_timestamp.append(timestamp_components[5])
    
    new_timestamp = " ".join(new_timestamp)
    new_timestamp = datetime.strptime(new_timestamp, '%m %d %H:%M:%S %Y')    
    # print(new_timestamp_list)
    new_timestamp_list.append(new_timestamp)

df['timestamp'] = new_timestamp_list

# print(df['timestamp'])
df.to_csv("pheme_timestamp_corrected")




