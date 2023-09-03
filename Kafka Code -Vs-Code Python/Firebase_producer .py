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
    
cred = credentials.Certificate("C:\\Users\\MHD\\Desktop\\kafka-installation\\kafka-python-code\\accelerometer-db-firebase-adminsdk-8t564-607f4ea317.json")
firebase_admin.initialize_app(cred , {
    'databaseURL': ''
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
    #print(event.data)  # new data at /reference/event.path. None if deleted

firebase_admin.db.reference('Sensor').listen(listener)


