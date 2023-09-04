from asyncio.windows_events import NULL
import sys, json
import json 
from kafka import KafkaConsumer
#Streaming data 
from bokeh.models import Legend
from functools import partial
from bokeh.models.widgets import DataTable, DateFormatter, TableColumn ,Div
from multiprocessing.sharedctypes import Value
from turtle import color, width
from bokeh.models import Slider

from bokeh.io import curdoc ,show
from bokeh.models import ColumnDataSource, DatetimeTickFormatter , Select
from bokeh.layouts import layout
from bokeh.plotting import figure
from datetime import datetime
from math import radians
from matplotlib.pyplot import title 
import numpy as np
from requests import options
from soupsieve import select
import time
from bokeh.models import CustomJS
import js2py
from bokeh.layouts import column
from bokeh.models import HTMLTemplateFormatter
# wqssssssssssssssssssssssssssssssssssssss

consumer_Prediction = KafkaConsumer(
        'result',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='latest',
                        )

consumer_Raw = KafkaConsumer(
        'messages',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='latest',
                        )


source_Prediction = ColumnDataSource(dict(x=[],y=[]))
source_x = ColumnDataSource(dict(x=[],y=[]))
source_y = ColumnDataSource(dict(x=[],y=[]))
source_z = ColumnDataSource(dict(x=[],y=[]))
# source_Table_Raw = ColumnDataSource(dict(xvalue=[],yvalue=[],))

columns = [
        TableColumn(field="xvalue", title="xvalue",),
        TableColumn(field="yvalue", title="yvalue",),
    ]

 
#create figure 
p_Prediction= figure(x_axis_type="datetime",width=1100,height=350)
p_Raw= figure(x_axis_type="datetime",width=1200,height=350)
sliderx = Slider(start=-10, end=10, value=0, step=.01, title="xvalue",bar_color='orange')
slidery = Slider(start=-10, end=10, value=0, step=.01, title="yvalue",bar_color='green')
sliderz = Slider(start=-10, end=10, value=0, step=.01, title="zvalue", bar_color='blue')
sliderx.margin=(20, 5, 20, 5)
slidery.margin=(20, 5, 20, 5)
sliderz.margin=(20, 5, 20, 5)


#create data source


def get_html_formatter(my_col):
    template = """
        <div style="background:<%= 
            (function colorfromint(){
                if(prediction == '1.0'){
                    return('#ff0000')}
                else if (prediction == '0.0')
                    {return('#009688')}
                }()) %>; 
            color: white"> 
        <%= value %>
        </div>
    """.replace('prediction',my_col)
    
    return HTMLTemplateFormatter(template=template)



source_Table_Raw = ColumnDataSource(dict(anomalyScore=[],prediction=[],label=[]))
columns = [
        TableColumn(field="anomalyScore", title="anomalyScore",),
        TableColumn(field="prediction", title="prediction",formatter=get_html_formatter('prediction')),
        TableColumn(field="label", title="label",formatter=get_html_formatter('label'))]
data_table_Raw = DataTable(source=source_Table_Raw, columns=columns, width=400, height=280,scroll_to_selection=True,selectable =True ,background="red")




legend_Raw = Legend(items=[
    ("xvalue",   [p_Raw.line(x="x",y="y",source=source_x,color='orange')]),
    ("yvalue", [p_Raw.line(x="x",y="y",source=source_y,color='green')]),
    ("zvalue", [p_Raw.line(x="x",y="y",source=source_z,color='blue')])
], location=(0, 150))
p_Raw.add_layout(legend_Raw, 'right')

#generate data 

p_Prediction.line(x="x",y="y",source=source_Prediction)


counter = 0 
# create periodice function
def Update_Prediction():
    for message in consumer_Prediction:
        result_Prediction= json.loads(message.value.decode('utf-8'))    
        break

    new_Data_Prediction=dict(x=[datetime.now()],y=[result_Prediction['anomalyScore']])
    new_Data_TAble_Raw = dict(anomalyScore=[result_Prediction['anomalyScore']],
    prediction=[result_Prediction['prediction']], label=[result_Prediction['label']])

     
    source_Prediction.stream(new_Data_Prediction,rollover=200)

     
    teste=int(len(source_Table_Raw.data['anomalyScore']))
    source_Table_Raw.selected.indices = [teste-1]
    source_Table_Raw.stream(new_Data_TAble_Raw,rollover=200)

    if float(result_Prediction['prediction']) == 1 :
        p_Prediction.circle(x=[datetime.now()],y=result_Prediction['anomalyScore'],color="firebrick",size=6, line_color="firebrick") 
    curdoc().add_next_tick_callback(partial(update_Raw))
        
  
def update_Raw():
    for message in consumer_Raw:
        result_raw= json.loads(message.value.decode('utf-8'))    
        break
    
    if result_raw['xvalue'] != NULL :   
        new_Data_x=dict(x=[datetime.now()],y=[result_raw['xvalue']])
        new_Data_y=dict(x=[datetime.now()],y=[result_raw['yvalue']])
        new_Data_z=dict(x=[datetime.now()],y=[result_raw['zvalue']])
    
        source_x.stream(new_Data_x,rollover=100)
        source_y.stream(new_Data_y,rollover=100)
        source_z.stream(new_Data_z,rollover=100)
        sliderx.value = int(result_raw['xvalue'])
        slidery.value = int(result_raw['yvalue'])
        sliderz.value = int(result_raw['zvalue'])
        if int(result_raw['xvalue'])<0:
            sliderx.bar_color="red"
        else: 
            sliderx.bar_color="orange"

        if int(result_raw['yvalue'])<0:
            slidery.bar_color="red"
        else: 
            slidery.bar_color="green"
        if int(result_raw['zvalue'])<0:
            sliderz.bar_color="red"
        else:
            sliderz.bar_color="blue" 

        global counter
        counter+=1
        if counter>=30:
            counter = 0 
            curdoc().add_next_tick_callback(partial(Update_Prediction))


p_Raw.title.text="X , Y , Z Values from the Raw Streaming Feed "
p_Prediction.title.text="the Anomaly socre and Detecting Outliers Sgtreaming Feed" 


div_Sliders = Div(text="""<P>Changes of oreantation Values within the 3 axises :</P>
<ul>
    <li>X-axis</li>
    <li>Y-axis</li>
    <li>Z-axis</li>
</ul>""",
width=200, height=100)

div_Table = Div(text="""<P>Prediction Monitoring Table</P>""",
width=200, height=20)


date_pattern = ["%y-%m-%d\n%H:%M:%S"]

p_Prediction.xaxis.formatter =DatetimeTickFormatter (
        seconds = date_pattern,
        minsec=date_pattern,
        minutes=date_pattern,
        hourmin=date_pattern,
        hours=date_pattern,
        days=date_pattern,
        months=date_pattern,
        years=date_pattern
)

p_Prediction.xaxis.major_label_orientation=radians(80)
p_Prediction.xaxis.axis_label="Time"
p_Prediction.yaxis.axis_label="AnomalyScore"


p_Raw.xaxis.major_label_orientation=radians(80)
p_Raw.xaxis.axis_label="Time"
p_Raw.yaxis.axis_label="Raw_Value"

sliders = column(div_Sliders,sliderx, slidery, sliderz)

Table_Column=column(div_Table,data_table_Raw)

#config layout
lay_out =layout([p_Prediction, Table_Column],
                  [sliders,p_Raw])

curdoc().title="streaming example"
curdoc().add_root(lay_out)
curdoc().theme = "night_sky"
curdoc().add_periodic_callback(update_Raw, 100)
