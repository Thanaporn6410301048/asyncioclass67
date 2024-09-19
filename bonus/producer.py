from aiokafka import AIOKafkaProducer
import asyncio

async def send_one():
    # สร้าง AIOKafkaProducer ที่เชื่อมต่อกับ Kafka broker ที่ localhost:9092
    producer = AIOKafkaProducer(
        bootstrap_servers='localhost:9092'
    )
    # เริ่มต้น producer และเชื่อมต่อกับ broker
    await producer.start()
    try:
        # ส่งข้อความไปยัง topic "my_topic"
        await producer.send_and_wait("my_topic", b"Super message")
        print("Message sent successfully")
    finally:
        # รอให้ส่งข้อความที่ค้างอยู่ทั้งหมด หรือหมดอายุ
        await producer.stop()

# รันฟังก์ชัน send_one ใน event loop
asyncio.run(send_one())
