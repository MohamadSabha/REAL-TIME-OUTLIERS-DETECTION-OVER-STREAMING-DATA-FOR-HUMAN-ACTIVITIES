import sys, json
import json 
from kafka import KafkaConsumer
import csv
from csv import writer


if __name__ == '__main__':
    # Kafka Consumer 
    consumer = KafkaConsumer(
        'result',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='latest'
    )
    
    # open a file to write the results 
    header = ['window','anomalyScore','prediction','label']
    with open('C:\\CSV Results\\data.csv', 'w', encoding='UTF8', newline='') as f:
        writer2 = csv.writer(f)
        # write the header
        writer2.writerow(header)# write multiple rows
        f.close()    


# as long as theres messages in the consumer then they will be writen to the csv file
    for message in consumer:
        print(message.value)
        result_Prediction= json.loads(message.value.decode('utf-8'))
        with open('C:\\CSV Results\\data.csv', 'a', newline='') as f_object:  
            # Pass the CSV  file object to the writer() function
            writer_object = writer(f_object)
            # Result - a writer object
            # Pass the data in the list as an argument into the writerow() function
            writer_object.writerows([[result_Prediction['window'],result_Prediction['anomalyScore'],result_Prediction['prediction'],result_Prediction['label']]])  
            # Close the file object
            f_object.close()    




        