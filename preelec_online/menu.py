from .models import Camp_online_64, Camp_online_6x
def campmenu(View):
    if View.request.user.groups.exists():
        group = View.request.user.groups.all()[0].name
    else: return False
    #กรณีน้อง
    if group == '64_student':
        try:
            db = View.request.user.camp_online_64
            menu = [
                ['ตรวจสอบข้อมูล','64/viewdata/','ตรวจสอบและแก้ไขข้อมูลที่ลงทะเบียน','file', 'orange'],
                ['ตรวจสอบตารางกิจกรรม','64/table/', 'ตรวจสอบตารางกิจกรรมและจุดนัดพบ','tachometer', 'red'],
                ['ใบขออนุญาตผู้ปกครอง','64/parent/', 'ดาวน์โหลด และพิมพ์ใบขออนุญาตผู้ปกครอง','book-open', 'yellow'],
                ['ยกเลิกการสมัคร','64/unregister/', 'ยกเลิกการสมัครเข้าค่าย','calendar-x', 'pink'],
            ]
        except Camp_online_64.DoesNotExist:
            
            menu = [
                ['สมัครเข้าค่าย','64/register/','สมัครเข้าค่าย Pre-Electronics 9','calendar-plus','blue'],
               # ['ตรวจสอบตารางกิจกรรม','64/table/', 'ตรวจสอบตารางกิจกรรมและจุดนัดพบแบบ Real-Time','tachometer','orange'],
            ]
    #กรณีรุ่นเรา
    elif group in ['63_student', 'admin','61_student','62_student','gust']:
        menu = [
                    ['สั่งซื้อสินค้า','6x/shop/','สมัครเข้าทำค่าย Pre-Elec 9','baseball', 'blue'],
                    
                ]
        try: 
            db = View.request.user.camp_online_6x
            if db.completed is True:
                menu = [
                        ['รายการสั่งซื้อ','6x/shop/','ตราวสอบรายการสั่งซื้อและหลักฐานการโอน','baseball', 'blue'],
                        ]
        except Camp_online_6x.DoesNotExist: pass

    else :
        menu = [
                    ['สั่งซื้อสินค้า','6x/shop/','สมัครเข้าทำค่าย Pre-Elec 9','baseball', 'blue']

                ]
    if View.request.user.is_staff:
        menu.append(['ยืนยันการสั่งซื้อ','6x/orderlist/','ยืนยันรายการสั่งซื้อ','baseball', 'blue'])
    return menu