from .models import Camp_online_64, Camp_online_6x
def campmenu(View):
    if View.request.user.groups.exists():
        group = View.request.user.groups.all()[0].name
    else: return False
    #กรณีน้อง
    if group == '64_student':
        menu = [
                ['สมัครเข้าค่าย','64/register/','สมัครเข้าค่าย Pre-Electronics 9','calendar-plus','blue'],
                ['ตรวจสอบตารางกิจกรรม','timetable/', 'ตรวจสอบตารางกิจกรรมและจุดนัดพบแบบ Real-Time','tachometer','red'],
            ]
        try:
            db = View.request.user.camp_online_64
            menu.pop(0)
        except Camp_online_64.DoesNotExist:
            pass            
    #กรณีรุ่นเรา
    elif group in ['63_student', 'admin','61_student','62_student','guest']:
        menu = [
                    ['สั่งซื้อสินค้า','6x/shop/','สั่งซื้อสินค้าที่ระลึก','baseball', 'blue'],
                    ['ตรวจสอบตารางกิจกรรม','timetable/', 'ตรวจสอบตารางกิจกรรมและจุดนัดพบแบบ Real-Time','tachometer','red'],
                ]
        try: 
            db = View.request.user.camp_online_6x
            if db.completed is True:
                menu = [
                        ['รายการสั่งซื้อ','6x/shop/','ตราวสอบรายการสั่งซื้อและหลักฐานการโอน','baseball', 'blue'],
                        ['ตรวจสอบตารางกิจกรรม','timetable/', 'ตรวจสอบตารางกิจกรรมและจุดนัดพบแบบ Real-Time','tachometer','red'],
                        ['บัญชี','6x/statement/', 'ตรวจสอบบัญชี','tachometer','yellow'],
                        ]
        except Camp_online_6x.DoesNotExist: pass

    else :
        menu = [
                    ['ตรวจสอบตารางกิจกรรม','timetable/', 'ตรวจสอบตารางกิจกรรมและจุดนัดพบแบบ Real-Time','tachometer','red'],

                ]
    if View.request.user.is_staff:
        menu.append(['ยืนยันการสั่งซื้อ','6x/orderlist/','ตรวจสอบและยืนยันรายการสั่งซื้อ','baseball', 'blue'])
        menu.append(['เช็คน้องรับของ','64/datalist/','ตรวจสอบสถานะการได้รับของ','book', 'orange'])
    return menu