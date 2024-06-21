# running a function with arguments in another thread
# รันฟังก์ชันในอีกเธรดหนึ่ง

from time import sleep, ctime

from threading import Thread

# ฟังก์ชันกำหนดเองที่บล็อกสักครู่
def task(sleep_time, message):
    """
    ฟังก์ชันนี้บล็อกสักครู่แล้วแสดงข้อความ

    Args:
        sleep_time (float): ระยะเวลาการบล็อกในวินาที
        message (str): ข้อความที่จะแสดง
    """
    # บล็อกสักครู่
    sleep(sleep_time)

    # แสดงข้อความ
    print(f"{ctime()} {message}")

# สร้างเธรด
thread = Thread(target=task, args=(1.5, "นี่มาจากเธรดอื่น"))

# รันเธรด
thread.start()

# รอให้เธรดเสร็จสิ้น
print(f"{ctime()} รอเธรด...")

thread.join()