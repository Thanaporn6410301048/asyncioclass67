# Multiprocessing 2 kitkens, 2 cooker, 2 dishes
import multiprocessing
import os
from time import sleep, ctime, time

def cooking(index):
    cooking_time = time()
    print(f'{ctime()} Kitchen - {index} : Begin cooking...PID {os.getpid()}')
    sleep(2)
    duration = time() - cooking_time
    print(f'{ctime()} Kitchen - {index} : Cooked done in {duration:0.2f} seconds')

def kitchen(index):
    cooking(index)

if __name__ == "__main__":
    #Begin of main thread
    print(f'{ctime()} Main          : Start Cooking...PID {os.getpid()}')
    start_time = time()

    # Multi kitchens with each chef
    kitchens = list()
    for index in range(2):
        p = multiprocessing.Process(target=kitchen, args=(index,))
        kitchens.append(p)
        #starting process
        p.start()

''' 
code นี้เป็น multiprocess ด้วยการใช้ function

multi process

ครูเขาให้เรามองว่า process คือห้องครัว 
มีลูกค้าเข้ามาในร้านกี่คน สั่งใข่เจียวกี่จาน ก็สร้างห้องครัวตามจำนวนจานที่สั่ง


multi thread

ครูให้เรามองถาพว่า thread คือพ่อครัวที่ทำงานในห้องครัวห้องเดียว
ความยากคือพ่อครัวจะตะลุมกันใช้ห้องเดียวกันได้อย่างไร
'''
