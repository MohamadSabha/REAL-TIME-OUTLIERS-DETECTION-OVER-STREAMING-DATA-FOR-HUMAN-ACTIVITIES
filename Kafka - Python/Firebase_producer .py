from firebase import firebase
import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import time 
import json 
import random 
from datetime import datetime
from data_generator import generate_message
from kafka import KafkaProducer
    
# here goes the url to the json file for your Database credentials
cred = credentials.Certificate("DB_Credentials.json")  
firebase_admin.initialize_app(cred , {
    'databaseURL': 'https://' # your firebase databse URL
    }     
)

# Messages will be serialized as JSON 
def serializer(message):
    return json.dumps(message).encode('utf-8')

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=serializer
)

def listener(event):
    print(event.event_type)  # can be 'put' or 'patch'
    print(event.path)  # relative to the reference, it seems
    dummy_message = event.data
    print(f'Producing message @ {datetime.now()} | Message = {str(dummy_message)}')
    producer.send('messages', dummy_message)

firebase_admin.db.reference('Sensor').listen(listener)


