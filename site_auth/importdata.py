#%%
from .models import *
import pandas as pd
import datetime

def cvtime(oldtime):
    if type(oldtime) != str:
        return None
    time = datetime.datetime.strptime(oldtime, "%d/%m/%Y").strftime("%Y-%m-%d")
    return(time)

fields = ["ชื่อ",'นามสกุล','รหัส','เบอร์โทร','ไอดีไลน์','วันเกิด','ชื่อเล่น', 'อีเมล']

data = pd.read_csv ('data/electronics_64.csv')   
EEData_64.objects.all().delete()
for j in range(0,len(data)):
    db = EEData_64( 
        name = data[fields[0]][j],surname = data[fields[1]][j],
        student_id = data[fields[2]][j],
        self_telephone_num ='0'+str(data[fields[3]][j]), 
        line_id = data[fields[4]][j], birth_date = cvtime(data[fields[5]][j]),
         nickname = data[fields[6]][j],email = data[fields[7]][j])
    db.save()
# %%
