from time import sleep

target_time = 10

def up_timer(secs):
    for i in range(secs,-1,-1):
        print(i)
        sleep(1)
    print("時間!")

up_timer(target_time)
