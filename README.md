# REAL-TIME-OUTLIERS-DETECTION-OVER-STREAMING-DATA-FOR-HUMAN-ACTIVITIES

This project aims to propose a methodology to address the challenge of outlier detection over streaming data in real-time. The methodology is based on a developed architectural pipe-line combined synergistically of multiple strategies and technologies such as Apache Kafka and Apache Spark. For effectiveness evaluation purposes, an implementation of the methodology was performed by developing a solution for a real-life problem that detects outliers over streams of human activities.
The developed solution is powered by two systems as follows:

• Android mobile application: for stream data generation of human activities,

• Station-based system: for real-time back-end processing and presentation of data.

The implemented and developed solution was designed to operate in an indoor environment such as shopping centers where the Global Position System (GPS) services are insufficient enough. Hence, the mobile phone’s built-in accelerometer sensor can be utilized. Activities carried out in such environments can be classified as follows: (Walking, jogging, sitting, standing, upstairs, downstairs). When users are performing such activities, the normal behavior of a user can be considered all the aforementioned actions except for the running or jogging activity which is an activity that can be considered or classified as an abnormal behavior to be undertaken in normal circumstances in areas such as shopping malls.


On top of the pipeline, different data preprocessing, transformation, and feature engineering techniques were utilized on the generated streamed data to train a robust machine learning model. Also, to boost the performance of detecting outliers in real-time as much as possible. The isolation Forest Algorithm was adopted to train our machine learning model to achieve the detection task which is less complex, more scalable, and addresses other algorithms’ shortcomings. Finally, a real-time dashboard was designed to show the results of the system and anomalies as they are detected in real-time.

<ins>**Human Activity Recognition Framework Design**</ins>

Aiming to summarize the general and typical picture of the designing and implementing of a pattern recognition system such as human activity recognition, the next figure is introduced which shows how human activity recognition system's main modules and parts are constructed together in order to achieve the task of activity recognition successfully. several modules can be noticed in the previous diagram in which the human activity recognition system consists of a data collection step, Data segmentation, feature Engineering, and the training of the model selected. And as a result of the earlier processes, we will finally be able to detect and recognize the desired activity.

![Activity Recognition (1)](https://github.com/MohamadSabha/REAL-TIME-OUTLIERS-DETECTION-OVER-STREAMING-DATA-FOR-HUMAN-ACTIVITIES/assets/40656744/e9f1c7b0-4511-485d-b9ec-347d5e26f06c)

<ins> **Human Activity Recognition Taxonomy diagram ** </ins>

The following diagram illustrates a taxonomy diagram that summarizes most of the conducted research and works on the area of human activity recognition in which it shows different considered points where a one can keep in mind when planning to implement new work related to this area such as recognition types, used techniques, applied algorithms, data sources as well as and application areas.

![Activity Recognition flow diagram](https://github.com/MohamadSabha/REAL-TIME-OUTLIERS-DETECTION-OVER-STREAMING-DATA-FOR-HUMAN-ACTIVITIES/assets/40656744/cc9d06a6-9954-4924-bf47-a82ecdb7d5b1)


<ins>**Methodology Architecture**</ins>

The following figure shows our methodology architecture and how each phase of the ETL is modified based on our methodology approach and system requirements.

![MethodologyNew](https://github.com/MohamadSabha/REAL-TIME-OUTLIERS-DETECTION-OVER-STREAMING-DATA-FOR-HUMAN-ACTIVITIES/assets/40656744/d5d5c9b7-a62a-4632-9293-a1cfde5b2e97)


Next is the implementation diagram of our system. The main idea here is to be able to receive the data as it is generated from the user's phone and perform analysis and processing techniques using different tools as well as deploying a machine learning model on the top of the stream by conducting an integration of different distributed stream processing and analysis frameworks such as Apache Spark and spark Kafka to be able to monitor and predict the user outliers in real-time and give action based on it if needed.


<ins>**System implementation**</ins>

The implementation Process flow is divided into two main phases, the Training phase which will be working with a historical dataset, and the implementation phase which will be working with our DataStream in real-time. Apache Spark distributed Stream Processing engine will be employed in the background of those two phases, in addition, Apache Kafka Streaming platform will be employed as a messaging system and a decoupling layer, and finally, an Isolation Forest model is trained and applied on top of streaming data as it flows in the system.

![Implementation flow diagram](https://github.com/MohamadSabha/REAL-TIME-OUTLIERS-DETECTION-OVER-STREAMING-DATA-FOR-HUMAN-ACTIVITIES/assets/40656744/3c677699-2fc1-44f1-a527-1f5fb81da527)


<ins>**Used Dataset**</ins>


you can find the used dataset at : [WISDM LabDataset](https://www.cis.fordham.edu/wisdm/dataset.php#actitracker)




