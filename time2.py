from time import sleep

target_time = 10

def up_timer(secs):
    for i in range(0,secs):
        print(i)
        sleep(1)
    print("時間!")

up_timer(target_time)    
