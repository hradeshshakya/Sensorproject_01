from pymongo.mongo_client import MongoClient
import pandas as pd
import json

# url
url = "mongodb+srv://hradesgdb:9936474743@cluster0.3lnc3.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to server
client = MongoClient(url)

# Create database name and collection name
DATABASE_NAME = "pwskills"
COLLECTION_NAME = "wafer_fault"

df = pd.read_csv(r"C:\Users\kushw\Desktop\Sensorproject\notebooks\wafer_23012020_041211.csv")

df = df.drop("Unnamed: 0",axis=1)

json_record = list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
