package com.example.myapplication1;
import com.google.android.gms.tasks.Task;

import java.sql.Date;
import java.sql.Time;
import java.sql.Timestamp;
import java.util.Map;
public class Record {
    private Float Xvalue;
    private Float Yvalue;
    private Float Zvalue;
    private String DeviceID;
    private Map TimeStamp;
    private Float Label;
    public Record() {
    }
    public Record( Float xvalue, Float yvalue, Float zvalue,String deviceid,Map timeStamp,Float label) {
        Xvalue = xvalue;
        Yvalue = yvalue;
        Zvalue = zvalue;
        DeviceID =deviceid;
        TimeStamp =timeStamp;
        Label =label;
    }
    public Float getXvalue() {
        return Xvalue;
    }
    public void setXvalue(Float xvalue) {
        Xvalue = xvalue;
    }
    public Float getYvalue() {
        return Yvalue;
    }
    public void setYvalue(Float yvalue) {
        Yvalue = yvalue;
    }
    public Float getZvalue() {
        return Zvalue;
    }
    public void setZvalue(Float zvalue) {
        Zvalue = zvalue;
    }
    public String getDeviceID() { return DeviceID; }
    public void setDeviceID(String deviceid) { DeviceID = deviceid; }
    public Float getLabel() { return Label; }
    public void setLabel(String label) { DeviceID = label; }
    public Map  getTimestamp() {return TimeStamp;}
    public void setTimestamp(Map timestamp) {this.TimeStamp= timestamp;}
}