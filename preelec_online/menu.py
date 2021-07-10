from .models import Camp_online_64, Camp_online_6x
def campmenu(View):
    if View.request.user.groups.exists():
        group = View.request.user.groups.all()[0].name
    else: return False
    #กรณีน้อง
    if group == '64_student':
        menu = [
                ['สมัครเข้าค่าย','64/register/','สมัครเข้าค่าย Pre-Electronics 9','calendar-plus','blue'],
                ['ตรวจสอบตารางกิจกรรม','timetable/', 'ตรวจสอบตารางกิจกรรม Real-Time','tachometer','red'],
            ]
        try:
            db = View.request.user.camp_online_64
            menu = [
                        ['สมัครค่ายเรียบร้อย','.','สมัครค่ายเรียบร้อย','check', 'blue'],
                        ['ตรวจสอบตารางกิจกรรม','timetable/', 'ตรวจสอบตารางกิจกรรม Real-Time','tachometer','red'],
                    ]
        except Camp_online_64.DoesNotExist:
            pass            
    #กรณีรุ่นเรา
    elif group in ['63_student', 'admin','61_student','62_student','guest']:
        menu = [
                    ['ตรวจสอบตารางกิจกรรม','timetable/', 'ตรวจสอบตารางกิจกรรม Real-Time','tachometer','red'],
                    ['บัญชี','6x/statement/', 'ตรวจสอบบัญชี','tachometer','yellow'],
                ]
        try: 
            db = View.request.user.camp_online_6x
            if db.completed is True:
                menu = [
                        ['รายการสั่งซื้อ','6x/shop/','ตราวสอบรายการสั่งซื้อและหลักฐานการโอน','baseball', 'blue'],
                        ['ตรวจสอบตารางกิจกรรม','timetable/', 'ตรวจสอบตารางกิจกรรม Real-Time','tachometer','red'],
                        ['บัญชี','6x/statement/', 'ตรวจสอบบัญชี','tachometer','yellow'],
                    ]
        except Camp_online_6x.DoesNotExist: pass
        if group == 'guest':
            menu.pop(2)
    else :
        menu = [
                    ['ตรวจสอบตารางกิจกรรม','timetable/', 'ตรวจสอบตารางกิจกรรมและจุดนัดพบแบบ Real-Time','tachometer','red'],
                    

                ]
    if View.request.user.is_staff:
        menu.append(['ยืนยันการสั่งซื้อ','6x/orderlist/','ตรวจสอบและยืนยันรายการสั่งซื้อ','baseball', 'blue'])
        menu.append(['เช็คน้องรับของ','64/datalist/','ตรวจสอบสถานะการได้รับของ','book', 'orange'])
    return menu