import time, sys, os

def do_alarm():
    data = list(os.popen('date'))[0].strip()
    with open('/home/chris/alarm_sanity_check.txt', 'w') as fhand:
        data = 'alarm.py @ ' + data 
        fhand.write(data)
    sys.exit(0)
    while True:
        os.system('play /home/chris/.system/alarm/beep-09.wav')
        time.sleep(2)

if __name__ == '__main__':
    do_alarm()
