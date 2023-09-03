# REAL-TIME-OUTLIERS-DETECTION-OVER-STREAMING-DATA-FOR-HUMAN-ACTIVITIES
This project aims to propose a methodology to address the challenge of outlier detection over streaming data in real-time. The methodology is based on a developed architectural pipe-line combined synergistically of multiple strategies and technologies such as Apache Kafka and Apache Spark. For effectiveness evaluation purposes, an implementation of the methodology was performed by developing a solution for a real-life problem that detects outliers over streams of human activities.
The developed solution is powered by two systems as follows:

• Android mobile application: for stream data generation of human activities,

• Station-based system: for real-time back-end processing and presentation of data.

The implemented and developed solution was designed to operate in an indoor environment such as shopping centers where the Global Position System (GPS) services are insufficient enough. Hence, the mobile phone’s built-in accelerometer sensor can be utilized. Activities carried out in such environments can be classified as follows: (Walking, jogging, sitting, standing, upstairs, downstairs). When users are performing such activities, the normal behavior of a user can be considered all the aforementioned actions except for the running or jogging activity which is an activity that can be considered or classified as an abnormal behavior to be undertaken in normal circumstances in areas such as shopping malls.


On top of the pipeline, different data preprocessing, transformation, and feature engineering techniques were utilized on the generated streamed data to train a robust machine learning model. Also, to boost the performance of detecting outliers in real-time as much as possible. The isolation Forest Algorithm was adopted to train our machine learning model to achieve the detection task which is less complex, more scalable, and addresses other algorithms’ shortcomings. Finally, a real-time dashboard was designed to show the results of the system and anomalies as they are detected in real-time.


![Implementation flow diagram](https://github.com/MohamadSabha/REAL-TIME-OUTLIERS-DETECTION-OVER-STREAMING-DATA-FOR-HUMAN-ACTIVITIES/assets/40656744/3c677699-2fc1-44f1-a527-1f5fb81da527)
