# running a function in another thread

# รันฟังก์ชันในอีกเธรดหนึ่ง

from time import sleep, ctime

from threading import Thread

# ฟังก์ชันกำหนดเองที่บล็อกสักครู่
def task():
    # บล็อกสักครู่
    sleep(1)

    # แสดงข้อความ
    print(f'{ctime()} from another thread')

# สร้างเธรด
thread = Thread(target=task)

# รันเธรด
thread.start()

# รอให้เธรดเสร็จสิ้น
print(f'{ctime()} from main thread')

thread.join()

