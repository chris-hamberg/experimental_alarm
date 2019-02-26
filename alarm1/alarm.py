from do import do_alarm
from day_map import *
import datetime, time, os

def process(hour=8, minute=15):

    mod = 0

    alarm_hour = hour
    alarm_minu = minute
    suffix = 'am' if alarm_hour < 12 else 'pm'

    while True:
        delta = build_delta()
        sentinel = datetime.datetime(delta.year, delta.month, delta.day) 
        
        try:
            assert sunday >= sentinel
        except (NameError, AssertionError):
            for sunday in allsundays(delta.year):
                sunday = datetime.datetime(sunday.year, sunday.month, sunday.day)
                if sunday >= delta:
                    break

        alarm = build_alarm(delta, sunday, alarm_hour, alarm_minu)
        display(alarm, delta, alarm_hour, alarm_minu, suffix, mod)
        mod += 1
        if delta >= alarm:
            do_alarm()

def display(alarm, delta, alarm_hour, alarm_minu, suffix, mod):
    sep = ':' if not mod%2 else ' '
    seconds = (alarm.second - delta.second - 1)%60
    minutes = (alarm.minute - delta.minute - 1)%60
    hours   = (alarm.hour - delta.hour - 1)%24
    days    = (alarm.day - delta.day)%7
    os.system('clear')
    print('### Alarm ### \n[days]:{days}\n[hours]:{hours}\n'
            '[minutes]:{minutes}\n[seconds]:{seconds}'.format_map(vars()))
    print('@ Sun {alarm_hour}{sep}{alarm_minu} {suffix}'.format_map(vars()))
    time.sleep(1)

def build_alarm(delta, sunday, alarm_hour, alarm_minu):
    return datetime.datetime(delta.year, 
           delta.month, sunday.day, alarm_hour, alarm_minu)

def build_delta():
    delta = datetime.datetime.utcnow()
    hour  = (delta.hour + 19)%24
    return datetime.datetime(
            delta.year, delta.month, delta.day, 
            hour, delta.minute, delta.second
            )

def main(): process()

if __name__ == '__main__':
    main()
