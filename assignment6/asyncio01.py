import asyncio  # นำเข้าโมดูล asyncio เพื่อใช้สำหรับการเขียนโปรแกรมแบบ asynchronous

# define an asynchronous iterator
class AsyncIterator():  # สร้างคลาส AsyncIterator
    # constructor, define some state
    def __init__(self):  # นิยามฟังก์ชัน __init__ เป็นคอนสตรัคเตอร์ของคลาส
        self.counter = 0  # กำหนดตัวแปร counter ให้มีค่าเริ่มต้นเป็น 0

    # create an instance of the iterator
    def __aiter__(self):  # นิยามฟังก์ชัน __aiter__ สำหรับการสร้างอินสแตนซ์ของ iterator
        return self  # คืนค่า self ซึ่งเป็นอินสแตนซ์ของคลาส

    # return the next awaitable
    async def __anext__(self):  # นิยามฟังก์ชัน __anext__ สำหรับคืนค่าของ iterator แบบ asynchronous
        # check for no further items
        if self.counter >= 10:  # ตรวจสอบถ้าตัวแปร counter มีค่ามากกว่าหรือเท่ากับ 10
            raise StopAsyncIteration  # หยุดการ iteration ถ้าตัวแปร counter มีค่ามากกว่าหรือเท่ากับ 10
        # increment the counter
        self.counter += 1  # เพิ่มค่าตัวแปร counter ขึ้น 1
        # simulate work
        await asyncio.sleep(1)  # จำลองการทำงานด้วยการหยุดรอ 1 วินาที
        # return the counter value
        return self.counter  # คืนค่าของตัวแปร counter

# main coroutine
async def main():  # นิยามฟังก์ชัน main ซึ่งเป็นฟังก์ชันหลักที่ทำงานแบบ asynchronous
    # loop over async iterator with async for loop
    async for item in AsyncIterator():  # ใช้คำสั่ง async for เพื่อ loop ผ่านค่าใน AsyncIterator
        print(item)  # แสดงค่าของ item ที่ได้จาก iterator

# execute the asyncio program
asyncio.run(main())  # เรียกใช้ฟังก์ชัน main ผ่าน asyncio.run เพื่อเริ่มต้นการทำงานแบบ asynchronous