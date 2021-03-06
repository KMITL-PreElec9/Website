#%%
from numpy import NaN, nan
from .models import *
import pandas as pd
import datetime

def cvtime(oldtime):
    if type(oldtime) != str:
        return None
    time = datetime.datetime.strptime(oldtime, "%m/%d/%Y").strftime("%Y-%m-%d")
    return(time)

fields = ["ชื่อ",'นามสกุล','รหัส','เบอร์โทร','ไอดีไลน์','วันเกิด','ชื่อเล่น', 'อีเมล', 'อีเมล2']

data = pd.read_csv ('data/electronics_64.csv')   
EEData_64.objects.all().delete()
for j in range(0,len(data)):
    db = EEData_64( 
        name = data[fields[0]][j],surname = data[fields[1]][j],
        student_id = data[fields[2]][j],
        line_id = data[fields[4]][j], birth_date = cvtime(data[fields[5]][j]),
        nickname = data[fields[6]][j],email = data[fields[7]][j],email2 = data[fields[8]][j])
    if  not pd.isna(data[fields[3]][j]):
        db.self_telephone_num ='0'+str(int(data[fields[3]][j]))
    else: db.self_telephone_num = None
    db.save()
# %%
