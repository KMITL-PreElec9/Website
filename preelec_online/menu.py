from .models import Camp_online_64, Camp_online_6x
def campmenu(View):
    if View.request.user.groups.exists():
        group = View.request.user.groups.all()[0].name
    else: return False
    #กรณีน้อง
    if group == '64_student':
        menu = [
                ['<h4>สมัครเข้าค่าย</h4>','64/register/','<p>สมัครเข้าค่าย Pre-Electronics 9</p>','calendar-plus','blue'],
                ['<h4>ตรวจสอบตารางกิจกรรม</h4>','timetable/', '<p>ตรวจสอบตารางกิจกรรม Real-Time</p>','tachometer','red'],
            ]
        try:
            db = View.request.user.camp_online_64
            menu = [
                        ['<h4>สมัครค่ายเรียบร้อย</h4>','.','<p>สมัครค่ายเรียบร้อย</p>','check', 'blue'],
                        ['<h4>ตรวจสอบตารางกิจกรรม</h4>','timetable/', '<p>ตรวจสอบตารางกิจกรรม Real-Time</p>','tachometer','red'],
                    ]
        except Camp_online_64.DoesNotExist:
            pass            
    #กรณีรุ่นเรา
    elif group in ['63_student', 'admin','61_student','62_student','guest']:
        menu = [
<<<<<<< HEAD
                    ['ตรวจสอบตารางกิจกรรม','timetable/', 'ตรวจสอบตารางกิจกรรม Real-Time','tachometer','red'],
                    ['บัญชี','6x/statement/', 'ตรวจสอบบัญชี','tachometer','yellow'],
=======
                    ['<h4 style="color: crimson;">หมดเวลาการสั่งซื้อ</h4>','.','<p style="color: crimson;">หมดเวลาการสั่งซื้อ</p>','tachometer', 'red'],
                    ['<h4>ตรวจสอบตารางกิจกรรม</h4>','timetable/', '<p>ตรวจสอบตารางกิจกรรม Real-Time</p>','baseball','blue'],
                    ['<h4>บัญชี</h4>','6x/statement/', '<p>ตรวจสอบบัญชี</p>','book','yellow'],
>>>>>>> a86cfde8705376c8c578e1770a938cb6a7520950
                ]
        try: 
            db = View.request.user.camp_online_6x
            if db.completed is True:
                menu = [
                        ['<h4>รายการสั่งซื้อ</h4>','6x/shop/','<p>ตราวสอบรายการสั่งซื้อและหลักฐานการโอน</p>','baseball', 'blue'],
                        ['<h4>ตรวจสอบตารางกิจกรรม</h4>','timetable/', '<p>ตรวจสอบตารางกิจกรรม Real-Time</p>','tachometer','red'],
                        ['<h4>บัญชี</h4>','6x/statement/', '<p>ตรวจสอบบัญชี</p>','tachometer','yellow'],
                    ]
        except Camp_online_6x.DoesNotExist: pass
        if group == 'guest':
            menu.pop(2)
    else :
        menu = [
                    ['<h4>ตรวจสอบตารางกิจกรรม</h4>','timetable/', '<p>ตรวจสอบตารางกิจกรรม Real-Time</p>','tachometer','red'],
                    

                ]
    if View.request.user.is_staff:
        menu.append(['<h4>ยืนยันการสั่งซื้อ</h4>','6x/orderlist/','<p>ตรวจสอบและยืนยันรายการสั่งซื้อ</p>','baseball', 'blue'])
        menu.append(['<h4>เช็คน้องรับของ</h4>','64/datalist/','<p>ตรวจสอบสถานะการได้รับของ</p>','book', 'orange'])
    return menu