import time, sys, os

#ALARM_DAY = 'Fri'
#ALARM_HOU = str(12+11)
#ALARM_MIN = '21'

def process(ALARM_DAY, ALARM_HOU, ALARM_MIN):
    
    ticks = 0

    while True:

        display(ticks, ALARM_DAY, ALARM_HOU, ALARM_MIN)
        ticks += 1 if ticks < 10 else -9

        date = list(os.popen('date'))[0].strip().split()
        day, clock = date[0], date[3]
        hour, minute, second = clock.split(':')

        if (    day == ALARM_DAY
                ) and (
                hour <= ALARM_HOU
                ) and (
                int(ALARM_MIN) <= int(minute)
                ): alarm()

        time.sleep(1)

def alarm():
    path = os.path.join(os.getcwd(), 'beep-09.wav')
    os.system('play {path}'.format_map(vars()))

def display(ticks, day, hour, minute):
    suffix = 'pm' if int(hour) > 11 else 'am'
    hour   = int(hour)%12
    delimiter = ':' if not ticks%2 else ' '
    os.system('clear')
    print('[simple alarm] @ {day} {hour}{delimiter}{minute} {suffix}'.format_map(vars()))

def parse():
    
    try:
        day, hour, minute = sys.argv[1:]
    except ValueError:
        print('~$ python simple_alarm.py <day> <hour> <minute>')
        print('<day> example: Fri')
        print('<hour> is in 24 hour time')
        sys.exit(0)
    else:
        return day, hour, minute

def main():
    day, hour, minute = parse()
    process(day, hour, minute)

if __name__ == '__main__':
    main()
