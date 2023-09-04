from firebase import firebase
import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# here goes the url to the json file for your Database credentials
cred = credentials.Certificate("DB_Credentials.json")  
firebase_admin.initialize_app(cred , {
    'databaseURL': 'https://' # your firebase databse URL
    }     
)


#empty the database
ref = db.reference('Sensor')
ref.delete()


def listener(event):
    print(event.event_type)  # can be 'put' or 'patch'
    print(event.path)  # relative to the reference, it seems
    print(event.data)  # new data at /reference/event.path. None if deleted

firebase_admin.db.reference('Sensor').listen(listener)
