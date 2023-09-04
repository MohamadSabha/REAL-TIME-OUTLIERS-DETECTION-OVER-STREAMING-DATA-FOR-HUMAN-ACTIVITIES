package com.example.myapplication1;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.os.Bundle;
import android.text.format.Time;
import android.util.Log;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.TextView;

import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ServerValue;

import java.time.LocalDateTime;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;
import java.util.TimeZone;

public class MainActivity extends AppCompatActivity  implements SensorEventListener {
    private RadioGroup My_radioGroup;
    private boolean Outlier_Pressed =false;
    private static final String TAG = "MainActivity";
    private SensorManager sensorManager;
    Sensor accelerometer;
    TextView Xvalue,Yvalue,Zvalue;
    FirebaseDatabase db = FirebaseDatabase.getInstance();
    private DatabaseReference  databaserefrence =FirebaseDatabase.getInstance().getReference("Sensor");
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        getSupportActionBar().setDisplayShowTitleEnabled(false);
        Xvalue= (TextView) findViewById(R.id.Xvalue);
        Yvalue= (TextView) findViewById(R.id.Yvalue);
        Zvalue= (TextView) findViewById(R.id.Zvalue);
        Log.d(TAG, "onCreate: Initilizing sensor services ");
        sensorManager = (SensorManager) getSystemService(Context.SENSOR_SERVICE);
        accelerometer = sensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER);
        sensorManager.registerListener(MainActivity.this, accelerometer, SensorManager.SENSOR_DELAY_NORMAL);
        Log.d(TAG, "onCreate: Register the accelerometer sensor");
        db.getReference(Sensor.class.getSimpleName());
        My_radioGroup = findViewById(R.id.radio_Group);
        My_radioGroup.setOnCheckedChangeListener(new RadioGroup.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(RadioGroup group, int checkedId) {
                switch (checkedId)
                {
                    case R.id.radio_Normal:
                        Outlier_Pressed=false;
                        break;
                    case R.id.radio_Outlier:
                        Outlier_Pressed=true;
                        break;
                }
            }
        });
    }
    @Override
    public void onAccuracyChanged(Sensor sensor, int accuracy) {
    }
    @Override
    public void onSensorChanged(SensorEvent event) {
        Log.d(TAG, "onSensorChanged: x:"+event.values[0]+"y:"+event.values[1]+"z:"+event.values[2]+"");
        Xvalue.setText("X Value :"+event.values[0]);
        Yvalue.setText("Y Value :"+event.values[1]);
        Zvalue.setText("Z Value :"+event.values[2]);
        Map map = new HashMap();
        if (Outlier_Pressed==true)
        {
            float float_label = Outlier_Pressed ? 1 : 0;
            Record R = new Record(event.values[0],event.values[1],event.values[2],"Huawei p30",ServerValue.TIMESTAMP,float_label);
            databaserefrence.push().setValue(R);
        }
        else
        {
            float float_label = Outlier_Pressed ? 1 : 0;
            Record R = new Record(event.values[0],event.values[1],event.values[2],"Huawei p30",ServerValue.TIMESTAMP,float_label);
            databaserefrence.push().setValue(R);
        }
    }
}