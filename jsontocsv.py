import pandas as pd
from io import StringIO


# read the entire file into a python array
with open('mine.json', 'r', encoding ='utf-8-sig') as f:
    data = f.readlines()

# remove the trailing "\n" from each line
data = map(lambda x: x.rstrip(), data)

# each element of 'data' is an individual JSON object.
# i want to convert it into an *array* of JSON objects
# which, in and of itself, is one large JSON object
# basically... add square brackets to the beginning
# and end, and have all the individual business JSON objects
# separated by a comma
data_json_str = "[" + ','.join(data) + "]"
newdf = pd.read_json(StringIO(data_json_str))
newdf.to_csv("mine.csv", encoding ='utf-8-sig')
# # now, load it into pandas
# data_df = pd.read_json(data_json_str)
# #print (data_json_str)